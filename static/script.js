const themeSwitcher = document.querySelector('.theme-switcher');
const body = document.body;
const themeKey = 'theme';
const loadingBar = document.querySelector('.loading-bar');

// Функция для сохранения текущей темы в локальное хранилище
const saveThemeToLocalStorage = (theme) => {
    localStorage.setItem(themeKey, theme);
};

// Функция для загрузки текущей темы из локального хранилища
const loadThemeFromLocalStorage = () => {
    const savedTheme = localStorage.getItem(themeKey);
    if (savedTheme) {
        body.classList.add(savedTheme);
    }
};

// Загрузка темы при загрузке страницы
loadThemeFromLocalStorage();

themeSwitcher.addEventListener('click', () => {
    // Переключение темы
    body.classList.toggle('dark-theme');

    // Сохранение текущей темы в локальное хранилище
    if (body.classList.contains('dark-theme')) {
        saveThemeToLocalStorage('dark-theme');
    } else {
        saveThemeToLocalStorage(''); // Если тема не темная, сохраняем пустую строку
    }
});

const showLoadingBar = () => {
    loadingBar.style.display = 'block';
    loadingBar.style.width = '0';
    setTimeout(() => {
        loadingBar.style.width = '100%';
    }, 10); // Небольшая задержка для анимации
};

const hideLoadingBar = () => {
    loadingBar.style.width = '0';
    setTimeout(() => {
        loadingBar.style.display = 'none';
    }, 500); // Соответствует времени transition
};

const handleSearch = async (event) => {
    event.preventDefault();
    showLoadingBar();

    const formData = new FormData(event.target);
    const response = await fetch('/ajax_search', {
        method: 'POST',
        body: formData
    });

    const result = await response.json();
    console.log(result);

    const searchResultsContainer = document.querySelector('.search-results');
    if (result.status === 'success') {
        let html = `<h2>Search Results for '${result.query}':</h2>`;
        result.results.forEach(item => {
            html += `
                <div class="search-result">
                    <a href="${item.url}" class="result-title">${item.title}</a>
                    <p class="result-snippet">${item.first_sentence}</p>
                    <hr>
                </div>
            `;
        });
        searchResultsContainer.innerHTML = html;
    } else {
        searchResultsContainer.innerHTML = `<h2>Nothing found for '${result.query}'.</h2>`;
    }
    hideLoadingBar();
};

document.addEventListener('DOMContentLoaded', function() {
    document.getElementById('search-form').addEventListener('submit', handleSearch);

    if (document.querySelector('.search-results')) {
        document.querySelector('.search-results').addEventListener('submit', handleSearch);
    }
});
