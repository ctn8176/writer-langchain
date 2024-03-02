import streamlit as st
from dotenv import load_dotenv
import json
from langchain.chains import LLMChain, SequentialChain
from langchain.prompts import PromptTemplate
# from langchain_community.llms import Writer
from langchain.llms import OpenAI
import os

os.environ['OPENAI_API_KEY'] = st.secrets['OPENAI_API_KEY']
os.environ['WRITER_API_KEY'] = st.secrets['WRITER_API_KEY']
os.environ['WRITER_ORG_ID'] = st.secrets['WRITER_ORG_ID']

# App framework

def blog_creation():
    load_dotenv()
    prompt = st.text_input("What is your blog post about?")

    headline_template = PromptTemplate(input_variables=['blog topic'],
                              template='write out a title for the {blog topic}. give three examples.')

    script_template = PromptTemplate(input_variables=['headline'],
                              template='write out a blog post for this headline HEADLINE: {headline}')

    # llm
    # Writer_llm = Writer()
    OpenAI_llm = OpenAI(temperature=0.7)

    headline_chain = LLMChain(llm=OpenAI_llm, prompt=headline_template, verbose='true', output_key='headline')
    script_chain = LLMChain(llm=OpenAI_llm, prompt=script_template, verbose='true', output_key='script')
    sequential_chain = SequentialChain(chains=[headline_chain, script_chain],
                                       input_variables=['blog topic'], output_variables=['headline', 'script'], verbose=True)

    if prompt:
        response = sequential_chain({'blog topic': prompt})

        # Parse and clean the JSON response for headline
        headline_text = json.loads(response['headline'])['choices'][0]['text'].strip()

        st.write(headline_text)
        st.write(response['script'])

# Run the Streamlit app
if __name__ == "__blog_creation__":
    blog_creation()
