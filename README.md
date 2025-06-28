# 🧠 MentorBot – Personalized AI Learning Companion

MentorBot is an AI-powered educational assistant that provides personalized answers, resource recommendations, progress tracking, and voice responses for learners. Built with Flask, OpenAI API, and a clean interactive UI — it helps users explore topics in Python, Math, Science, and more.

---

## 🌐 Live Demo

👉 [Live App on Render](https://mentorbot-9fh1.onrender.com)  
👉 [Frontend GitHub Repo](https://github.com/Prach2207/mentorbot)

---

## 🔑 Key Features

- ✅ **AI-Powered Q&A:** Ask questions on multiple subjects and get accurate AI answers
- ✅ **Fallback Response System:** Works even without an active OpenAI API (generates simulated responses)
- ✅ **Resource Recommendations:** Links to relevant online learning materials
- ✅ **Voice Output:** Mentored responses are spoken aloud (toggleable)
- ✅ **Learning Progress Tracker:** Visual progress bars by subject
- ✅ **Login & Signup System:** Secure access to your learning dashboard
- ✅ **Dark Mode UI:** Sleek, modern interface with glassmorphism design

---

## 🛠 Tech Stack

- **Frontend:** HTML, CSS, Bootstrap
- **Backend:** Python, Flask
- **AI:** OpenAI GPT (with fallback logic)
- **Voice:** JavaScript SpeechSynthesis API
- **Hosting:** Render (Backend)

---

## ⚙️ Setup Instructions (Local)

1. **Clone the repo**
   ```bash
   git clone https://github.com/your-username/mentorbot.git
   cd mentorbot
2.Create and activate virtual environment

bash
Copy
Edit
python -m venv venv
venv\Scripts\activate     # Windows
source venv/bin/activate  # macOS/Linux
3.Install dependencies
pip install -r requirements.txt
4.Add your OpenAI API key

Create a .env file in the root folder:

ini
Copy
Edit
OPENAI_API_KEY=your_openai_key_here
5.Run the app
python app.py

 Deployment Instructions (Render)
Push the project to GitHub

Go to https://render.com

Create a new Web Service → connect GitHub

---



Set:

Build Command: (leave blank)

Start Command: gunicorn app:app

Add environment variable:

OPENAI_API_KEY = your_key_here

Deploy and get your public URL


Author
Prachi Shivakumar Kallayyanamath
B.Tech Student



