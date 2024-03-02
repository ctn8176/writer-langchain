import streamlit as st
from pdf import chatbot
from blog import blog_creation

def main():
    st.set_page_config(page_title="Writer <> Langchain Workflows", page_icon=":rocket:")
    st.title('Writer <> Langchain Workflows :rocket:')
    st.subheader("How can I help?")

    option = st.selectbox("Select an option:", ["Create Blog Post", "Chat with PDF Chatbot"])

    if option == "Create Blog Post":
        blog_creation()
    elif option == "Chat with PDF Chatbot":
        chatbot()

if __name__ == '__main__':
    main()
