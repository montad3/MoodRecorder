# 🧪 Mood of the Queue

A lightweight internal tool to log and visualize the emotional "vibe" of the support ticket queue throughout the day.

Built with [Streamlit](https://streamlit.io/), [Google Sheets](https://www.google.com/sheets/about/), and ❤️.

---

## 🚀 Features

- Log mood via emoji dropdown
- Optional notes for context
- Appends entries to a shared Google Sheet
- Visualizes today's mood entries in a live bar chart

---

## 📸 Demo

![demo](https://user-images.githubusercontent.com/your-demo-screenshot.gif)

> Replace with Loom walkthrough or screenshot if needed.

---

## 🛠️ How It Works

1. Select your mood (😊 😠 😕 🎉)
2. Optionally add a note (e.g., “Rx delays today”)
3. Click **Log Mood**
4. View the bar chart of mood entries for today

---

## 🧱 Tech Stack

- Python 3
- Streamlit
- Plotly
- Pandas
- Google Sheets (via `gspread` and `google-auth`)

---

## 🔐 Google Sheets Setup

To connect securely to Google Sheets:

1. Create a Google Cloud project
2. Enable the **Google Sheets API** and **Google Drive API**
3. Create a **service account** and download its JSON key
4. Share your Google Sheet with the service account email as an Editor

Store the service account key as a secret on Streamlit Cloud:

```toml
GOOGLE_SERVICE_ACCOUNT_JSON = """{
  "type": "service_account",
  ...
}"""