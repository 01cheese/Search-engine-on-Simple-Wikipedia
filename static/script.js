const themeSwitcher = document.querySelector('.theme-switcher');
const body = document.body;
const themeKey = 'theme';

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



document.addEventListener('DOMContentLoaded', function() {
    document.getElementById('search-form').addEventListener('submit', function(event) {
        event.preventDefault(); // Предотвращаем отправку формы по умолчанию
        // Здесь можно добавить дополнительную логику перед отправкой формы, если нужно
        this.submit(); // Отправляем форму
    });
});
