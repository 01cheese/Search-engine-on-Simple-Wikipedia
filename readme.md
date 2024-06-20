# Wikipedia Search Application

![image](https://github.com/01cheese/Search-engine-on-Simple-Wikipedia/assets/115219323/cf175c0f-4264-4d43-90f9-17a98b90a8fd)
![image](https://github.com/01cheese/Search-engine-on-Simple-Wikipedia/assets/115219323/9ba44e38-a923-4a02-84fb-69aa01fff9c3)



This project is a Flask-based web application designed to perform keyword-based searches on a dataset derived from the Simple English Wikipedia. The application processes search queries, identifies relevant Wikipedia articles, and retrieves summarized information for display.

## Features

- Keyword-based search using TF-IDF vectorization and cosine similarity
- Asynchronous HTTP requests for fetching Wikipedia data
- Simple and user-friendly interface with theme switching
- Error handling and default responses for failed data retrieval

## Setup

### Prerequisites

Ensure you have the following installed:
- Python 3.7 or higher
- pip (Python package installer)

### Installation

1. Create a virtual environment and activate it:
    ```sh
    python -m venv venv
    source venv/bin/activate   # On Windows use `venv\Scripts\activate`
    ```

2. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

3. Set up the SQLite database:
    - Ensure your `links.db` is located in the `static` directory with the appropriate schema.

### Running the Application

1. Start the Flask application:
    ```sh
    python main.py
    ```

2. Open your web browser and navigate to `http://127.0.0.1:5000`.

## Project Structure

- `main.py`: The main Flask application file that handles routing and search functionality.
- `async_http.py`: Contains asynchronous functions for fetching Wikipedia data.
- `test.py`: Utility functions for loading and preprocessing data, as well as finding similar keywords.
- `templates/`: Contains HTML templates (`index.html` and `result.html`).
- `static/`: Contains static files like CSS and JavaScript.

## Libraries Used

- Flask~=3.0.3: Web framework for building the application.
- pandas~=2.2.2: Data manipulation and analysis library.
- scikit-learn~=1.5.0: Machine learning library for vectorization and similarity computation.
- aiohttp~=3.9.5: Asynchronous HTTP client for fetching Wikipedia data.
- bs4~=0.0.2: BeautifulSoup library for parsing HTML.
- beautifulsoup4~=4.12.3: HTML parser for extracting information.

## How It Works

1. **Data Loading and Preprocessing**:
    - `test.py` contains functions to load data from the SQLite database and preprocess it using TF-IDF vectorization.

2. **Search Functionality**:
    - `main.py` handles the search functionality by receiving the query, finding similar keywords using cosine similarity, and retrieving corresponding URLs.
    - Asynchronous requests fetch Wikipedia data, and results are cleaned and presented to the user.

3. **Asynchronous Data Retrieval**:
    - `async_http.py` performs asynchronous HTTP requests to Wikipedia, parses the HTML to extract titles and first sentences, and returns the data for display.

4. **Frontend**:
    - HTML templates render the search form and results.
    - `script.js` includes theme switching functionality and form submission handling.

## Usage

1. **Search**:
    - Enter a keyword in the search bar and submit the form.
    - The application retrieves and displays relevant Wikipedia articles.

2. **Theme Switching**:
    - Click the theme switcher button to toggle between light and dark themes.
    - The selected theme is saved in local storage and applied on subsequent visits.

## Error Handling

- If no data is retrieved or an error occurs, the application displays a default message with pre-defined responses.

## Contributing

Feel free to fork the repository, create a branch, and submit pull requests. Contributions are welcome!


## Acknowledgements

- Flask, Pandas, Scikit-learn, Aiohttp, and BeautifulSoup communities for their excellent libraries and documentation.
- My parents who gave me the idea for the project)
---

### Example

Here's an example of a search result:

- **Query**: `iphone 4`
- **Results**:
  - **Title**: `iphone 4`
  - **First Sentence**: The iPhone 4 is a smartphone made by Apple.
  - **URL**: https://simple.wikipedia.org/wiki/IPhone_4

---

### Contact
[zelenko009@gmail.com](mailto:zelenko009@gmail.com)

This README provides a comprehensive guide to setting up and using the Wikipedia Search Application. Enjoy exploring and expanding the project!
