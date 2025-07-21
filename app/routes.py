import random
from flask import (render_template, url_for, flash, redirect, request, Blueprint, session, abort)
from flask_login import login_user, current_user, logout_user, login_required
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flask_wtf.file import FileField, FileAllowed

from app import db, bcrypt
from app.models import User, MatchHistory
from app.nlp_processor import extract_text_from_file, calculate_match_score

# --- Form Classes ---
class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6)])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Create Account')

    def validate_username(self, username):
        if User.query.filter_by(username=username.data).first():
            raise ValidationError('Username is taken.')

    def validate_email(self, email):
        if User.query.filter_by(email=email.data).first():
            raise ValidationError('Email is already registered.')

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')

class OTPForm(FlaskForm):
    otp = StringField('OTP', validators=[DataRequired(), Length(min=6, max=6)])
    submit = SubmitField('Verify Account')
    
class MatcherForm(FlaskForm):
    resume = FileField('Upload Your Resume', validators=[
        DataRequired(),
        FileAllowed(['pdf', 'docx', 'txt'], 'Only PDF, DOCX, or TXT files allowed!')
    ])
    job_description = TextAreaField('Paste Job Description', validators=[DataRequired()])
    submit = SubmitField('Calculate Match Score')

# --- Blueprints ---
auth_bp = Blueprint('auth', __name__, url_prefix='/auth')
main_bp = Blueprint('main', __name__)

# --- Authentication Routes ---
@auth_bp.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password_hash=hashed_password)
        db.session.add(user)
        db.session.commit()
        
        otp = str(random.randint(100000, 999999))
        session['otp_for_verification'] = otp
        session['user_id_for_verification'] = user.id
        
        flash(f"Your OTP is: {otp}", 'otp-display')
        return redirect(url_for('auth.verify_otp'))
        
    return render_template('auth/register.html', title='Register', form=form)

@auth_bp.route("/verify_otp", methods=['GET', 'POST'])
def verify_otp():
    if 'otp_for_verification' not in session:
        flash('Invalid request. Please register first.', 'danger')
        return redirect(url_for('auth.register'))
        
    form = OTPForm()
    if form.validate_on_submit():
        if form.otp.data == session['otp_for_verification']:
            user = User.query.get(session['user_id_for_verification'])
            user.is_verified = True
            db.session.commit()
            
            session.pop('otp_for_verification', None)
            session.pop('user_id_for_verification', None)
            
            flash('Account verified successfully! You can now log in.', 'success')
            return redirect(url_for('auth.login'))
        else:
            flash('Invalid OTP. Please try again.', 'danger')
            
    return render_template('auth/verify_otp.html', title='Verify OTP', form=form)

@auth_bp.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password_hash, form.password.data):
            if not user.is_verified:
                flash('Account not verified. Please register again to get a new OTP.', 'warning')
                return redirect(url_for('auth.register'))
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('main.index'))
        else:
            flash('Login failed. Check email and password.', 'danger')
    return render_template('auth/login.html', title='Login', form=form)

@auth_bp.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('main.index'))

# --- Main Application Routes ---
@main_bp.route("/", methods=['GET', 'POST'])
@login_required
def index():
    form = MatcherForm()
    if form.validate_on_submit():
        resume_text = extract_text_from_file(form.resume.data.stream, form.resume.data.filename.rsplit('.', 1)[1].lower())
        if not resume_text:
            flash('Could not extract text from resume. Try a different file.', 'danger')
            return redirect(url_for('main.index'))

        score = calculate_match_score(resume_text, form.job_description.data)

        new_match = MatchHistory(job_description=form.job_description.data, resume_text=resume_text, score=int(score), author=current_user)
        db.session.add(new_match)
        db.session.commit()
        return redirect(url_for('main.results', score=score))
        
    return render_template('main/index.html', title='Home', form=form)

@main_bp.route("/results")
@login_required
def results():
    score = request.args.get('score', 0, type=float)
    return render_template('main/results.html', title='Match Results', score=score)

@main_bp.route("/history")
@login_required
def history():
    matches = MatchHistory.query.filter_by(user_id=current_user.id).order_by(MatchHistory.timestamp.desc()).all()
    return render_template('main/history.html', title='History', matches=matches)

@main_bp.route("/delete_history/<int:history_id>", methods=['POST'])
@login_required
def delete_history(history_id):
    history_item = MatchHistory.query.get_or_404(history_id)
    if history_item.author != current_user:
        abort(403)
    db.session.delete(history_item)
    db.session.commit()
    flash('History item deleted.', 'success')
    return redirect(url_for('main.history'))