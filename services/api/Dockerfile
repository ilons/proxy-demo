FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7

COPY demo /app/demo

CMD ["uvicorn", "demo.main:app", "--host", "0.0.0.0", "--port", "80", "--reload"]
