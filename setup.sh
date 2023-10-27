python3 -m venv venv
source venv/bin/activate

pip install poetry

poetry config virtualenvs.create false
poetry install --no-root

pre-commit install

cp .env.example .env
