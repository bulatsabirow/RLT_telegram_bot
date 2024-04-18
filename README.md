## Требования ##
1. [Python >= 3.10](https://www.python.org/downloads/)
2. [Poetry](https://pypi.org/project/poetry/)

## Локальный запуск проекта ##
1. Вход в виртуальное окружение:
    `
    poetry shell 
    `
2. Установка зависимостей:
    `
    poetry install
    `
3. Поднятие MongoDB с помощью Docker:
    `
    docker compose -f 'docker-compose.dev.yml' up -d
    `
4. Выгрузка тестовых данных в базу данных (выполняется только при первом запуске):
    `
    docker exec -ti mongodb mongorestore -d test -c sample_collection /data/sample_collection.bson
    `
5. Инициализация линтера:
    `
    pre-commit install
    `
6. Задать переменную окружения `$TOKEN` - токен Telegram бота
7. Запуск бота:
    `
    python main.py
    `