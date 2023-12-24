# PEP Parser

Этот проект представляет собой веб-парсер для сбора информации о PEP (Python Enhancement Proposals) с сайта [https://peps.python.org/](https://peps.python.org/).

## Как использовать

1. Установите зависимости:

    ```bash
    pip install -r requirements.txt
    ```

2. Запустите парсер:

    ```bash
    scrapy crawl pep
    ```

    Парсер соберет информацию о PEP и создаст два файла .csv в папке `results`: один со списком всех PEP, а другой с общей сводкой по статусам.

## Структура проекта

- `pep_parse/`: Исходный код проекта.
  - `spiders/`: Содержит ваши веб-пауки, включая `PepSpider`.
  - `items.py`: Определение структуры данных (PepParseItem).
  - `middlewares.py`: Определение middleware для обработки запросов (если необходимо).
  - `pipelines.py`: Определение пайплайна для обработки данных.
  - `settings.py`: Настройки Scrapy.
- `results/`: Папка, в которой сохраняются результаты парсинга.
- `scrapy.cfg`: Конфигурационный файл Scrapy.
- `README.md`: Этот файл с инструкциями.

## Результаты

- `results/pep_ДатаВремя.csv`: Список всех PEP с информацией о номере, названии и статусе.
- `results/status_summary_ДатаВремя.csv`: Сводка по статусам PEP.
