# 🤖 JARVIS — AI-Powered Personal Assistant

An intelligent AI assistant inspired by Iron Man's JARVIS, powered by **Groq's LLaMA 3.3 70B** model with voice recognition, text-to-speech, weather forecasting, web search, task management, and bilingual support (English & Hindi).

![Python](https://img.shields.io/badge/Python-3.8+-blue?logo=python&logoColor=white)
![Groq](https://img.shields.io/badge/Groq-LLaMA_3.3_70B-orange)
![SQLite](https://img.shields.io/badge/SQLite-Database-green?logo=sqlite&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-yellow)

---

## ✨ Features

- **🧠 AI Conversations** — Natural language processing using Groq's LLaMA 3.3 70B model with context memory
- **🎤 Voice Input/Output** — Speech recognition + text-to-speech for hands-free interaction
- **🌐 Bilingual Support** — Full English and Hindi language support
- **🌤️ Weather Forecasting** — Real-time weather data with API integration
- **🔍 Web Search** — DuckDuckGo-powered web search from the command line
- **✅ Task Management** — Create, track, and complete tasks with persistent SQLite storage
- **💻 System Information** — CPU, memory, disk usage monitoring
- **🚀 App Launcher** — Open applications (VS Code, YouTube, Notes, etc.) via voice/text commands
- **💾 Conversation History** — All conversations stored in SQLite database
- **🎭 JARVIS Personality** — Witty, sophisticated AI persona that never breaks character

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- Groq API Key ([Get one free here](https://console.groq.com/))
- Microphone (optional, for voice input)

### Installation

```bash
# Clone the repository
git clone https://github.com/SneaKy17/jarvis-ai-assistant.git
cd jarvis-ai-assistant

# Install dependencies
pip install -r requirements.txt

# Set up environment variables
cp .env.example .env
# Edit .env and add your GROQ_API_KEY
```

### Run JARVIS

```bash
python main.py
```

Select your language (English/Hindi) and start interacting!

## 📁 Project Structure

```
jarvis-ai-assistant/
├── main.py                 # Application entry point & command loop
├── jarvis_engine.py        # Core AI engine (Groq/LLaMA integration)
├── input_handler.py        # Voice recognition & text-to-speech
├── database.py             # SQLite database for conversations & tasks
├── task_manager.py         # Task management (CRUD operations)
├── weather_handler.py      # Weather API integration
├── web_search_handler.py   # DuckDuckGo web search
├── system_handler.py       # System info (CPU, memory, disk)
├── config.py               # Configuration & environment variables
├── requirements.txt        # Python dependencies
├── .env.example            # Environment variable template
└── README.md               # This file
```

## 💬 Available Commands

| Category | Commands |
|----------|---------|
| 🌤️ **Weather** | "What's the weather?", "Will it rain?" |
| 🔍 **Search** | "Search for...", "Look up..." |
| ✅ **Tasks** | "Add a task...", "My pending tasks", "Mark task done" |
| 💻 **System** | "System information", "Disk space" |
| 🚀 **Apps** | "Open VS Code", "Open YouTube" |
| 🎤 **Input** | Press `1` for voice, `2` for text |
| 📝 **General** | Ask anything — JARVIS handles it with AI! |

## 🔬 Technical Details

### AI Engine
- **Model**: LLaMA 3.3 70B Versatile (via Groq API)
- **Context Window**: Rolling 20-message conversation history
- **Personality**: Custom system prompt maintaining JARVIS persona
- **Temperature**: 0.7 for balanced creativity

### Voice System
- **Input**: Google Speech Recognition API
- **Output**: pyttsx3 text-to-speech engine
- **Languages**: English (`en`) and Hindi (`hi`)
- **Fallback**: Text input when microphone unavailable

### Database
- **Engine**: SQLite3
- **Tables**: Conversations, Tasks, Calendar Events
- **Persistence**: All data stored locally in `jarvis_data.db`

## 🛠️ Tech Stack

| Category | Technology |
|----------|-----------|
| Language | Python 3.8+ |
| LLM | Groq API (LLaMA 3.3 70B) |
| Voice Input | SpeechRecognition |
| Voice Output | pyttsx3 |
| Database | SQLite3 |
| Web Search | DuckDuckGo API |
| System Info | psutil, platform |

## ⚙️ Configuration

Edit `.env` to customize:

```env
GROQ_API_KEY=your_api_key_here
JARVIS_NAME=JARVIS
USER_NAME=Sir
DEBUG=False
```

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

## 🤝 Contributing

Contributions are welcome! Feel free to open issues or submit pull requests.

---

*Built by [Nikhil Saklani](https://github.com/SneaKy17)*
