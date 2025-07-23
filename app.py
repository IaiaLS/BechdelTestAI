import streamlit as st
import matplotlib.pyplot as plt

from analysis.bechdel_test import bechdel_test
from analysis.gender_analysis import analyze_text

st.title(" BechdelTestAI - Teste de Bechdel")
input_text = st.text_area("Cole aqui o texto (ex: roteiro ou transcrição)")

if st.button("Analisar"):
    if input_text.strip():
        resultTestBechdel = bechdel_test(input_text)
        st.write("**Resultado:**", dict(resultTestBechdel))

        result = analyze_text(input_text)

        if result["characters_by_gender"]:
            st.subheader("Distribuição de personagens por gênero")
            fig1, ax1 = plt.subplots()
            ax1.pie(result["characters_by_gender"].values(),
                    labels=result["characters_by_gender"].keys(), autopct='%1.1f%%')
            st.pyplot(fig1)
        else:
            st.info("Nenhum personagem com gênero identificado.")

        if result["speech_by_gender"]:
            st.subheader("Distribuição de falas por gênero")
            fig2, ax2 = plt.subplots()
            ax2.pie(result["speech_by_gender"].values(),
                    labels=result["speech_by_gender"].keys(), autopct='%1.1f%%')
            st.pyplot(fig2)
        else:
            st.info("Nenhuma fala identificada.")
    else:
        st.warning("Digite algum texto para analisar.")