import streamlit as st
import json

with open('blood_report_llm_output.json', encoding="utf-8", mode='r') as file:
    response = json.load(file)

print(response.content)



# from blood_report import blood_report


# with open('blood report.txt', 'r') as file:
#     blood_report = file.read()


# left, right = st.columns(2)

# with left:
#     with st.container(border=True):
#         st.header(blood_report)

# with right:
#     with st.container(border=True):
#         st.header("Summary + diet plan")
#         st.write(response)


# with st.container(border=True):
#         st.header(blood_report)

# with st.container(border=True):
#         st.header("Summary + diet plan")
#         st.write(response)
