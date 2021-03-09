# SF Module D10

### Для локального запуска:

1. Клонировать репозиторий и зайти в папку проекта
    ```
    git clone https://github.com/relax-man/SF-ModuleD10.git car_searcher 
    cd .\car_searcher
    ```

2. Установить модули из requirements.txt
    ```
    python -m venv env
    pip install -r .\requirements.txt
    ```

3. Добавить файл src\settings\local.py со своим SECRET_KEY
    ```
    from settings.base import *

    SECRET_KEY = << Your secret key >>
    DEBUG = True

    ALLOWED_HOSTS = ['localhost', '127.0.0.1']

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }

    CORS_ALLOW_ALL_ORIGINS = True
    ```

4. Провести миграции
    ```
    python src/manage.py migrate
    ```

5. Загрузить фикстуры
    ```
    python src/manage.py loaddata fixtures/cars.json
    ```

6. Запустить проект
    ```
    python src/manage.py runserver
    ```
