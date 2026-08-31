# 🛠️ AutoPatch AI — Autonomous SRE Agent

AutoPatch AI is an autonomous background SRE agent built for the **All Things Agentic Hackathon** (Taskmaster track).

It automatically intercepts system error logs, performs root-cause analysis using **Gemini 3.6 Flash**, generates executable code fixes, and persists execution states directly in **Google Cloud Firestore**.

## 🚀 Features
- **Zero-Touch Root Cause Analysis**: Evaluates error stack traces without human intervention.
- **Automated Patch Generation**: Generates clean, corrected Python functions.
- **State Persistence**: Records execution metrics and document IDs in Firestore (`taskmaster_runs`).

## 🛠️ Tech Stack
- **AI Model**: Google Gemini 3.6 Flash (`google-genai` SDK)
- **Database**: Google Cloud Firestore (`firebase-admin` SDK)
- **Language**: Python 3.12+

## ⚙️ Quick Start

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/RobertUmniy/autopatch-taskmaster.git](https://github.com/RobertUmniy/autopatch-taskmaster.git)
   cd autopatch-taskmaster
Install dependencies:

Bash
pip install -r requirements.txt
Configure Environment:
Create a .env file with your Gemini API key:

Фрагмент кода
GEMINI_API_KEY=your_gemini_api_key
Place your Firebase service account JSON key as serviceAccountKey.json in the root folder.

Run the Agent:

Bash
python main.py
