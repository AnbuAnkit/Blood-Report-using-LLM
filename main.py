import streamlit as st
# from blood_report import blood_report


with open('blood report.txt', 'r') as file:
    blood_report = file.read()

# left, right = st.columns(2)

# with left:
#     with st.container(border=True):
#         st.header(blood_report)

# with right:
#     with st.container(border=True):
#         st.header("Summary")
#         st.write(blood_report)


from importnb import Notebook
with Notebook():
    import response

print(response)

# st.title("Blood Report Summarizer")