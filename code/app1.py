import streamlit as st
import pandas as pd
import os
from dotenv import load_dotenv
from pandasai import SmartDataframe 
from langchain_groq.chat_models import ChatGroq # Just import this

# Load environment variables
load_dotenv()
grokcloud_api_key = os.getenv('GROKCLOUD_API_KEY')


def chat_with_csv(df, prompt):
    data = pd.read_csv(df)
    data.head()
    llm = ChatGroq(model_name = 'llama-3.3-70b-versatile',api_key = grokcloud_api_key)
    df = SmartDataframe(data,config = {'llm':llm})

    result = df.chat(prompt)
    # smart_df = SmartDataframe(df, config={"api_key": grokcloud_api_key, "llm": "llama-3.3-70b-versatile"})
    # from pandasai import LLM

    # llm_instance = LLM(model="llama-3.3-70b-versatile")
    # config = {"api_key": grokcloud_api_key, "llm": llm_instance}


    # result = smart_df.chat(prompt)
    print(result)
    return result

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

# ChatCSV Application

# import streamlit as st
# import pandas as pd
# import os
# from dotenv import load_dotenv
# from pandasai import SmartDataframe
# from pandasai import LLM

# # Load environment variables
# load_dotenv()
# grokcloud_api_key = os.getenv('GROKCLOUD_API_KEY')

# # Function to interact with the CSV using LLM
# def chat_with_csv(df, prompt):
#     # Initialize SmartDataframe with the dataframe and LLM configuration
#     smart_df = SmartDataframe(df, config={"api_key": grokcloud_api_key, "llm": "llama-3.3-70b-versatile"})
    
#     # Create an instance of LLM
#     llm_instance = LLM(model="llama-3.3-70b-versatile")
    
#     # Use SmartDataframe to interact with the CSV based on the prompt
#     result = smart_df.chat(prompt)
#     return result

# # Streamlit setup
# st.set_page_config(layout='wide')
# st.title("ChatCSV powered by LLM (GrokCloud)")

# # File uploader for CSV file
# input_csv = st.file_uploader("Upload the CSV", type=['csv'])

# if input_csv is not None:
#     col1, col2 = st.columns([1, 1])

#     # Display the uploaded CSV in the left column
#     with col1:
#         st.info("CSV Uploaded Successfully")
#         data = pd.read_csv(input_csv)
#         st.dataframe(data)

#     # User input and interaction with the CSV in the right column
#     with col2:
#         st.info("Chat with CSV")   
#         input_text = st.text_area("Enter your query")
        
#         if input_text:
#             if st.button("Chat with CSV"):
#                 st.info("Your Query: " + input_text)
#                 result = chat_with_csv(data, input_text)
#                 st.success(result)








# import streamlit as st
# import pandas as pd
# import os
# from dotenv import load_dotenv
# from pandasai import SmartDataframe, LLM

# # Load environment variables
# load_dotenv()
# grokcloud_api_key = os.getenv('GROKCLOUD_API_KEY')

# def chat_with_csv(df, prompt):
#     llm_instance = LLM(model="deepseek-r1-distill-llama-70b", api_key=grokcloud_api_key)
#     config = {"llm": llm_instance}
#     smart_df = SmartDataframe(df, config=config)
#     result = smart_df.chat(prompt)
#     print(result)
#     return result

# st.set_page_config(layout='wide')
# st.title("ChatCSV powered by LLM (GrokCloud)")

# input_csv = st.file_uploader("Upload the CSV", type=['csv'])

# if input_csv is not None:
#     col1, col2 = st.columns([1,1])

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
#                 result = chat_with_csv(data, input_text)
#                 st.success(result)


# import streamlit as st
# import pandas as pd
# import os
# from dotenv import load_dotenv
# from pandasai import SmartDataframe
# from pandasai.llms import GrokCloud  # Assuming there's an import for GrokCloud

# # Load environment variables
# load_dotenv()
# grokcloud_api_key = os.getenv('GROKCLOUD_API_KEY')  # Ensure this is set correctly

# def chat_with_csv(df, prompt):
#     # Initialize GrokCloud LLM with the API key
#     llm = GrokCloud(api_token=grokcloud_api_key)
    
#     # Pass the GrokCloud LLM instance to SmartDataframe
#     smart_df = SmartDataframe(df, config={"llm": llm})
    
#     # Query the dataframe with the prompt
#     result = smart_df.chat(prompt)
#     return result

# st.set_page_config(layout='wide')
# st.title("ChatCSV powered by LLM (GrokCloud)")

# # File upload
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
#                 result = chat_with_csv(data, input_text)
#                 st.success(result)
