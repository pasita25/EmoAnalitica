import streamlit as st

from predictor import predecir_emocion

st.set_page_config(
    page_title="EmoAnalítica",
    page_icon="😊",
    layout="centered",
)

st.title("😊 EmoAnalítica")
st.subheader("Clasificador de emociones en español")

st.write(
    "Escribe un comentario y descubre qué emoción "
    "identifica nuestro modelo de inteligencia artificial."
)

texto = st.text_area(
    "Escribe tu texto:",
    placeholder="Ejemplo: ¡Estoy muy feliz porque terminé mi proyecto!",
    height=140,
)

if st.button("Clasificar emoción", type="primary"):
    if not texto.strip():
        st.warning("Por favor, ingresa un texto antes de continuar.")
    else:
        with st.spinner("Analizando el texto..."):
            resultado = predecir_emocion(texto)

        emocion = resultado["emocion"]
        probabilidades = resultado["probabilidades"]

        st.success(f"Emoción predominante: {emocion}")

        st.write("### Probabilidades estimadas")

        probabilidades_ordenadas = dict(
            sorted(
                probabilidades.items(),
                key=lambda item: item[1],
                reverse=True,
            )
        )

        st.bar_chart(probabilidades_ordenadas)

        st.caption(
            "Las probabilidades corresponden a estimaciones "
            "del modelo y no representan un diagnóstico "
            "emocional de la persona."
        )
