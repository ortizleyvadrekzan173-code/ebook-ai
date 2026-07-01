import streamlit as st
from fpdf import FPDF

st.title("📚 Drekzan AI Books")

prompt = st.text_area("Escribe la idea de tu eBook")

autor = "Drekzan Ortiz Leyva"
dedicatoria = "Con amor y gratitud dedico este libro a mi madre Maura Leyva García."

def generar_libro(prompt):
    contenido = f"""
TÍTULO: {prompt}

INTRODUCCIÓN
Este libro trata sobre: {prompt}

CAPÍTULO 1
Contenido sobre {prompt}...

CAPÍTULO 2
Continuación sobre {prompt}...

CONCLUSIÓN
Reflexión final sobre {prompt}.
"""
    return contenido

if st.button("Generar eBook"):
    texto = generar_libro(prompt)

    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    pdf.multi_cell(0, 10, f"Autor: {autor}\n\n")
    pdf.multi_cell(0, 10, f"Dedicatoria:\n{dedicatoria}\n\n")
    pdf.multi_cell(0, 10, texto)

    pdf.output("ebook.pdf")

    st.success("eBook generado")
    st.download_button("Descargar PDF", open("ebook.pdf", "rb"), "ebook.pdf")
