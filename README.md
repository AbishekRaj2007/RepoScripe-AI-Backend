# 🚀 RepoScribe AI – Backend

RepoScribe AI Backend is a **FastAPI-based backend service** that generates professional `README.md` files for GitHub repositories using **AI-powered streaming responses**.

It uses **Groq LLMs (LLaMA 3.1)** to generate README content **token-by-token**, enabling real-time updates on the frontend.

---

## ✨ Features

- 🔥 AI-powered README generation
- ⚡ Real-time **streaming output**
- 🧠 Powered by **Groq (LLaMA 3.1 models)**
- 🌐 REST API using FastAPI
- 🔓 CORS enabled for frontend integration
- 🧩 Clean, modular backend architecture

---

## 🏗️ Tech Stack

- **Backend Framework:** FastAPI
- **AI Provider:** Groq
- **Model Used:** `llama-3.1-8b-instant`
- **Language:** Python 3.10+
- **Streaming:** FastAPI `StreamingResponse`
- **Server:** Uvicorn

---

## 📁 Project Structure

```text
RepoScribe-AI-Backend/
│
├── app/
│   ├── main.py                # FastAPI app & routes
│   ├── config.py              # Environment variables
│   └── services/
│       └── ai_service.py      # Groq streaming logic
│
├── venv/                      # Virtual environment
├── .env                       # API keys (ignored)
├── requirements.txt           # Python dependencies
└── README.md                  # Project documentation
🔐 Environment Variables
Create a .env file in the project root:

env
Copy code
GROQ_API_KEY=your_groq_api_key_here
⚠️ Do not commit .env to GitHub.

📦 Installation & Setup
1️⃣ Clone the repository
bash
Copy code
git clone https://github.com/your-username/reposcribe-ai-backend.git
cd reposcribe-ai-backend
2️⃣ Create and activate virtual environment
bash
Copy code
python -m venv venv
Windows

bash
Copy code
venv\Scripts\activate
Linux / macOS

bash
Copy code
source venv/bin/activate
3️⃣ Install dependencies
bash
Copy code
pip install -r requirements.txt
▶️ Running the Server
bash
Copy code
uvicorn app.main:app --reload
Server will start at:

dts
Copy code
http://127.0.0.1:8000
📖 API Documentation
Swagger UI:

dts
Copy code
http://127.0.0.1:8000/docs
🔁 Streaming README Generation Endpoint
POST /generate-readme-stream
Request Body
json
Copy code
{
  "repoUrl": "https://github.com/user/repository",
  "style": "professional"
}
Response
Streams README content token-by-token

Content-Type: text/plain

🧪 Testing the Streaming API (Recommended)
Use curl:

bash
Copy code
curl -N -X POST http://127.0.0.1:8000/generate-readme-stream \
-H "Content-Type: application/json" \
-d "{\"repoUrl\":\"https://github.com/octocat/Hello-World\",\"style\":\"professional\"}"
