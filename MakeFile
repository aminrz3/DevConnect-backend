run:
	poetry run uvicorn app.main:app --reload

lint:
	poetry run ruff check .
	poetry run black --check .
	poetry run isort --check-only .
	poetry run mypy app

format:
	poetry run black .
	poetry run isort .

test:
	poetry run pytest -v --disable-warnings

docker-build:
	docker build -t devconnect .

docker-run:
	docker run -p 8000:8000 devconnect
