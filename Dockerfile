
FROM python:3.11-slim

# Copiar uv para instalar dependencias reproducibles
COPY --from=ghcr.io/astral-sh/uv:0.13.6 /uv /uvx /bin/

# Carpeta de trabajo dentro del contenedor
WORKDIR /app

# Utilizar Python del contenedor y evitar descargas innecesarias
ENV UV_PYTHON_DOWNLOADS=never
ENV UV_LINK_MODE=copy
ENV PATH="/app/.venv/bin:$PATH"

# Instalar solamente las dependencias de ejecución
COPY pyproject.toml uv.lock .python-version ./
RUN uv sync --locked --no-dev --no-install-project

# Copiar únicamente los archivos necesarios
COPY app.py predictor.py preprocesamiento.py ./
COPY clasificador_emociones.joblib ./

# Puerto de Streamlit
EXPOSE 8501

# Iniciar la aplicación
CMD ["streamlit", "run", "app.py", \
     "--server.address=0.0.0.0", \
     "--server.port=8501", \
     "--server.headless=true"]
