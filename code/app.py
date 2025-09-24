import streamlit as st
import pandas as pd
import os
from dotenv import load_dotenv
from pandasai.llm.openai import OpenAI
from pandasai import PandasAI
from pandasai.llm.grokcloud import GrokCloud  
import streamlit as st
import pandas as pd
import os
from dotenv import load_dotenv
from pandasai.llm.grokcloud import GrokCloud  # <<< CHANGE HERE
from pandasai import PandasAI

load_dotenv()
grokcloud_api_key = os.getenv('GROKCLOUD_API_KEY')  

# function to query a csv file using pandasai and GrokCloud
def chat_with_csv(df, prompt):
    llm = GrokCloud(api_token=grokcloud_api_key)  
    pandas_ai = PandasAI(llm)
    result = pandas_ai.run(df, prompt=prompt)
    print(result)
    return result

# from pandasai.smart_dataframe import SmartDataframe

# # function to query a csv file using pandasai and GrokCloud
# def chat_with_csv(df, prompt):
#     llm = GrokCloud(api_token=grokcloud_api_key)  # Initialize LLM
#     smart_df = SmartDataframe(df)  # Use SmartDataframe to wrap the dataframe
#     result = smart_df.ask(prompt)  # Use the `ask` method to get the response from the model
#     print(result)
#     return result


st.set_page_config(layout='wide')
st.title("ChatCSV powered by LLM (GrokCloud)")

input_csv = st.file_uploader("Upload the CSV", type=['csv'])

if input_csv is not None:
    col1, col2 = st.columns([1, 1])

    with col1:
        st.info("CSV Uploaded Successfully")
        data = pd.read_csv(input_csv)
        st.dataframe(data)

    with col2:
        st.info("Chat with CSV")   
        input_text = st.text_area("Enter your query")
        if input_text:
            if st.button("Chat with CSV"):
                st.info("Your Query: " + input_text)
                result = chat_with_csv(data, input_text)
                st.success(result)


# openai_api_key = os.getenv('OPENAI_API_KEY')

# #function for pandas ai to query a csv file

# def chat_with_csv(df,prompt):
#     llm = OpenAI()
#     pandas_ai = PandasAI(llm)
#     result = pandas_ai.run(df,prompt=prompt)
#     print(result)
#     return result

# st.set_page_config(layout = 'wide')
# st.title("ChatCSV powered by LLM")

# input_csv = st.file_uploader("upload the csv", type=['csv'])

# if input_csv is not None:
#     col1, col2 = st.columns([1,1])

#     with col1:
#         st.info("CSV Uploaded sucessfully")
#         data = pd.read_csv(input_csv)
#         st.dataframe(data)

#     with col2:
#         st.info("chat with csv")   
#         input_text = st.text_area("enter your query")
#         if input_text is not None:
#             if st.button("chat with csv"):
#                 st.info("your query: "+ input_text)
#                 result = chat_with_csv(data, input_text)
#                 st.success(result)


#how to run === streamlit run app.py

