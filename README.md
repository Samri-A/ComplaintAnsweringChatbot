# Complaint Answering Chatbot

This project is a Complaint Answering Chatbot that processes, analyzes, and answers consumer complaints using advanced text processing, data augmentation, and vector-based retrieval techniques. The system leverages Python scripts for data handling and a Streamlit app for interactive user engagement.

---

## Project Structure

```
.gitignore
README.md
requirements.txt
.github/
  workflows/
    ci.yml
.vscode/
  settings.json
data/
  processed/
    complaints_processed.csv
  raw/
    complaints.csv
  vector_store/
    chroma.sqlite3
    033eb154-a33b-4c81-97ee-5c40c1b98cc5/
env/
notebook/
  10EDA.ipynb
  text_processing.ipynb
src/
  __init__.py
  .env
  app.py
  Augment_Generation.py
  embed_in_vectorstore.py
  preprocess_document.py
  __pycache__/
tests/
  unitest.py
```

---

## Main Components

- **src/**: Source code for the main application and data processing scripts.
  - [`src/app.py`](src/app.py): Main Streamlit app entry point.
  - [`src/Augment_Generation.py`](src/Augment_Generation.py): Data augmentation and generation utilities.
  - [`src/embed_in_vectorstore.py`](src/embed_in_vectorstore.py): Embeds processed documents into a vector store (ChromaDB).
  - [`src/preprocess_document.py`](src/preprocess_document.py): Preprocessing scripts for complaint documents.

- **data/**: Data storage directory.
  - `raw/complaints.csv`: Raw complaint data.
  - `processed/complaints_processed.csv`: Preprocessed complaint data.
  - `vector_store/`: Vector database (ChromaDB) for storing embeddings.

- **notebook/**: Jupyter notebooks for exploratory data analysis and text processing.
  - [`notebook/10EDA.ipynb`](notebook/10EDA.ipynb): Exploratory Data Analysis.
  - [`notebook/text_processing.ipynb`](notebook/text_processing.ipynb): Text preprocessing and feature engineering.

- **tests/**: Unit and integration tests ([`tests/unitest.py`](tests/unitest.py)).

- **.github/**: GitHub Actions workflows for CI/CD.

- **requirements.txt**: Python dependencies.

---

## Setup

1. **Clone the repository**
   ```sh
   git clone <repo-url>
   cd ComplaintAnsweringChatbot
   ```

2. **Create and activate a virtual environment**
   ```sh
   python -m venv env
   source env/bin/activate  # On Windows: env\Scripts\activate
   ```

3. **Install dependencies**
   ```sh
   pip install -r requirements.txt
   ```

4. **Prepare data**
   - Place raw complaint data in `data/raw/complaints.csv`.
   - Run preprocessing scripts as needed.

---

## Usage

- **Data Preprocessing:**  
  Use [`src/preprocess_document.py`](src/preprocess_document.py) to clean and preprocess complaint data.

- **Data Augmentation:**  
  Use [`src/Augment_Generation.py`](src/Augment_Generation.py) for augmenting and generating additional data.

- **Embedding and Vector Store:**  
  Use [`src/embed_in_vectorstore.py`](src/embed_in_vectorstore.py) to embed documents and store them in ChromaDB.

- **Streamlit Application:**  
  Run the main app with:
  ```sh
  streamlit run src/app.py
  ```
  This will launch the interactive chatbot interface.

- **Notebooks:**  
  Explore and analyze data using the notebooks in the [`notebook/`](notebook/) directory.

---

## Screenshot

_ a screenshot of the Streamlit app _
![image](https://github.com/user-attachments/assets/e711e884-3bb6-48c6-bf67-eec22b208bb9)

---

## Testing

Run tests using unitestin the [`tests/`](tests/) directory.

---

## Contributing

1. Fork the repository.
2. Create a new branch.
3. Make your changes and add tests.
4. Submit a pull request.

---
