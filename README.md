# Ollama-Jang

**Feed URL Data to AI for Better Response**

This project utilizes LangChain to load documents from the web and PDF files, convert them into embeddings, and store them in Chroma. The project also performs question-answer retrieval based on these embeddings to provide better responses from the AI.

*Inspired by the work of [@MervinPraison](https://github.com/MervinPraison)*


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

## Installation

1. Clone the repository :
   ```sh
   git clone https://github.com/dofbi/ollama-jang
   cd ollama-jang

2. Create a virtual environment :

3. Install the dependencies :

4. Copy the .env.example file to .env and modify the variables as needed :

5. Run the project :

## Configuration


## Usage
The project loads data from the provided URLs, splits the data into chunks, converts them to embeddings, and stores them in Chroma. It then retrieves information based on these embeddings to provide enhanced AI responses.

###Before Retrieval-Augmented Generation (RAG)###
The project answers questions using the AI model without retrieving context from the embeddings.

###After Retrieval-Augmented Generation (RAG)###
The project answers questions using the AI model with context retrieved from the embeddings.