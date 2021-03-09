## Base Django-Heroku project

**TODO:**

- Generate secret_key
    ```
    from django.core.management.utils import get_random_secret_key
    print(get_random_secret_key())
    ```

- Create virtual env
    ```
    python -m venv env
    pip install -r requirements.txt
    ```

- Remove comments in .gitignore
    ```
    # VsCode
    .vscode/
    
    # Local settings
    src/settings/local.py
    ```