# AI Resume Matcher

![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white)

A Flask-based web application that uses Natural Language Processing (NLP) to calculate a match score between a resume and a job description. This tool helps users quickly assess the relevance of a resume for a specific job opening.

## Features

-   **Secure User Authentication**: Full registration and login system with OTP verification.
-   **NLP-Powered Matching**: Utilizes TF-IDF and Cosine Similarity to score resume-job description relevance.
-   **Multi-Format Support**: Accepts resumes in `.pdf`, `.docx`, and `.txt` formats.
-   **Match History**: Users can view a history of their past analyses, sorted by date with Indian Standard Time (IST) timestamps.
-   **Responsive UI**: A clean, modern, and professional user interface.
-   **Dark Mode**: A toggleable dark theme for user comfort.

## Tech Stack

-   **Backend**: Flask, Flask-SQLAlchemy, Flask-Login, Flask-Bcrypt, Flask-WTF
-   **Frontend**: HTML, CSS, JavaScript
-   **Database**: SQLite
-   **NLP**: Scikit-learn, NLTK
-   **Deployment**: Gunicorn (for production)

## Setup and Installation

Follow these steps to get the project running on your local machine.

**1. Clone the repository:**
```bash
git clone [https://github.com/YourUsername/resume-matcher-flask-app.git](https://github.com/YourUsername/resume-matcher-flask-app.git)
cd resume-matcher-flask-app
