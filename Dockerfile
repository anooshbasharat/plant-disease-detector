# The image only contains the app and the trained model, not the dataset (see .dockerignore).
FROM python:3.11-slim

# uv installs the exact package versions from uv.lock
COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin/uv
WORKDIR /app

COPY pyproject.toml uv.lock ./
RUN uv sync --frozen --no-dev --no-install-project

COPY app.py model.joblib ./
COPY .streamlit/ ./.streamlit/

EXPOSE 8501
CMD ["uv", "run", "--no-sync", "streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
