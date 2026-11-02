from pathlib import Path

import joblib

from preprocesamiento import preprocesar_texto

RUTA_MODELO = Path(__file__).resolve().parent / "clasificador_emociones.joblib"

ETIQUETAS = {
    "anger": "Ira",
    "disgust": "Asco",
    "fear": "Miedo",
    "joy": "Alegría",
    "others": "Otras",
    "sadness": "Tristeza",
    "surprise": "Sorpresa",
}


def cargar_modelo():
    artefactos = joblib.load(RUTA_MODELO)
    return artefactos["modelo"], artefactos["vectorizador"]


def predecir_emocion(texto):
    if not isinstance(texto, str) or not texto.strip():
        raise ValueError("Debes ingresar un texto válido.")

    texto_limpio = preprocesar_texto(texto)
    modelo, vectorizador = cargar_modelo()

    texto_vectorizado = vectorizador.transform([texto_limpio])
    emocion = modelo.predict(texto_vectorizado)[0]

    probabilidades = modelo.predict_proba(texto_vectorizado)[0]

    resultados = {
        ETIQUETAS[clase]: float(probabilidad)
        for clase, probabilidad in zip(modelo.classes_, probabilidades)
    }

    return {
        "emocion": ETIQUETAS[emocion],
        "probabilidades": resultados,
    }
