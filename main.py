import streamlit as st
from langchain_helper import get_few_shot_db_chain

st.title("AtliQ T Shirts: Database Q&A 👕")

question = st.text_input("Question: ")

if question:
    chain = get_few_shot_db_chain()
    response = chain.run(question)

    st.header("Answer")
    st.write(response)

# if __name__ == "__main__":
#     chain = get_few_shot_db_chain()
#     print(chain.run("how many total t shirts are left in total in stock?"))