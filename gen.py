
import streamlit as st
from openai import OpenAI

f = open(r"C:\Users\Rahul\Desktop\Internship\Task 10\key.txt")
OPENAI_API_KEY = f.read()

st.title("Code Reviewer")
st.subheader("Finds bugs in code and write the corrected code")

client = OpenAI(api_key = OPENAI_API_KEY)

prompt = st.text_area("Enter a Code")

if st.button("Generate") == True:
    response = client.chat.completions.create(
      model="gpt-3.5-turbo-0125",
      messages=[
        {"role": "system", "content": "You are an Expert in code review. So, find bugs, errors and give the corrected code."},
        {"role": "user", "content": prompt}
      ]
    )
    st.write(response.choices[0].message.content)
