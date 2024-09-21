from langchain.prompts import PromptTemplate
from langchain.llms import OpenAI
from dotenv import load_dotenv
from langchain.chains import LLMChain
import os

# Load environment variables
load_dotenv()

# Retrieve the OpenAI API key from .env
openai_api_key = os.getenv("OPENAI_API_KEY")

# Initialize the OpenAI LLM
llm = OpenAI(openai_api_key=openai_api_key)

# Define code explanation chain
code_explanation_template = """
You are an AI assistant. The user has provided the following code snippet:

{code}

Please do the following:
1. Explain what the code is doing.
2. Identify any errors or bugs.
3. Suggest a fix for each error.
4. For each fix, explain why the fix is needed, and provide a confidence score (between 0 and 100%) for how likely the fix will resolve the issue.
5. Provide a counterfactual explanation: What will happen if the fix is NOT applied?
"""
code_prompt = PromptTemplate(template=code_explanation_template, input_variables=["code"])
code_chain = LLMChain(llm=llm, prompt=code_prompt)

# Define error handling chain
error_handling_template = """
The user encountered the following error message:

{error_message}

Please do the following:
1. Explain what the error message means in plain language.
2. Suggest a fix for the error.
3. Explain why this fix will resolve the error.
4. Provide a confidence score (between 0 and 100%) for the suggested fix.
5. Provide a counterfactual explanation: What will happen if the fix is not applied?
"""
error_prompt = PromptTemplate(template=error_handling_template, input_variables=["error_message"])
error_chain = LLMChain(llm=llm, prompt=error_prompt)