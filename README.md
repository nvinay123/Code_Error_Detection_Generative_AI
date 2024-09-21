You can run the project by following the following steps:
Step-by-Step Instructions to Run the Project
1. Install Required Dependencies
Make sure you have all necessary dependencies installed. The essential libraries include:
To install all the dependencies:
pip install -r requirements.txt
If you don't have a requirements.txt file, install the dependencies directly:
pip install streamlit langchain openai python-dotenv
2. Create the .env File
Ensure that you have a .env file in the root directory of your project. This file will store your OpenAI API key securely.
Example .env file:
OPENAI_API_KEY=your-openai-api-key
Make sure you replace your-openai-api-key with the actual key provided by OpenAI.
3. Directory Structure
Your project directory should look like this:
├── .env                # Contains OpenAI API key
├── app.py              # Streamlit app (runs the interface)
├── assistant.py        # LangChain and OpenAI logic
├── requirements.txt    # List of dependencies
└── README.md           # (Optional) Project documentation
4. Run the Streamlit Application
To run the Streamlit application, navigate to the root directory of your project in the terminal or command prompt and run:
streamlit run app.py
This command will launch your application. By default, Streamlit opens the app in a new tab in your web browser (usually at http://localhost:8501/).
5. Test the Application
Once the application is running:
Code Explanation: Paste or type some Python code in the "Enter your code here" section and click Explain and Debug. You should see explanations of what the code is doing, any errors, the suggested fixes, and explanations for why the fixes are necessary.
Error Analysis: If you have an error message, paste it in the "Enter the error message" section and click Analyze Error. The assistant should provide an explanation of the error, the suggested fix, and a confidence score along with a counterfactual scenario.
7. Troubleshooting
Missing API Key: If you encounter errors related to the API key not being found, double-check your .env file and ensure the python-dotenv package is installed and properly loading the environment variables.
Dependency Errors: If any dependencies fail, try manually installing them one by one.
With these steps, your Explainable AI Debugging Assistant should be up and running, providing debugging steps along with explanations for why it suggests certain fixes.
