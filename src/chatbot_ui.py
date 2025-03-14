"""
chatbot_ui.py
A single-file chatbot UI that uses your existing modules:
 - speech_to_text (record_audio, transcribe_audio)
 - llm_query_correction (correct_query_with_llm)
 - youtube_search (search_youtube)
 - video_player (play_video)

Features:
 - Type or voice-record your query.
 - If query starts with "search", we show top 5 YouTube results.
 - Then user can say "select N" to open that video.
 - A chat-like interface with a text widget for conversation.

Dependencies:
 pip install Pillow requests
 (and any dependencies you already have for your modules)
"""

import tkinter as tk
import threading
import webbrowser
from tkinter import messagebox

# For optional thumbnail fetching
import requests
from io import BytesIO
from PIL import Image, ImageTk

# Import your existing modules
from src.speech_to_text import record_audio, transcribe_audio
from src.llm_query_correction import correct_query_with_llm
from src.youtube_search import search_youtube
from src.video_player import play_video

class ChatbotUI:
    def __init__(self, root):
        self.root = root
        self.root.title("YouTube Voice Assistant Chatbot")
        self.root.geometry("900x600")

        # Main Frame
        main_frame = tk.Frame(root, bg="#2b2b2b")
        main_frame.pack(fill=tk.BOTH, expand=True)

        # Title Label
        self.title_label = tk.Label(
            main_frame,
            text="🎤 YouTube Voice Assistant",
            font=("Helvetica", 24, "bold"),
            fg="white",
            bg="#2b2b2b"
        )
        self.title_label.pack(pady=(10, 20))

        # Chat Display
        self.chat_display = tk.Text(
            main_frame,
            state='disabled',
            wrap='word',
            bg="#1e1e1e",
            fg="white",
            font=("Helvetica", 12)
        )
        self.chat_display.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        # User Input
        self.entry = tk.Entry(main_frame, font=("Helvetica", 14), bg="#3c3f41", fg="white", insertbackground="white")
        self.entry.pack(padx=10, pady=(0, 10), fill=tk.X)
        self.entry.bind("<Return>", self.handle_text_input)

        # Button Frame
        btn_frame = tk.Frame(main_frame, bg="#2b2b2b")
        btn_frame.pack(pady=5)

        # Record Voice Button
        self.record_btn = tk.Button(
            btn_frame,
            text="🎙️ Record Voice",
            font=("Helvetica", 12),
            fg="white",
            bg="#4CAF50",
            activebackground="#66bb6a",
            command=self.handle_voice_input
        )
        self.record_btn.pack(side=tk.LEFT, padx=5)

        # Videos Storage
        self.videos = []  # will store search results for selection


    def append_chat(self, message):
        """Append a message to the chat display."""
        self.chat_display.config(state='normal')
        self.chat_display.insert(tk.END, message + "\n")
        self.chat_display.config(state='disabled')
        self.chat_display.see(tk.END)

    def say(self, text):
        """Make the assistant 'speak' by appending text. (No TTS here, just chat text.)"""
        self.append_chat(f"Assistant: {text}")


    def handle_text_input(self, event=None):
        """Handle typed input from the Entry widget."""
        user_text = self.entry.get().strip()
        if user_text:
            self.append_chat("You: " + user_text)
            self.entry.delete(0, tk.END)
            self.process_input(user_text)

    def handle_voice_input(self):
        """Handle voice input in a separate thread."""
        threading.Thread(target=self.get_voice_input, daemon=True).start()

    def get_voice_input(self):
        """Record & transcribe audio, then process it."""
        self.say("Listening for your query...")
        record_audio()  # 1) record user_audio.wav
        text = transcribe_audio("user_audio.wav")  # 2) transcribe
        if not text:
            self.say("Sorry, I didn't catch that.")
            return
        # 3) optionally correct with LLM
        text = correct_query_with_llm(text)
        self.append_chat("You (voice): " + text)
        self.process_input(text)

    def process_input(self, text):
        """Process typed or spoken input."""
        text_lower = text.lower()
        if text_lower.startswith("search"):
            query = text[6:].strip()  
            if not query:
                self.say("Please provide a query after 'search'.")
                return
            self.search_videos(query)
        elif text_lower.startswith("select"):
            parts = text_lower.split()
            if len(parts) < 2:
                self.say("Please say 'select' followed by a number.")
                return
            try:
                index = int(parts[1]) - 1
                self.play_video_at_index(index)
            except ValueError:
                self.say("I didn't understand that selection. Try 'select 1' or 'select 2'.")
        else:
            self.search_videos(text)

    def search_videos(self, query):
        self.say(f"Searching YouTube for: {query}")
        results = search_youtube(query)
        if not results:
            self.say("No results found for that query.")
            return
        self.videos = results
        self.show_videos_in_chat()

    def show_videos_in_chat(self):
        """Show top 5 videos with optional thumbnails in chat."""
        for idx, video in enumerate(self.videos):
            self.append_chat(f"{idx+1}. {video['title']} ({video['duration']})")
        self.say("Say or type 'select 1' to open the first video, 'select 2' for the second, etc.")

    def play_video_at_index(self, index):
        if index < 0 or index >= len(self.videos):
            self.say("Invalid selection number.")
            return
        video = self.videos[index]
        self.say(f"Opening: {video['title']}")
        play_video(video["url"])

if __name__ == "__main__":
    root = tk.Tk()
    app = ChatbotUI(root)
    root.mainloop()
