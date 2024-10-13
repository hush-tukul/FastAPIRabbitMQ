# Makefile for FastAPI + Uvicorn project

.PHONY: install
install:
	@echo "Installing dependencies..."
	pip install -r requirements.txt

.PHONY: run
run:
	@echo "Running FastAPI with Uvicorn..."
	uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload

.PHONY: run-prod
run-prod:
	@echo "Running FastAPI in production mode..."
	uvicorn app.main:app --host 0.0.0.0 --port 8000 --workers 4

.PHONY: clean
clean:
	@echo "Cleaning up..."
	find . -name "*.pyc" -exec rm -f {} \;
	find . -name "__pycache__" -exec rm -rf {} \;

.PHONY: test
test:
	@echo "Running tests..."
	pytest
