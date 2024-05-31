from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
import sqlite3
import pandas as pd


def load_data_from_db():
    conn = sqlite3.connect('static/links.db')
    df = pd.read_sql_query("SELECT tfidf_keywords, url FROM links", conn)
    return df


def preprocess_data(df):
    vectorizer = TfidfVectorizer(stop_words='english')
    tfidf_matrix = vectorizer.fit_transform(df['tfidf_keywords'].dropna())
    return vectorizer, tfidf_matrix


def find_similar_keywords(query, vectorizer, tfidf_matrix, df):
    query_vector = vectorizer.transform([query])
    cosine_similarities = linear_kernel(query_vector, tfidf_matrix).flatten()
    similar_indices = cosine_similarities.argsort()[:-10:-1]
    similar_keywords = df.loc[df['tfidf_keywords'].dropna().index[similar_indices], 'tfidf_keywords'].tolist()
    similar_urls = df.loc[df['tfidf_keywords'].dropna().index[similar_indices], 'url'].tolist()
    return similar_keywords, similar_urls

