import streamlit as st
import pandas as pd
import numpy as np

def himan():
    st.write('##TOUCH APP')

    st.write('TOUCH APP')
    st.write('## TOUCH APP')

    data = pd.read_csv("imdb_top_1000.csv")
    st.write(data)

    data2 = pd.read_csv("operations_journal.json",delimiter=";")
    st.write(data2)

    data3 = pd.read_csv("netflix_titles_nov_2019.csv")
    st.write(data3)

    st.write("## His Cool Chart")
    st.link_button("go to page 2d",url="/dashboard")
    st.link_button("source video",url="https://www.youtube.com/watch?v=D0D4Pa22iG0&t=41s&ab_channel=pixegami")

    chart_data = pd.DataFrame(
        np.random.randn(20,3),
        columns=["a","b","c"]
    )
    st.bar_chart(chart_data)
    st.line_chart(chart_data)


if __name__ == '__main__':
    himan()