# 🩺 Acupuncture Clinical Advisor - Retrieval-Augmented Generation (RAG)

## 📌 Overview
The **Acupuncture Clinical Advisor** is a Retrieval-Augmented Generation (RAG) application that provides evidence-based acupuncture treatment recommendations. It utilizes **LangChain**, **FAISS**, and **Groq's Llama3-70B** model to analyze clinical guidelines and generate structured treatment plans.

## 🏗️ Project Structure
```
├── main.py                 # Streamlit-based user interface
├── rag_notebook.ipynb      # Notebook for processing PDFs and creating FAISS index
├── requirements.txt        # Dependencies for the project
├── faiss_index/            # FAISS vector store directory
├── Acupuncture_PDFs/       # Directory containing clinical guideline PDFs
└── README.md               # Project documentation
```

## 🚀 Features
- **Clinical Query Processing**: Users can input acupuncture-related clinical questions.
- **PDF-based Knowledge Base**: Extracts information from acupuncture guidelines.
- **FAISS Vector Store**: Efficient retrieval of relevant knowledge.
- **LLM-powered Analysis**: Uses Groq's Llama3-70B to generate professional responses.
- **Streamlit UI**: Simple and interactive interface for clinical consultation.

## 📥 Installation
### 1️⃣ Clone the Repository
```bash
git clone https://github.com/yourusername/acupuncture-rag.git
cd acupuncture-rag
```

### 2️⃣ Create a Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

## 🔑 API Key Configuration
Create a **.env** file in the root directory and add your **GROQ API key**:
```ini
GROQ_API_KEY=your_api_key_here
```

## 📚 Preparing the Knowledge Base
### 1️⃣ Process Clinical Guidelines (PDFs)
Place your acupuncture guideline PDFs inside the `Acupuncture_PDFs/` directory.
Then, run the **rag_notebook.ipynb** script to create a FAISS vector store:
```bash
python rag_notebook.py
```

### 2️⃣ Start the Streamlit Application
```bash
streamlit run main.py
```

## 📌 Usage
1. Open the web UI.
2. Enter a clinical question related to acupuncture.
3. Click **"Generate Treatment Plan"**.
4. View structured recommendations including:
   - Diagnosis criteria
   - Treatment protocol
   - Acupuncture points
   - Safety considerations

## 🛠️ Technologies Used
- **Python**
- **Streamlit** (UI)
- **LangChain** (RAG pipeline)
- **FAISS** (Vector database)
- **Groq Llama3-70B** (LLM for response generation)
- **HuggingFace Sentence-Transformers** (Embeddings)
- **PyPDFLoader** (PDF processing)

## 📝 License
MIT License. Feel free to use and improve this project!

## 🤝 Contributing
If you want to contribute, fork this repository and submit a pull request. Feedback and improvements are always welcome!

## 📧 Contact
For any inquiries, reach out via:
- **X (Twitter)**: [@dhaivat00](https://x.com/dhaivat00)
- **Instagram**: [dhaivatjambudia](https://www.instagram.com/dhaivatjambudia/)
- **LinkedIn**: [Dhaivat Jambudia](https://www.linkedin.com/in/dhaivat-jambudia/)
- Or open an issue on GitHub.

