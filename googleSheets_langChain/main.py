import os
from dotenv import load_dotenv
import gradio as gr
import pandas as pd
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from langchain_google_genai import ChatGoogleGenerativeAI

# ---------------- Load Gemini API Key ----------------
load_dotenv()
os.environ["GOOGLE_API_KEY"] = os.getenv("GOOGLE_API_KEY")

# ---------------- Google Sheets Setup ----------------
def connect_sheet(sheet_url):
    """Connects to a Google Sheet via URL."""
    try:
        scope = ["https://spreadsheets.google.com/feeds",
                 "https://www.googleapis.com/auth/drive"]
        creds = ServiceAccountCredentials.from_json_keyfile_name(
            "credentials.json", scope)
        client = gspread.authorize(creds)
        sheet = client.open_by_url(sheet_url).sheet1
        return sheet
    except Exception as e:
        print(f"Error connecting to sheet: {e}")
        return None

# ---------------- Gemini LLM Setup ----------------
llm = ChatGoogleGenerativeAI(model="gemini-2.5-pro")

# ---------------- Core Functions ----------------
def get_columns(sheet_url):
    """Return column headers and detected types of the sheet."""
    sheet = connect_sheet(sheet_url)
    if not sheet:
        return "❌ Cannot connect to sheet."
    df = pd.DataFrame(sheet.get_all_records())
    if df.empty:
        return "Sheet is empty!"
    types = []
    for col in df.columns:
        if pd.api.types.is_numeric_dtype(df[col]):
            types.append("Numeric")
        else:
            types.append("String")
    col_info = [f"{col} ({typ})" for col, typ in zip(df.columns, types)]
    return ", ".join(col_info)

def insert_data(sheet_url, row):
    """Insert a new row into the sheet with type validation."""
    try:
        sheet = connect_sheet(sheet_url)
        if not sheet:
            return "❌ Cannot connect to sheet."

        df = pd.DataFrame(sheet.get_all_records())
        if df.empty:
            return "❌ Sheet is empty, cannot detect types."

        values = [v.strip() for v in row.split(",")]
        headers = df.columns.tolist()
        if len(values) != len(headers):
            return f"❌ Number of values ({len(values)}) does not match columns ({len(headers)})."

        # Validate types
        for i, val in enumerate(values):
            col = df[headers[i]]
            if pd.api.types.is_numeric_dtype(col):
                try:
                    float(val)
                except ValueError:
                    return f"❌ Column '{headers[i]}' expects a numeric value. Got '{val}'."

        sheet.append_row(values)
        return f"✅ Row added successfully: {values}"
    except Exception as e:
        return f"❌ Error: {e}"

def summarize_sheet(sheet_url):
    """Generate a summary of the sheet data using LLM."""
    try:
        sheet = connect_sheet(sheet_url)
        if not sheet:
            return "❌ Cannot connect to sheet."
        data = sheet.get_all_records()
        df = pd.DataFrame(data)
        if df.empty:
            return "Sheet is empty!"
        table_text = df.to_string(index=False)
        prompt = f"Spreadsheet data:\n{table_text}\nProvide a clear summary without symbols like # or *."
        summary = llm.invoke(prompt)
        return summary.content
    except Exception as e:
        return f"❌ Error: {e}"

def ask_question(sheet_url, q):
    """Answer a question based on the sheet data using LLM."""
    try:
        sheet = connect_sheet(sheet_url)
        if not sheet:
            return "❌ Cannot connect to sheet."
        data = sheet.get_all_records()
        df = pd.DataFrame(data)
        if df.empty:
            return "Sheet is empty!"
        context = " ".join(df.astype(str).values.flatten())
        prompt = f"Based on this spreadsheet data, answer the question:\nData: {context}\nQuestion: {q}"
        response = llm.invoke(prompt)
        return response.content
    except Exception as e:
        return f"❌ Error: {e}"

# ---------------- Gradio Interface ----------------
with gr.Blocks() as demo:
    gr.Markdown("## 🧾 Dynamic Google Sheets Assistant")

    # Sheet URL Input
    sheet_input = gr.Textbox(label="Enter Google Sheet URL", placeholder="https://docs.google.com/spreadsheets/d/...")

    # ---------------- Insert Data Tab ----------------
    with gr.Tab("Insert Data"):
        col_display = gr.Textbox(label="Columns in Sheet (with types)", interactive=False)
        row_input = gr.Textbox(label="Enter row values comma-separated")
        insert_btn = gr.Button("Insert")
        insert_out = gr.Textbox(label="Result", lines=3)
        sheet_input.change(get_columns, inputs=sheet_input, outputs=col_display)
        insert_btn.click(insert_data, inputs=[sheet_input, row_input], outputs=insert_out)

    # ---------------- Summarize Tab ----------------
    with gr.Tab("Summarize Sheet"):
        sum_btn = gr.Button("Summarize")
        sum_out = gr.TextArea(label="Summary", lines=15)
        sum_btn.click(summarize_sheet, inputs=sheet_input, outputs=sum_out)

    # ---------------- Ask Question Tab ----------------
    with gr.Tab("Ask a Question"):
        q_box = gr.Textbox(label="Ask question")
        q_btn = gr.Button("Ask")
        q_out = gr.TextArea(label="Answer", lines=15)
        q_btn.click(ask_question, inputs=[sheet_input, q_box], outputs=q_out)

# Launch
demo.launch(share=True, prevent_thread_lock=False)