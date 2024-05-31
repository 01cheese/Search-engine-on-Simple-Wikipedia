from flask import Flask, render_template, request
from test import load_data_from_db, preprocess_data,find_similar_keywords
import async_http


nothing_found = [{'title': None, 'first_sentence': 'Failed to retrieve data from Wikipedia.', 'url': 'https://simple.wikipedia.org/wiki/Kramfors'}, {'title': '2020 Belizean general election', 'first_sentence': 'The 2020 Belizean general election elected the members of the House of Representatives in the National Assembly.', 'url': 'https://simple.wikipedia.org/wiki/2020_Belizean_general_election'}, {'title': 'United Democratic Party (Belize)', 'first_sentence': 'The United Democratic Party  is one of the two major political parties in Belize.', 'url': 'https://simple.wikipedia.org/wiki/United_Democratic_Party_(Belize)'}, {'title': 'Manuel Esquivel', 'first_sentence': 'Sir Manuel Amadeo Esquivel, KCMG, PC  is a Belizean politician.', 'url': 'https://simple.wikipedia.org/wiki/Manuel_Esquivel'}]


# Загрузка данных и предварительная обработка
df = load_data_from_db()
vectorizer, tfidf_matrix = preprocess_data(df)


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/search', methods=['POST'])
def search():
    query = request.form['query']
    if query == '':
        return render_template('index.html')
    else:
        similar_keywords, similar_urls = find_similar_keywords(query, vectorizer, tfidf_matrix, df)

        result = async_http.asyncio.run(async_http.main(similar_urls))

        cleaned_list = []
        titles_seen = set()

        for item in result:
            title = item['title']
            if title not in titles_seen:
                cleaned_list.append(item)
                titles_seen.add(title)

        result = cleaned_list
        if all(item in result for item in nothing_found):
            return render_template('result.html', query=query, zipped_data=0)
        else:
            title_page = []
            first_sentence = []
            url_page = []
            for page_data in result:
                if page_data['title'] == None:
                    page_data['title'] = page_data['url']
                if page_data['first_sentence'] == None:
                    page_data['first_sentence'] = ''

                url_page.append(page_data['url'])
                title_page.append(page_data['title'])
                first_sentence.append(page_data['first_sentence'])
            zipped_data = zip(title_page, url_page, first_sentence)
            return render_template('result.html', query=query, zipped_data=zipped_data)


if __name__ == '__main__':
    app.run(debug=True)
