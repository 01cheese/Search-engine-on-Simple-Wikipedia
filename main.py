from flask import Flask, render_template, request, jsonify
from test import load_data_from_db, preprocess_data, find_similar_keywords
import async_http

nothing_found = [{'title': 'Basic English',
                  'first_sentence': 'BASIC English  is a controlled language used to explain complex thoughts.',
                  'url': 'https://simple.wikipedia.org/wiki/Basic_English'},
                 {'title': None, 'first_sentence': 'Failed to retrieve data from Wikipedia.',
                  'url': 'https://simple.wikipedia.org/wiki/Kramfors'},
                 {'title': 'Bullet Club',
                  'first_sentence': 'Bullet Club  is a professional wrestling stable that competes in the New Japan Pro-Wrestling .',
                  'url': 'https://simple.wikipedia.org/wiki/Bullet_Club_Gold'},
                 {'title': 'Seo Tai-ji', 'first_sentence': 'Seo Tai-ji  is a South Korean singer.',
                  'url': 'https://simple.wikipedia.org/wiki/Seo_Tai-ji'},
                 {'title': 'Odia language', 'first_sentence': None, 'url': 'https://simple.wikipedia.org/wiki/Oriya'},
                 {'title': 'Oriya film industry',
                  'first_sentence': 'Oriya Film Industry or Ollywood refers to the Bhubaneswar and Cuttack-based Oriya film industry in the Republic of India.',
                  'url': 'https://simple.wikipedia.org/wiki/Oriya_film_industry'},
                 {'title': None, 'first_sentence': 'Failed to retrieve data from Wikipedia.',
                  'url': 'https://simple.wikipedia.org/wiki/Gili_Air'},
                 {'title': None, 'first_sentence': 'Failed to retrieve data from Wikipedia.',
                  'url': 'https://simple.wikipedia.org/wiki/Gili_Meno'},
                 {'title': 'Quilmesaurus', 'first_sentence': None,
                  'url': 'https://simple.wikipedia.org/wiki/Quilmesaurus'}]

# Загрузка данных и предварительная обработка
df = load_data_from_db()
vectorizer, tfidf_matrix = preprocess_data(df)

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/ajax_search', methods=['POST'])
def ajax_search():
    query = request.form['query']
    similar_keywords, similar_urls = find_similar_keywords(query, vectorizer, tfidf_matrix, df)
    result = async_http.asyncio.run(async_http.main(similar_urls))

    cleaned_list = []
    titles_seen = set()

    for item in result:
        title = item['title']
        if title not in titles_seen:
            cleaned_list.append(item)
            titles_seen.add(title)

    if all(item in result for item in nothing_found):
        return jsonify(status='nothing found', query=query)
    else:
        response = [{'title': item['title'], 'url': item['url'], 'first_sentence': item['first_sentence']} for item in
                    cleaned_list]
        return jsonify(status='success', query=query, results=response)


if __name__ == '__main__':
    app.run(debug=True)
