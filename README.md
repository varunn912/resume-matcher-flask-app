AI Resume Matcher

Flask | Python | NLP | SQLite

A full-stack web application that leverages Natural Language Processing (NLP) to intelligently evaluate how well a resume matches a given job description. The system computes a match score using TF-IDF vectorization and Cosine Similarity, enabling faster and data-driven resume screening.

This project demonstrates strong fundamentals in backend development, NLP, authentication, and clean UI design, making it suitable for Software Development Engineer (SDE) roles.

🚀 Key Features
🔐 Secure Authentication System

User registration and login using Flask-Login

Password hashing with Flask-Bcrypt

OTP-based email verification for enhanced security

🧠 NLP-Based Resume Matching

Converts resumes and job descriptions into numerical vectors using TF-IDF

Computes similarity using Cosine Similarity

Generates a clear match percentage score

📄 Multi-Format Resume Support

Accepts resumes in:

.pdf

.docx

.txt

Automatic text extraction and preprocessing

🕒 Match History Tracking

Stores previous resume analyses in SQLite

Displays match history sorted by date

Timestamps handled in Indian Standard Time (IST)

🎨 Modern & Responsive UI

Clean, professional interface

Fully responsive across devices

Dark Mode toggle for improved user experience

🛠 Tech Stack
Backend

Python

Flask

Flask-SQLAlchemy

Flask-Login

Flask-Bcrypt

Flask-WTF

Frontend

HTML5

CSS3

JavaScript

Database

SQLite

NLP & ML

Scikit-learn (TF-IDF, Cosine Similarity)

NLTK (text preprocessing)

Deployment

Gunicorn (production server)

📂 Project Architecture
resume-matcher-flask-app/
│
├── app/
│ ├── routes.py
│ ├── models.py
│ ├── forms.py
│ ├── utils/
│ │ └── nlp_matcher.py
│
├── templates/
├── static/
│ ├── css/
│ └── js/
│
├── instance/
│ └── database.db
│
├── run.py
├── requirements.txt
└── README.md

⚙️ Setup & Installation

1️⃣ Clone the Repository
git clone https://github.com/varunn912/resume-matcher-flask-app.git
cd resume-matcher-flask-app
2️⃣ Create Virtual Environment
python -m venv venv
source venv/bin/activate
3️⃣ Install Dependencies
pip install -r requirements.txt
4️⃣ Run the Application
python run.py
Access the app at:
http://127.0.0.1:5000

📈 Use Cases

Resume screening for recruiters

Self-evaluation before job applications

ATS-style matching experimentation

NLP learning and experimentation

🧠 What This Project Demonstrates (For Recruiters)

Strong understanding of Flask backend architecture

Practical application of NLP algorithms

Secure authentication and user session handling

Database modeling and query management

Clean UI/UX with dark mode

Production-ready deployment awareness

🔮 Future Enhancements

Skill-level weighting and keyword importance

Semantic matching using embeddings (BERT)

Admin dashboard for recruiters

Cloud deployment (AWS / Azure)

Resume parsing with named entity recognition

👨‍💻 Author
Kamshetty Varun
B.Tech CSE (AI & ML)
Aspiring Software Development Engineer (SDE)
