# Dynamic Google Sheets Assistant

This project is a **Dynamic Google Sheets Assistant** built using Python, Gradio, and LangChain with Google Gemini API integration. It allows users to interact with Google Sheets in a web interface to perform tasks like viewing column names, inserting data, summarizing sheet data, and asking questions based on the data.


## Features

- **View Column Names & Data Types:** Dynamically displays all column names along with their data types (Numeric or String).  
- **Insert Data with Validation:** Allows users to insert a row into the sheet, validating input according to the detected data type.  
- **Summarize Sheet Data:** Generates a clear summary of the sheet data using an LLM (Google Gemini).  
- **Ask Questions:** Users can ask questions related to the data, and the system provides intelligent answers using LLM.  
- **Interactive Web Interface:** Gradio-based interface with tabs for easy navigation.


## Libraries Used

- `os` – Environment variable handling.  
- `dotenv` – Load API keys from `.env` file.  
- `gradio` – Interactive web interface.  
- `pandas` – Data manipulation and analysis.  
- `gspread` – Google Sheets interaction.  
- `oauth2client` – Google API authentication.  
- `langchain_google_genai` – Access Google Gemini LLM for AI tasks.  

## How to Use

1. Enter the Google Sheet URL in the input box.  
2. Navigate between tabs:  
   - **Insert Data:** View columns and insert validated row data.  
   - **Summarize Sheet:** Get a summary of the sheet content.  
   - **Ask a Question:** Ask any question based on the sheet data.  


## Architecture & Details

### High-Level Architecture

**Components:**

- **Frontend (Gradio UI):** Provides the user interface for interacting with Google Sheets, including tabs for inserting data, summarizing sheet content, and asking questions.  
- **Backend (Python + LangChain + Google APIs):** Handles data validation, communicates with Google Sheets, and performs AI-based summarization and question answering using LangChain with Google Gemini.  
- **Google Sheets:** Stores all spreadsheet data, column information, and user entries.  
- **LangChain + Google Gemini:** Serves as the LLM responsible for generating summaries and answering questions based on the sheet data.  


### Low-Level Details

**Modules and Functions:**

1. **Google Sheets Connector:**  
   - `connect_sheet(sheet_url)` → Connects to a Google Sheet using gspread and Google credentials.  

2. **Data Handling:**  
   - `get_columns(sheet_url)` → Retrieves column names and detects data types (Numeric/String).  
   - `insert_data(sheet_url, row)` → Inserts a row into the sheet, validating values against detected column types.  

3. **AI Module (LangChain + Google Gemini):**  
   - `summarize_sheet(sheet_url)` → Generates an AI-based summary of spreadsheet content.  
   - `ask_question(sheet_url, question)` → Provides AI-generated answers to user queries based on the sheet data.  

4. **Frontend (Gradio UI):**  
   - **Tabs:** Insert Data, Summarize Sheet, Ask a Question.  
   - **Input:** Google Sheet URL.  
   - **Output:** Column information, insertion results, AI summaries, and answers.
     
## Real-Time Use Cases

- **Business Analytics:** Quickly summarize sales, inventory, or customer data in Google Sheets.  
- **Data Validation:** Ensure correct data types while inserting new entries.  
- **AI-Powered Insights:** Generate summaries and answers from spreadsheet data without manual calculations.
