import streamlit as st
from assistant import code_chain, error_chain

# Streamlit UI for Code Explanation and Debugging Assistant
st.title("Code Explanation and Debugging Assistant")

# Code Input Section
code = st.text_area("Enter your code here", height=300)
if st.button("Explain and Debug"):
    if code:
        # Run the LangChain process to get debugging suggestions and explanations
        response = code_chain.run(code)
        # Display the response which includes explanations and confidence scores
        st.write("### Code Explanation and Debugging Suggestions")
        st.write(response)
    else:
        st.write("Please enter some code to get an explanation.")

# Error Message Section
error_message = st.text_area("Enter the error message (if any)")
if st.button("Analyze Error"):
    if error_message:
        error_response = error_chain.run(error_message)
        st.write("### Error Explanation and Fix")
        st.write(error_response)
    else:
        st.write("Please enter an error message to analyze.")