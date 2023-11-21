# Exel to SQL

Программа для конвертации exel в sql. СОГЛАСНО ТЕСТОВОМУ ЗАДАНИЮ

В качестве базы данныйх используется SQLite. Есть дополнительная валидация данных через Pydantic.
Работа с базой данных выполняется через SQLAlchemy.

### Установка через pip

Создание виртуального окружения

```bash
python -m venv venv
```

Установка зависимостей

```bash
pip install -r requirements.txt
```

### Установка через poetry

Создание виртуального окружения

```bash
poetry shell
```

Установка зависимостей

```bash
poetry install
```

### Cоздание базы данных и выполнение миграций

```bash
alembic upgrade head
```

### Запуск

```bash
python main.py
```
