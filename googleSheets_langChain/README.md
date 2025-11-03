# Google Sheets Assistant

This project is a **Google Sheets Assistant** built using Python, Gradio, and LangChain with Google Gemini API integration. It allows users to interact with Google Sheets in a web interface to perform tasks like viewing column names, inserting data, summarizing sheet data, and asking questions based on the data.

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
## Flow Diagram

<img width="900" height="900" alt="flow" src="https://github.com/user-attachments/assets/067cbc5d-2a52-4907-9b62-38132c3da028" />

## Architecture & Details

### High-Level Architecture

**Components:**

- **Frontend (Gradio UI):** Provides the user interface for interacting with Google Sheets, including tabs for inserting data, summarizing sheet content, and asking questions.  
- **Backend (Python + LangChain + Google APIs):** Handles data validation, communicates with Google Sheets, and performs AI-based summarization and question answering using LangChain with Google Gemini.  
- **Google Sheets:** Stores all spreadsheet data, column information, and user entries.  
- **LangChain + Google Gemini:** Serves as the LLM responsible for generating summaries and answering questions based on the sheet data.  
**Architecture Diagram:**
<img width="900" height="900" alt="googleSheets_architecture" src="https://github.com/user-attachments/assets/b7406b44-632c-4f87-aaef-c5801982c60f" />

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

### Setup
   Follow these steps to set up and run the Dynamic Google Sheets Assistant:

   **Step1**:Create Project Folder
   
   - Create a folder and navigate into it:

           mkdir googleSheet-assistant 
           cd googleSheet-assistant
   - Copy your `main.py` into this folder.
      
   **Step-2:** Create and Activate Virtual Environment 
   
   - Windows: `python -m venv venv` then `venv\Scripts\activate`
   - macOS/Linux: `python -m venv venv` then `source venv/bin/activate`
      
   **Step-3:** Install Dependencies
   
         pip install python-dotenv gradio pandas gspread oauth2client langchain-google-genai
   
   **Step-4:** Set Up Google Sheets API
   
   - Go to Google Cloud Console → Create a project.
   - Enable Google Sheets API.
   - Create a Service Account and download the JSON key file (credentials.json).
   - Place credentials.json in the same folder as main.py.
   - Share your Google Sheet with the Service Account email to allow read/write access.

   **Step-5:** Set Up Google Gemini API Key
   - Create a .env file in the same folder as main.py:

           GOOGLE_API_KEY=YOUR_GOOGLE_GEMINI_API_KEY
   - Replace YOUR_GOOGLE_GEMINI_API_KEY with your actual API key.
         
   **Step-6:** Run the Application
   
            python main.py
   - Gradio will start a local web server.
   - It will display a URL in the terminal, like:

         Running on local URL:  http://127.0.0.1:7860
   - Open this URL in your browser to access the Google Sheets Assistant.
     
### Real-Time Use Cases

- **Business Analytics:** Quickly summarize sales, inventory, or customer data in Google Sheets.  
- **Data Validation:** Ensure correct data types while inserting new entries.  
- **AI-Powered Insights:** Generate summaries and answers from spreadsheet data without manual calculations.
  
### Future Scope:
- Multi-Sheet Support : Extend the tool to handle multiple sheets in a single Google Spreadsheet for better data management.
- Data Visualization : Automatically generate charts (bar, line, pie) from sheet data for quick insights.
- Voice Interaction : Enable users to ask questions and insert data using speech commands.
- Cloud Deployment & Export : Deploy on cloud platforms for remote access and allow export of summaries in PDF or Excel.

### PPT Link : 
   https://docs.google.com/presentation/d/1ilBQXU9LOyTWz_0ioni46LMRKBQxjf8c/edit?usp=sharing&ouid=112554400976286662374&rtpof=true&sd=true
### Video Link : 
   https://drive.google.com/file/d/194z-83gzZqmk2lRqAvqSF1z2U_uo5oLE/view?usp=sharing
  
