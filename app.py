import streamlit as st
from pdf import chatbot

def main():
    st.set_page_config(page_title="Writer <> Langchain Workflows", page_icon=":rocket:")
    st.title('Langchain PDF Demo :rocket:')
    st.subheader("How can I help?")
    chatbot()

if __name__ == '__main__':
    main()
