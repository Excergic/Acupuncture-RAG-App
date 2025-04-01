import streamlit as st
from langchain_community.vectorstores import FAISS
from langchain_core.prompts import ChatPromptTemplate
from langchain_huggingface import HuggingFaceEmbeddings  
from langchain_groq import ChatGroq
from langchain_core.runnables import RunnablePassthrough

## use cache
@st.cache_resource(show_spinner=False)
def get_embeddings():
    return HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

@st.cache_resource(show_spinner=False)
def get_vectorStore():  # Fixed typo in function name
    return FAISS.load_local(
        "faiss_index",
        embeddings=get_embeddings(),
        allow_dangerous_deserialization=True
    )

@st.cache_resource(show_spinner=False)
def get_rag_chain():
    vectorstore = get_vectorStore()  # Fixed function name
    retriever = vectorstore.as_retriever(search_kwargs={"k": 5})

    prompt_template = """
        Analyze these clinical guidelines
        {context}

        Question: {question}

        Provide Structured Response:
        1. Diagnosis criteria
        2. Treatment protocol
        3. Acupuncture points
        4. Safety considerations
    """
    prompt = ChatPromptTemplate.from_template(prompt_template)
    llm = ChatGroq(
        temperature=0.3,
        model_name="llama3-70b-8192",
        api_key=st.secrets["GROQ_API_KEY"]
    )

    return (
        {"context": retriever, "question": RunnablePassthrough()}
        | prompt
        | llm
    )

## UI Component
st.title("🩺 Acupuncture Clinical Advisor")
st.caption("Evidence-based Treatment Recommendations")

## Main Execution Flow
query = st.text_input(
    "Enter clinical query:",
    placeholder="e.g. I am having headache, how to treat with acupuncture...."
)

if st.button("Generate Treatment Plan"):
    if not query:
        st.warning("Please enter a clinical question")
        st.stop()
    
    try:
        with st.spinner("Consulting medical literature..."):
            chain = get_rag_chain()
            response = chain.invoke(query)
            
            st.subheader("Clinical Recommendation")
            st.markdown(f"""
            <div style='
                padding: 1.5rem;
                border-radius: 0.8rem;
                background: #000000;
                color: #ffffff;
                box-shadow: 0 2px 4px rgba(255,255,255,0.1);
                margin: 1rem 0;
                font-family: monospace;
            '>
                {response.content}
            </div>
            """, unsafe_allow_html=True)
            
    except Exception as e:
        st.error(f"Clinical analysis failed: {str(e)}")
        st.exception(e)