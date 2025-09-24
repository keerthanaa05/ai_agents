
# import streamlit as st
# import pandas as pd
# import os
# from dotenv import load_dotenv
# from pandasai import SmartDataframe
# from langchain_groq.chat_models import ChatGroq  # make sure this is installed

# # Load environment variables
# load_dotenv()
# grokcloud_api_key = os.getenv('GROKCLOUD_API_KEY')

# def chat_with_csv(dataframe, prompt):
#     # No need to read_csv here, because you already passed the DataFrame
#     chat_model = ChatGroq(model_name='llama3-70b-8192', api_key=grokcloud_api_key)

    
#     # smart_df = SmartDataframe(dataframe, config={'llm': chat_model})
#     smart_df = SmartDataframe(dataframe, config={'llm': chat_model})

#     result = smart_df.chat(prompt)
    
#     print(result)
#     return result

# # Streamlit UI
# st.set_page_config(layout='wide')
# st.title("ChatCSV powered by LLM (GrokCloud)")

# input_csv = st.file_uploader("Upload the CSV", type=['csv'])

# if input_csv is not None:
#     col1, col2 = st.columns([1, 1])

#     with col1:
#         st.info("CSV Uploaded Successfully")
#         data = pd.read_csv(input_csv)
#         st.dataframe(data)

#     with col2:
#         st.info("Chat with CSV")   
#         input_text = st.text_area("Enter your query")
#         if input_text:
#             if st.button("Chat with CSV"):
#                 st.info("Your Query: " + input_text)
#                 result = chat_with_csv(data, input_text)  # <=== pass DataFrame (data), not input_csv
#                 st.success(result)

import streamlit as st
import pandas as pd
import os
from dotenv import load_dotenv
from pandasai import SmartDataframe
from langchain_groq.chat_models import ChatGroq  # make sure this is installed

# Load environment variables
load_dotenv()
grokcloud_api_key = os.getenv('GROKCLOUD_API_KEY')

def chat_with_csv(dataframe, prompt):
    # No need to read_csv here, because you already passed the DataFrame
    chat_model = ChatGroq(model_name='llama3-8b-8192', api_key=grokcloud_api_key)

    # Initialize SmartDataframe with conversational capabilities
    smart_df = SmartDataframe(dataframe, config={'llm': chat_model})

    result = smart_df.chat(prompt)
    
    print("===============", result)
    return result

# Streamlit UI
st.set_page_config(layout='wide')
st.title("Chat with CSV powered by LLM")

input_file = st.file_uploader("Upload the CSV", type=['csv', 'xlsx'])

if input_file is not None:
    col1, col2 = st.columns([1, 1])

    with col1:
        st.info("File Uploaded Successfully")
        # Read the file based on the file extension
        if input_file.name.endswith('.csv'):
            data = pd.read_csv(input_file)
        elif input_file.name.endswith('.xlsx'):
            data = pd.read_excel(input_file)
        
        st.dataframe(data)

    with col2:
        st.info("Chat with your File!")
        input_text = st.text_area("Enter your query")

        if input_text:
            if st.button("Submit Query"):
                st.info("Your Query: " + input_text)
                result = chat_with_csv(data, input_text)
                st.success(result)  
