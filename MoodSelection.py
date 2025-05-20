import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import datetime
import gspread
from google.oauth2.service_account import Credentials
import json
import os

# --- Google Sheets Setup ---
SCOPE = ["https://www.googleapis.com/auth/spreadsheets", "https://www.googleapis.com/auth/drive"]
json_str = os.environ.get("GOOGLE_SERVICE_ACCOUNT_JSON")
CREDS = Credentials.from_service_account_info(json.loads(json_str), scopes=SCOPE)
client = gspread.authorize(CREDS)

SHEET_NAME = "MoodRecording"
sheet = client.open(SHEET_NAME).sheet1

# --- Mood Options ---
MOODS = {
    "😊": "Happy",
    "😠": "Frustrated",
    "😕": "Confused",
    "🎉": "Celebratory"
}

# --- UI ---
st.title("🧪 Mood of the Queue")

# Mood logging form
with st.form("mood_form"):
    mood = st.selectbox("How's the mood?", options=list(MOODS.keys()))
    note = st.text_input("Optional note")
    submitted = st.form_submit_button("Log Mood")

    if submitted:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        sheet.append_row([timestamp, mood, note])
        st.success("Mood logged!")

# Load data
rows = sheet.get_all_records()
if rows:
    df = pd.DataFrame(rows)
    df['Timestamp'] = pd.to_datetime(df['Timestamp'])
    df_today = df[df['Timestamp'].dt.date == datetime.today().date()]

    mood_counts = df_today['Mood'].value_counts().reset_index()
    mood_counts.columns = ['Mood', 'count']

    if not mood_counts.empty:
        fig = px.bar(mood_counts, x='Mood', y='count', title="Today's Mood Distribution")
        st.plotly_chart(fig)
    else:
        st.info("No mood entries for today yet.")
else:
    st.info("The sheet has no data yet.")
