import streamlit as st
from ctransformers import AutoModelForCausalLM
from fpdf import FPDF

# Function to load the Llama model using CTransformers
@st.cache_resource
def load_model():
    model_path = 'path_of_LLM_model'

    # Load the Llama model correctly
    llm = AutoModelForCausalLM.from_pretrained(
        model_path_or_repo_id=model_path,
        model_type='llama',
        max_new_tokens=600, 
        temperature=0.01,
    )
    return llm

def generate_blog(topic, words, style, llm):
    prompt = f"Write a blog for a {style} job profile on the topic '{topic}' within {words} words."
    response = llm(prompt)
    return response

# Function to create PDF from text
def create_pdf(blog_text):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.set_font("Arial", size=12)
    lines = blog_text.split('\n')
    for line in lines:
        pdf.multi_cell(0, 10, line)
    return pdf

# Streamlit UI
st.set_page_config(page_title="📝 Blog Generator", layout="centered")
st.title("📝 Generate Blogs")

topic = st.text_input("Enter the Blog Topic", placeholder="e.g. Blog on Cyber Security")
col1, col2 = st.columns(2)

with col1:
    words = st.text_input("No. of Words", placeholder="e.g. 300")
with col2:
    style = st.selectbox("Writing for:", ("Researchers", "Data Scientist", "Common People"))

# Load model
llm = load_model()

# Button to generate blog
generate = st.button("🚀 Generate Blog")

if generate:
    if not topic or not words:
        st.warning("⚠️ Please fill all fields!")
    else:
        with st.spinner('Generating blog... Please wait!'):
            blog = generate_blog(topic, words, style, llm)
        # Save blog into session state so it doesn't get lost
        st.session_state.blog = blog
        st.success('✅ Blog generated successfully!')

        st.markdown("### ✍️ Generated Blog:")
        st.write(st.session_state.blog)

        # Download as PDF
        pdf = create_pdf(st.session_state.blog)
        pdf_output = pdf.output(dest='S').encode('latin1')
        st.download_button(
            label="📄 Download as PDF",
            data=pdf_output,
            file_name="generated_blog.pdf",
            mime='application/pdf'
        )

        # Download as Text
        st.download_button(
            label="📝 Download as Text File",
            data=st.session_state.blog,
            file_name="generated_blog.txt",
            mime="text/plain"
        )
