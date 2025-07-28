import os
import pandas as pd
from dotenv import load_dotenv
from langchain_experimental.agents import create_pandas_dataframe_agent
from langchain_google_genai import ChatGoogleGenerativeAI

# Load API key from .env file
load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# Validate API key
if not GOOGLE_API_KEY:
    raise EnvironmentError("❌ GOOGLE_API_KEY not found in .env file.")

# Initialize Gemini model
llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",  # "gemini-2.5-flash" does not exist yet; "1.5-flash" is latest supported by LangChain
    temperature=0.2,
    google_api_key=GOOGLE_API_KEY
)

# Main function to handle question with pandas agent
def get_agent_response(df: pd.DataFrame, question: str) -> str:
    try:
        # Create agent for pandas dataframe
        agent = create_pandas_dataframe_agent(
            llm=llm,
            df=df,
            verbose=False,
            allow_dangerous_code=True,
            handle_parsing_errors=True
        )

        # Run the agent with the user question
        response = agent.run(question)
        return response

    except Exception as e:
        return f"❌ Error: {str(e)}"