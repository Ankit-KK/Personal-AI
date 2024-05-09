import streamlit as st
from langchain.prompts import PromptTemplate
from langchain.llms import CTransformers

## Function to get response from llama 2 model
def getllamaresponse(prompt_template):
    # LLama2 model
    llm = CTransformers(model='models/llama-2-7b-chat.ggmlv3.q8_0.bin',
                        model_type='llama',
                        config={"max_new_tokens": 300, "temperature": 0.01})
    
    # Pass the prompt string to LLama 2 model
    response = llm(prompt_template)
    return response

st.set_page_config(page_title='Personal AI',
                   page_icon='🖥️',
                   layout='centered',
                   initial_sidebar_state='collapsed')

st.header("Personal AI 🖥️")

prompt_template = st.text_input("Enter the Prompt Template")

submit = st.button("Generate")

# Final Response
if submit and prompt_template:
    st.write(getllamaresponse(prompt_template))
elif submit:
    st.warning("Please provide a prompt template.")