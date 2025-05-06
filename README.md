# MathEGE Parser 📚➗

Парсер заданий с сайта [prof.mathege.ru](https://prof.mathege.ru/) для подготовки к ЕГЭ по математике. Собирает задания в структурированном виде с возможностью добавления ответов.

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python)](https://www.python.org/)
[![BeautifulSoup](https://img.shields.io/badge/BeautifulSoup-4.x-green)](https://www.crummy.com/software/BeautifulSoup/)

---

## 🛠 Функционал
- **Парсинг заданий**: Автоматический сбор задач по всем темам ЕГЭ
- **Структурирование данных**:
  - Сохранение заданий в формате JSON
  - Загрузка изображений задач в папки по номерам
- **Система ответов**: Ручное добавление решений (заготовка функционала)
- **Статистика**: Отслеживание прогресса заполнения ответов

---

## ⚙️ Установка
1. Установите зависимости:
```bash
pip install requests beautifulsoup4
