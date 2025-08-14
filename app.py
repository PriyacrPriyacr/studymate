import streamlit as st
import os
from pdf_processor import extract_text_from_pdf, chunk_text
from vector_store import create_faiss_index, search
from llm_answer import generate_answer

st.title("📚 StudyMate – AI Academic Assistant")

uploaded_file = st.file_uploader("Upload your PDF", type="pdf")

if uploaded_file:
    file_path = os.path.join("uploads", uploaded_file.name)
    with open(file_path, "wb") as f:
        f.write(uploaded_file.read())
    st.success("PDF uploaded successfully!")

    text = extract_text_from_pdf(file_path)
    chunks = chunk_text(text)
    index, _ = create_faiss_index(chunks)

    question = st.text_input("Ask a question about the uploaded material:")

    if question:
        relevant_chunks = search(question, index, chunks)
        context = " ".join(relevant_chunks)
        answer = generate_answer(context, question)
        st.markdown("### ✅ Answer:")
        st.write(answer)
