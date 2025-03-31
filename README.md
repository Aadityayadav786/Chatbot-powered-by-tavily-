# AI Chatbot with Streamlit & FastAPI

This is an AI-powered chatbot using **Streamlit** for the frontend and **FastAPI** for the backend. The chatbot integrates with **Groq API** and supports web search using **Tavily API**.

## 🚀 Features
- **Conversational AI** powered by Groq API.
- **Web Search** functionality (optional).
- **Customizable System Prompt** to modify chatbot behavior.
- **Multiple Model Support** (LLaMA-3, Mixtral, etc.).
- **FastAPI Backend** for handling chatbot queries.
- **Deployable on Streamlit Community Cloud.**

---

## 📂 Project Structure
```
streamlit-chatbot/
│── ai_agent.py         # AI agent logic
│── backend.py         # FastAPI backend
│── frontend.py        # Streamlit UI
│── requirements.txt   # Required Python libraries
│── .gitignore         # Ignore unnecessary files
│── README.md          # Project documentation
```

---

## 🔧 Installation & Setup
### 1️⃣ Clone the Repository
```sh
git clone https://github.com/YOUR_USERNAME/streamlit-chatbot.git
cd streamlit-chatbot
```

### 2️⃣ Create & Activate Virtual Environment
```sh
# Create a virtual environment
python -m venv venv

# Activate it (Windows)
venv\Scripts\activate

# Activate it (Mac/Linux)
source venv/bin/activate
```

### 3️⃣ Install Dependencies
```sh
pip install -r requirements.txt
```

### 4️⃣ Set Up Environment Variables
Create a `.env` file in the project directory and add:
```
GROQ_API_KEY=your_groq_api_key
TAVILY_API_KEY=your_tavily_api_key
```

---

## ▶️ Running the Application
### **Step 1: Start the FastAPI Backend**
```sh
uvicorn backend:app --host 0.0.0.0 --port 8000
```

### **Step 2: Run Streamlit Frontend**
```sh
streamlit run frontend.py
```

---

## 🌍 Deploy on Streamlit Cloud
1. **Push your code to GitHub.**
2. **Go to** [Streamlit Community Cloud](https://share.streamlit.io/).
3. **Click “New App” → Select your GitHub repo**.
4. **Set `frontend.py` as the main file**.
5. **Add API keys in `secrets.toml`** under `Advanced Settings`:
   ```
   [secrets]
   GROQ_API_KEY = "your_groq_api_key"
   TAVILY_API_KEY = "your_tavily_api_key"
   ```
6. **Deploy! 🎉**

---

## 💡 Contributing
Feel free to fork this repo and submit pull requests to improve the chatbot!

---

## 📜 License
This project is **open-source** under the MIT License.

