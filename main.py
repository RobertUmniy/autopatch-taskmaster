import os
import json
from dotenv import load_dotenv
from google import genai
from google.genai import types
import firebase_admin
from firebase_admin import credentials, firestore

# 1. Load environment variables
load_dotenv()

# 2. Initialize Firebase Admin SDK
cred = credentials.Certificate("serviceAccountKey.json")
if not firebase_admin._apps:
    firebase_admin.initialize_app(cred)
db = firestore.client()

# 3. Initialize Gemini Client
ai = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def run_taskmaster(error_log: str):
    print("🤖 [AutoPatch AI] Analyzing error log and generating fix...")
    
    prompt = f"""
    You are an autonomous SRE Agent. Analyze the error log and generate a code fix without human interaction.
    Error Log: {error_log}

    Return strictly JSON with fields:
    - "root_cause": Brief description of the issue
    - "code_fix": The corrected Python code
    - "status": Execution status ("FIXED")
    """

    res = ai.models.generate_content(
        model="gemini-3.6-flash",
        contents=prompt,
        config=types.GenerateContentConfig(response_mime_type="application/json")
    )
    data = json.loads(res.text)

    # Store execution result in Google Cloud Firestore
    doc = db.collection("taskmaster_runs").document()
    doc.set({**data, "timestamp": firestore.SERVER_TIMESTAMP})

    print(f"\n✅ [SUCCESS] Result received from Gemini and stored in Firebase Firestore!")
    print(f"📄 Document ID: {doc.id}")
    print(f"🛠️ Root Cause: {data.get('root_cause')}")
    print(f"💡 Fixed Code:\n{data.get('code_fix')}")
    return data

if __name__ == "__main__":
    test_log = "ZeroDivisionError: division by zero in calculate_metrics() at line 42"
    run_taskmaster(test_log)