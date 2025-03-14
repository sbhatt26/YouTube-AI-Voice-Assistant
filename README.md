# YouTube AI Voice Assistant 🎙️🎥

A voice-controlled AI assistant that enables hands-free YouTube search and playback using **GPT-4o, Whisper, and FastAPI**. This assistant processes natural language voice commands, retrieves relevant YouTube videos, and provides seamless user interaction through speech-to-text and text-to-speech models.

---

## Features 🚀

- **Voice-Activated YouTube Search** – Users can speak commands to search for videos.
- **Real-Time Speech Recognition** – Uses **OpenAI Whisper** for high-accuracy speech-to-text processing.
- **AI-Powered Query Interpretation** – **GPT-4o** enhances query understanding and refines search results.
- **Automated Video Playback** – Fetches and plays videos directly from YouTube.
- **Multi-Language Support** – Processes commands in various languages for accessibility.
- **FastAPI Backend** – Ensures low-latency responses and scalable API handling.

---

## Tech Stack 🛠️

- **Backend:** FastAPI, Python
- **AI Models:** OpenAI Whisper (Speech-to-Text), GPT-4o (NLP), Google Text-to-Speech (TTS)
- **YouTube Integration:** YouTube Data API v3, yt-dlp
- **Frontend (Optional):** Vue.js
- **Deployment:** Docker, AWS Lambda (Optional), Firebase

---

## 📂 Project Structure

/youtube_ai_voice_assistant  
├── **chatbot_ui.py** – Interactive chatbot UI for YouTube search  
├── **llm_query_correction.py** – Corrects search queries using GPT-4o  
├── **speech_to_text.py** – Records & transcribes voice input using Whisper  
├── **youtube_search.py** – Fetches top YouTube results  
├── **video_player.py** – Opens selected YouTube video in browser  
└── **main.py** – Orchestrates speech recognition, query correction, and video search  

---

### **1️⃣ Clone the Repository**

```bash
git clone https://github.com/yourusername/youtube-ai-voice-assistant.git
cd youtube-ai-voice-assistant
```

### 2️⃣ Create a Virtual Environment (Optional but Recommended)

```bash
python -m venv venv
source venv/bin/activate  # MacOS/Linux
venv\Scripts\activate     # Windows
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Set Up API Keys

Create a `.env` file and add the following keys:

```bash
OPENAI_API_KEY=your_openai_key
```

---

## **🗣️ Usage**

1. **Start the assistant** and enable your microphone.
2. Speak a command like:
   - _"Search for the latest AI research on YouTube."_
   - _"Play the top video about deep learning."_
3. The assistant will:
   - Convert speech to text using **Whisper**
   - Correct the query with **GPT-4o**
   - Fetch and display **top 5 YouTube results**
   - Play the selected video

---

## **📡 Example API Request**

To test the backend:

```bash
curl -X POST "http://localhost:8000/search" -H "Content-Type: application/json" \
-d '{"query": "latest AI research"}'
```

## 🔮 Future Enhancements

- 🔷 **Real-time video transcription**
- 🔷 **Voice-controlled playback (pause, resume, skip)**
- 🔷 **Smart home integration**
