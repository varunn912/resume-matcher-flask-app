import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
import docx
import PyPDF2

def extract_text_from_file(file_stream, file_extension):
    text = ""
    try:
        if file_extension == "pdf":
            pdf_reader = PyPDF2.PdfReader(file_stream)
            for page in pdf_reader.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text
        elif file_extension == "docx":
            doc = docx.Document(file_stream)
            for para in doc.paragraphs:
                text += para.text + "\n"
        elif file_extension == "txt":
            text = file_stream.read().decode('utf-8')
    except Exception as e:
        print(f"Error reading {file_extension.upper()} file: {e}")
        return ""
    return text

def preprocess_text(text):
    text = text.lower()
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    tokens = word_tokenize(text)
    stop_words = set(stopwords.words('english'))
    lemmatizer = WordNetLemmatizer()
    cleaned_tokens = [lemmatizer.lemmatize(word) for word in tokens if word not in stop_words and len(word) > 1]
    return " ".join(cleaned_tokens)

def calculate_match_score(resume_text, job_desc_text):
    processed_resume = preprocess_text(resume_text)
    processed_job_desc = preprocess_text(job_desc_text)
    
    if not processed_resume or not processed_job_desc:
        return 0.0

    corpus = [processed_resume, processed_job_desc]
    vectorizer = TfidfVectorizer()
    
    try:
        tfidf_matrix = vectorizer.fit_transform(corpus)
        cosine_sim = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])
        score = cosine_sim[0][0] * 100
        return round(score, 2)
    except ValueError:
        return 0.0