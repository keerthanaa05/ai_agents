import streamlit as st
import pandas as pd
import os
from dotenv import load_dotenv
from pandasai import SmartDataframe
from langchain_groq.chat_models import ChatGroq  
import importlib.util


load_dotenv()
grokcloud_api_key = os.getenv('GROKCLOUD_API_KEY')


def import_remove_none():
    module_name = "remove_none"
    module_spec = importlib.util.find_spec(module_name)
    if module_spec is None:
        raise ImportError(f"Module {module_name} not found.")
    remove_none = importlib.import_module(module_name)
    return remove_none

def chat_with_csv(dataframe, prompt):
    chat_model = ChatGroq(model_name='llama3-8b-8192', api_key=grokcloud_api_key)


    smart_df = SmartDataframe(dataframe, config={'llm': chat_model})

    result = smart_df.chat(prompt)
    return result


st.set_page_config(layout='wide')
st.title("AI Agent: File Analyzer and Suggestion Generator")

input_file = st.file_uploader("Upload the CSV or Excel file", type=['csv', 'xlsx'])

if input_file is not None:
    col1, col2 = st.columns([1, 1])

    with col1:
        st.info("File Uploaded Successfully")

        if input_file.name.endswith('.csv'):
            data = pd.read_csv(input_file)
        elif input_file.name.endswith('.xlsx'):
            data = pd.read_excel(input_file)
        
        st.write("Data Preview:")
        st.dataframe(data)

    with col2:
        st.info("AI Agent: Suggestions based on your file")
        

        suggestions = []


        missing_data = data.isnull().sum().sum()
        if missing_data > 0:
            suggestions.append(f"The dataset contains {missing_data} missing values. Consider removing them.")

        if suggestions:
            print(suggestions)
            st.success("AI Suggestions:")
            for suggestion in suggestions:
                st.write(f"- {suggestion}")
        

        input_text = st.text_area("Ask the AI Agent for more insights or tasks")

        if input_text:
            if ("remove null" or "yes" or "remove" or "ok")  in input_text.lower():
                st.info("Removing rows with null values...")
                try:
                    # Import remove_none.py dynamically
                    remove_none = import_remove_none()
                    cleaned_data = remove_none.remove_null_values(data)


                    output_filename = "cleaned_data.csv"
                    cleaned_data.to_csv(output_filename, index=False)


                    with open(output_filename, "rb") as file:
                        st.download_button(
                            label="Download Cleaned File",
                            data=file,
                            file_name=output_filename,
                            mime="text/csv"
                        )

                except Exception as e:
                    st.error(f"An error occurred: {e}")
