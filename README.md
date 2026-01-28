# AI Resume Matcher

### Flask · Python · NLP · SQLite

A **full-stack web application** that leverages **Natural Language Processing (NLP)** to intelligently evaluate how well a resume matches a given job description. The system computes a **match score** using **TF-IDF vectorization** and **Cosine Similarity**, enabling faster, accurate, and data-driven resume screening.

This project highlights strong foundations in **backend engineering, NLP, secure authentication, database design, and UI/UX**, making it highly relevant for **Software Development Engineer (SDE)** roles.

---

## 🚀 Key Features

### 🔐 Secure Authentication System

* User registration and login using **Flask-Login**
* Password hashing with **Flask-Bcrypt**
* **OTP-based email verification** for enhanced security

### 🧠 NLP-Based Resume Matching

* Converts resumes and job descriptions into numerical vectors using **TF-IDF**
* Calculates similarity using **Cosine Similarity**
* Generates a clear and interpretable **match percentage score**

### 📄 Multi-Format Resume Support

* Supports resume uploads in:

  * `.pdf`
  * `.docx`
  * `.txt`
* Automatic text extraction and preprocessing pipeline

### 🕒 Match History Tracking

* Stores all previous analyses in **SQLite**
* Displays match history sorted by date
* Timestamps handled in **Indian Standard Time (IST)**

### 🎨 Modern & Responsive UI

* Clean and professional user interface
* Fully responsive across desktop and mobile devices
* **Dark Mode toggle** for improved user comfort

---

## 🛠 Tech Stack

### Backend

* Python
* Flask
* Flask-SQLAlchemy
* Flask-Login
* Flask-Bcrypt
* Flask-WTF

### Frontend

* HTML5
* CSS3
* JavaScript

### Database

* SQLite

### NLP & Machine Learning

* Scikit-learn (TF-IDF, Cosine Similarity)
* NLTK (text preprocessing)

### Deployment

* Gunicorn (production-ready WSGI server)

---

## 📂 Project Architecture

```
resume-matcher-flask-app/
│
├── app/
│   ├── routes.py
│   ├── models.py
│   ├── forms.py
│   ├── utils/
│   │   └── nlp_matcher.py
│
├── templates/
├── static/
│   ├── css/
│   └── js/
│
├── instance/
│   └── database.db
│
├── run.py
├── requirements.txt
└── README.md
```

---

## ⚙️ Setup & Installation

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/varunn912/resume-matcher-flask-app.git
cd resume-matcher-flask-app
```

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate   # On Windows: venv\\Scripts\\activate
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Run the Application

```bash
python run.py
```

Access the application at:

```
http://127.0.0.1:5000
```

---

## 📈 Use Cases

* Resume screening for recruiters and hiring teams
* Self-evaluation before job applications
* ATS-style resume–JD matching experimentation
* Hands-on learning project for NLP and Flask

---

## 🧠 What This Project Demonstrates (For Recruiters)

* Strong understanding of **Flask-based backend architecture**
* Practical application of **NLP algorithms** in real-world use cases
* Secure authentication and session management
* Relational database modeling and query handling
* Clean UI/UX design with accessibility considerations
* Awareness of **production-ready deployment practices**

---

## 🔮 Future Enhancements

* Skill-level weighting and keyword prioritization
* Semantic matching using transformer-based embeddings (BERT)
* Recruiter/admin dashboard
* Cloud deployment (AWS / Azure)
* Advanced resume parsing with Named Entity Recognition (NER)

---

## 👨‍💻 Author

**Kamshetty Varun**
B.Tech – Computer Science & Engineering (AI & ML)
Aspiring Software Development Engineer
