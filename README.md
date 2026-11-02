
# EmoAnalítica

Aplicación web para clasificar emociones en textos en español
utilizando procesamiento del lenguaje natural y aprendizaje automático.

## Funcionalidad

El usuario escribe un texto y recibe:

- Emoción predominante.
- Probabilidades estimadas para siete categorías emocionales.

Las categorías son: alegría, tristeza, ira, miedo, asco, sorpresa y otras.

## Modelo
- Algoritmo: Regresión logística.
- Representación: Bag of Words (unigramas).
- Dataset original: EmoEvent.
- Biblioteca: scikit-learn 1.6.1.

El modelo y el vectorizador se encuentran en
`clasificador_emociones.joblib`.

## Requisitos

- Python 3.11
- uv
- Docker (opcional para ejecución local)

## Instalación

Clonar el repositorio y ejecutar:

```powershell
uv sync
```

## Ejecutar la aplicación
```powershell
uv run streamlit run app.py
```

Abrir http://localhost:8501

## Ejecutar pruebas
```powershell
uv run python -m pytest -v
uv run ruff check .
uv run ruff format --check .
```

## Ejecutar con Docker
Construir la imagen:

```powershell
docker build -t emoanalitica:1.0 .
```

Ejecutar el contenedor:
```powershell
docker run --rm -p 8502:8501 emoanalitica:1.0
```

Abrir http://localhost:8502


## Publicación temporal
Con Docker funcionando, ejecutar:

```powershell
cloudflared tunnel --url http://localhost:8502
```

Cloudflare generará una dirección pública temporal.

## Seguridad y limitaciones
La aplicación no requiere claves API.
No se deben ingresar datos personales o confidenciales.
Las probabilidades son estimaciones del modelo y no
constituyen diagnósticos emocionales.
El rendimiento puede variar según el tipo de texto.
