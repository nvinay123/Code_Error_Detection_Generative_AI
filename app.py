import streamlit as st
from assistant import code_chain, error_chain

# Set page configuration and title
st.set_page_config(
    page_title="Code Explanation and Debugging Assistant",
    page_icon="💻",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Header
st.markdown(
    """
    <style>
    .main-title {
        font-size: 3rem;
        font-weight: bold;
        text-align: center;
        color: #4B7BEC;
    }
    .sub-title {
        font-size: 1.5rem;
        font-weight: 600;
        text-align: center;
        color: #333;
    }
    .section {
        border-radius: 10px;
        background-color: #F4F4F8;
        padding: 1.5rem;
        margin-bottom: 2rem;
        box-shadow: 0px 4px 12px rgba(0, 0, 0, 0.1);
    }
    .button-style {
        background-color: #4B7BEC;
        color: white;
        padding: 0.75rem 1.25rem;
        border-radius: 8px;
        border: none;
        font-size: 1rem;
        font-weight: bold;
        cursor: pointer;
        margin-top: 1rem;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown("<div class='main-title'>💻 Code Explanation and Debugging Assistant</div>", unsafe_allow_html=True)
st.markdown("<div class='sub-title'>Empowering developers with insights into their code and errors</div>", unsafe_allow_html=True)

# Layout for Code and Error Sections
code_col, error_col = st.columns(2)

# Code Explanation Section
with code_col:
    st.markdown("## 🧑‍💻 Code Explanation")
    st.markdown("<div class='section'>", unsafe_allow_html=True)
    code = st.text_area("Enter your code here", height=200, key="code_input")
    
    # Fancy Button
    explain_debug_button = st.markdown(
        '<button class="button-style">Explain and Debug</button>',
        unsafe_allow_html=True
    )
    
    if st.button("Explain and Debug", key="explain_debug"):
        if code:
            with st.spinner("Analyzing the code and generating insights..."):
                # Run the LangChain process to get debugging suggestions and explanations
                response = code_chain.run(code)
                st.success("Code Explanation and Debugging Completed")
                st.markdown("<hr>", unsafe_allow_html=True)
                st.markdown("### Explanation and Suggestions:")
                st.write(response)
        else:
            st.warning("Please enter some code to get an explanation.")
    
    st.markdown("</div>", unsafe_allow_html=True)

# Error Message Section
with error_col:
    st.markdown("## 🛠️ Error Handling")
    st.markdown("<div class='section'>", unsafe_allow_html=True)
    error_message = st.text_area("Enter the error message (if any)", height=200, key="error_input")

    # Fancy Button
    analyze_error_button = st.markdown(
        '<button class="button-style">Analyze Error</button>',
        unsafe_allow_html=True
    )

    if st.button("Analyze Error", key="analyze_error"):
        if error_message:
            with st.spinner("Analyzing the error message..."):
                error_response = error_chain.run(error_message)
                st.success("Error Analysis Completed")
                st.markdown("<hr>", unsafe_allow_html=True)
                st.markdown("### Error Explanation and Fix:")
                st.write(error_response)
        else:
            st.warning("Please enter an error message to analyze.")
    
    st.markdown("</div>", unsafe_allow_html=True)

# Footer or Sidebar Information
st.sidebar.markdown("### About the Assistant")
st.sidebar.markdown(
    """
    This application uses advanced AI techniques to analyze code snippets and error messages.
    It provides detailed explanations and suggestions for bug fixing, all while delivering 
    an interactive user experience powered by LangChain and OpenAI.
    """
)
st.sidebar.markdown("### Features")
st.sidebar.markdown(
    """
    - 🔍 **Explain Code:** Understand what your code is doing, even in complex scenarios.
    - 🛠️ **Debug Issues:** Identify bugs and get suggestions for fixes.
    - 💬 **Counterfactual Analysis:** Learn what might happen if a suggested fix is not applied.
    - 🎯 **Confidence Scores:** Receive confidence scores for each fix suggestion.
    """
)
