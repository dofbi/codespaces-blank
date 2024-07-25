# Ollama-Jang

**Feed URL Data to AI for Better Response**

This project utilizes LangChain to load documents from the web and PDF files, convert them into embeddings, and store them in Chroma. The project also performs question-answer retrieval based on these embeddings to provide better responses from the AI.

_Inspired by the work of [@MervinPraison](https://github.com/MervinPraison)_

## Project Structure

- `main.py`: The main script that runs the code.
- `utils/data_loader.py`: Contains functions for loading documents.
- `configs/config.py`: Contains configurations and parameters.
- `embeddings/embedder.py`: Contains logic for creating embeddings from documents.
- `retrievers/retriever.py`: Contains logic for retrieving information from embeddings.
- `prompts/prompt_handler.py`: Handles the creation and execution of prompts.
- `requirements.txt`: List of necessary Python dependencies.
- `.env`: Contains environment variables for customization.
- `urls.txt`: Contains the URLs of documents to be loaded.

## Prerequisites

- Ollama installed locally. [Download Ollama](https://ollama.com/download?ref=hackernoon.com)
- Two models: `phi3` and `nomic-embed-text`.

  ```sh
  ollama pull phi3
  ollama pull nomic-embed-text

  ```

## Installation

1. **Clone the repository**:

   ```sh
   git clone https://github.com/dofbi/ollama-jang
   cd ollama-jang
   ```

2. **Create a virtual environment**:

   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the dependencies**:

   ```sh
   pip install -r requirements.txt
   ```

4. **Copy the .env.example file to .env and modify the variables as needed**:

   ```sh
   cp .env.example .env
   # Edit .env to set up your environment variables
   ```

5. **Run the project**:
   ```sh
   python main.py
   ```

## Configuration

All configurations and parameters are stored in `configs/config.py`. You can adjust settings such as API keys, model parameters, and storage paths.

## Usage

The project loads data from the provided URLs, splits the data into chunks, converts them to embeddings, and stores them in Chroma. It then retrieves information based on these embeddings to provide enhanced AI responses.

### Before Retrieval-Augmented Generation (RAG)

The project answers questions using the AI model without retrieving context from the embeddings.

### After Retrieval-Augmented Generation (RAG)

The project answers questions using the AI model with context retrieved from the embeddings, providing more accurate and relevant responses.

## Additional Notes

- Ensure Ollama is installed locally and properly configured.
- Make sure the `phi3` and `nomic-embed-text` models are downloaded and accessible for the program to run successfully.
