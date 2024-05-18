import streamlit as st
import time
import streamlit as st
from transformers import pipeline

st.title('Zadanie streamlit SUML 🖥️')

st.header('Przetwarzanie języka naturalnego oraz prosty tłumacz angielsko-niemiecki')

st.write('Funkcja tłumaczenie korzysta z modelu google-t5/t5-base (https://huggingface.co/google-t5/t5-base)')

st.write('Aby przetłumaczyć tekst z angielskiego na niemiecki wybierz z listy odpowiednią opcję')

st.write('Zadanie przygotowane na zaliczenie z zajęć SUML na PJATK.')

st.image('pjatk_logo.png', caption="Polsko-Japońska Akademia Technik Komputerowych")



#def typewriter(input: str, speed: int):
#                tokens = input.split()
#                container = st.empty()
#                for index in range(len(tokens) + 1):
#                    curr_full_text = " ".join(tokens[:index])
#                    container.markdown(curr_full_text)
#                    time.sleep(1 / speed)

option = st.selectbox(
    "Opcje",
    [
        "Wydźwięk emocjonalny tekstu (eng)",
        "Tłumacz z angielskiego na język niemiecki",
    ],
)

if option == "Wydźwięk emocjonalny tekstu (eng)":
    input = st.text_area(label="Wpisz tekst")
    if input:
        classifier = pipeline("sentiment-analysis")
        answer = classifier(input)
        st.write(answer)

elif option =="Tłumacz z angielskiego na język niemiecki":
    input = st.text_area(label="Wpisz tekst po angielsku. Maksymalna długość tłumaczonego tekstu to 2000 znaków.")
    if len(input) > 2000:
        st.error('Tłumaczony tekst nie moze być dłuszy niz 2000 znaków.')
    elif input:
        with st.spinner(text='Tłumaczenie moze chwilę potrwać. \n Proszę o cierpliwość..'):

            model = pipeline("translation_en_to_de", model="t5-base")
            input_translated = model(input, max_length=2000)
            output = input_translated[0]['translation_text']


        if output == input:
            st.error('Nie udało się przetłumaczyć tekstu. Upewnij się, ze jest on w języku angielskim.')
        else:
            st.success('Tłumaczenie gotowe!')
            st.write("Tłumaczenie:")
            st.write(output)
            #st.balloons()

st.write('by Marcin Milczarzewicz s21954')
