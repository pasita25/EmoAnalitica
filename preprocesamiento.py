import re


def preprocesar_texto(texto):
    texto = texto.lower()
    texto = re.sub(r"!+", " exclamacion ", texto)
    texto = re.sub(r"\?+", " interrogacion ", texto)
    texto = re.sub(r"\d+", " num ", texto)
    texto = re.sub(r"[^a-záéíóúüñ\s]", " ", texto)
    texto = re.sub(r"\s+", " ", texto).strip()
    return texto
