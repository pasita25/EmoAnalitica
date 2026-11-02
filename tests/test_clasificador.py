import pytest

from predictor import predecir_emocion
from preprocesamiento import preprocesar_texto


def test_preprocesamiento():
    resultado = preprocesar_texto("¡Hola! Tengo 25 años.")
    assert resultado == "hola exclamacion tengo num años"


def test_texto_vacio():
    with pytest.raises(ValueError):
        predecir_emocion("   ")


def test_prediccion():
    resultado = predecir_emocion("Estoy muy feliz porque terminé mi proyecto")

    assert resultado["emocion"] in {
        "Ira",
        "Asco",
        "Miedo",
        "Alegría",
        "Otras",
        "Tristeza",
        "Sorpresa",
    }

    assert len(resultado["probabilidades"]) == 7

    suma = sum(resultado["probabilidades"].values())
    assert suma == pytest.approx(1.0)
