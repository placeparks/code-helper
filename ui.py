import streamlit as st
import os
from openai import OpenAI

# Initialize the OpenAI client with your API key from environment variable
api_key = os.environ.get("OPENAI_API_KEY")
if not api_key:
    st.error("Please provide the OpenAI API key as an environment variable.")
    st.stop()

client = OpenAI(api_key=api_key)

def analyze_code(js_code):
    try:
        response = client.chat.completions.create(
            model="gpt-4-turbo-preview",
            messages=[
                {"role": "system", "content": "You are a helpful assistant, skilled in analyzing JavaScript code."},
                {"role": "user", "content": js_code}
            ]
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"An error occurred: {e}"

def generate_code(task_description):
    try:
        response = client.chat.completions.create(
            model="gpt-4-turbo-preview",
            messages=[
                {"role": "system", "content": "You are a helpful assistant capable of writing code for various tasks."},
                {"role": "user", "content": task_description}
            ]
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"An error occurred: {e}"

st.title('AI-Powered Code Assistant')

choice = st.radio("Choose an option:", ('Code Analysis', 'Code Generation'))

if choice == 'Code Analysis':
    user_code = st.text_area("Enter your JavaScript code here for analysis:")
    if st.button('Analyze Code'):
        result = analyze_code(user_code)
        st.text("Analysis Result:")
        st.write(result)

elif choice == 'Code Generation':
    task_description = st.text_area("Describe the task you want to generate code for:")
    if st.button('Generate Code'):
        result = generate_code(task_description)
        st.text("Generated Code:")
        st.code(result)

# Add custom CSS for footer
footer_style = """
position: fixed;
left: 0;
bottom: 0;
width: 100%;
text-align: center;
padding: 10px;
background-color: rgba(255, 255, 255, 0.5);  /* Semi-transparent light background */
color: #000;                                  /* Dark text for visibility */
border-top: 1px solid #000;                   /* Border to distinguish the footer */
z-index: 1000;                                /* Ensures it stays on top of other elements */
"""

# Footer
st.markdown(
    '<div style="{}">Developed by Mirac.eth<br>Contact: mirac.eth@ethereum.email</div>'.format(footer_style),
    unsafe_allow_html=True
)