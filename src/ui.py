# import sys
# import os
# import tkinter as tk
# from tkinter import messagebox
# import threading
# from src.speech_to_text import record_audio, transcribe_audio
# from src.llm_query_correction import correct_query_with_llm
# from src.youtube_search import search_youtube
# import webbrowser
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# class YouTubeVoiceAssistantUI:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("YouTube Voice Assistant")
#         self.root.geometry("500x500")
#         self.root.configure(bg="#f0f0f0")

#         # Title Label
#         self.label = tk.Label(root, text="🎤 YouTube Voice Assistant", font=("Arial", 14, "bold"), bg="#f0f0f0")
#         self.label.pack(pady=10)

#         # Record Button
#         self.record_button = tk.Button(root, text="🎙️ Record Voice", font=("Arial", 12), command=self.start_recording, bg="#4CAF50", fg="white")
#         self.record_button.pack(pady=10)

#         # Transcription Text
#         self.transcription_label = tk.Label(root, text="Transcribed Query:", font=("Arial", 10, "bold"), bg="#f0f0f0")
#         self.transcription_label.pack()
#         self.transcription_text = tk.StringVar()
#         self.transcription_entry = tk.Entry(root, textvariable=self.transcription_text, width=50, font=("Arial", 10))
#         self.transcription_entry.pack(pady=5)

#         # Search Button
#         self.search_button = tk.Button(root, text="🔍 Search YouTube", font=("Arial", 12), command=self.search_youtube, bg="#008CBA", fg="white")
#         self.search_button.pack(pady=10)

#         # Video Results Listbox
#         self.results_label = tk.Label(root, text="Select a video:", font=("Arial", 10, "bold"), bg="#f0f0f0")
#         self.results_label.pack()
#         self.video_listbox = tk.Listbox(root, width=60, height=6)
#         self.video_listbox.pack(pady=5)

#         # Play Button
#         self.play_button = tk.Button(root, text="▶ Play Video", font=("Arial", 12), command=self.play_selected_video, bg="#f44336", fg="white")
#         self.play_button.pack(pady=10)

#     def start_recording(self):
#         self.record_button.config(state=tk.DISABLED, text="🎙️ Recording...")
#         threading.Thread(target=self.process_voice_command).start()

#     def process_voice_command(self):
#         record_audio()
#         transcribed_text = transcribe_audio()
#         corrected_query = correct_query_with_llm(transcribed_text)
#         self.transcription_text.set(corrected_query)
#         self.record_button.config(state=tk.NORMAL, text="🎙️ Record Voice")

#     def search_youtube(self):
#         query = self.transcription_text.get()
#         if not query:
#             messagebox.showwarning("Warning", "Please provide a query first!")
#             return

#         self.video_listbox.delete(0, tk.END)
#         self.videos = search_youtube(query)

#         for idx, video in enumerate(self.videos):
#             self.video_listbox.insert(idx, f"{video['title']} ({video['duration']})")

#     def play_selected_video(self):
#         selected_index = self.video_listbox.curselection()
#         if not selected_index:
#             messagebox.showwarning("Warning", "Please select a video first!")
#             return

#         selected_video = self.videos[selected_index[0]]
#         webbrowser.open(selected_video["url"])

# if __name__ == "__main__":
#     root = tk.Tk()
#     app = YouTubeVoiceAssistantUI(root)
#     root.mainloop()

# import tkinter as tk
# import ttkbootstrap as ttk
# from ttkbootstrap.constants import *
# import threading
# import webbrowser
# from tkinter import messagebox

# from src.speech_to_text import record_audio, transcribe_audio
# from src.llm_query_correction import correct_query_with_llm
# from src.youtube_search import search_youtube

# class YouTubeVoiceAssistantUI:
#     def __init__(self, root):
#         # Choose a theme
#         style = ttk.Style("cyborg")  # e.g., "cyborg", "flatly", "superhero", etc.
#         root.title("YouTube Voice Assistant")
#         root.geometry("650x700")

#         # Main frame
#         main_frame = ttk.Frame(root, padding=20)
#         main_frame.pack(fill=BOTH, expand=YES)

#         # Title
#         self.title_label = ttk.Label(
#             main_frame,
#             text="🎤 YouTube Voice Assistant",
#             font=("Helvetica", 24, "bold"),
#             bootstyle="inverse-primary"
#         )
#         self.title_label.pack(pady=(0, 20))

#         # Record Button
#         self.record_button = ttk.Button(
#             main_frame,
#             text="🎙️ Record Voice",
#             command=self.start_recording,
#             bootstyle="success outline",
#             width=20
#         )
#         self.record_button.pack(pady=10)

#         # Transcribed Query
#         transcribed_frame = ttk.Frame(main_frame)
#         transcribed_frame.pack(fill=X, pady=10)

#         self.transcription_label = ttk.Label(
#             transcribed_frame,
#             text="Transcribed Query:",
#             font=("Helvetica", 12, "bold")
#         )
#         self.transcription_label.pack(anchor=W)

#         self.transcription_var = tk.StringVar()
#         self.transcription_entry = ttk.Entry(
#             transcribed_frame,
#             textvariable=self.transcription_var,
#             font=("Helvetica", 12),
#             width=50
#         )
#         self.transcription_entry.pack(pady=5, fill=X)

#         # Search Button
#         self.search_button = ttk.Button(
#             main_frame,
#             text="🔍 Search YouTube",
#             command=self.search_youtube,
#             bootstyle="info outline",
#             width=20
#         )
#         self.search_button.pack(pady=10)

#         # Results Frame
#         results_frame = ttk.Frame(main_frame)
#         results_frame.pack(fill=BOTH, expand=YES, pady=10)

#         self.results_label = ttk.Label(
#             results_frame,
#             text="Select a Video:",
#             font=("Helvetica", 12, "bold")
#         )
#         self.results_label.pack(anchor=W)

#         # Listbox + Scrollbar
#         listbox_frame = ttk.Frame(results_frame)
#         listbox_frame.pack(fill=BOTH, expand=YES)

#         self.scrollbar = ttk.Scrollbar(listbox_frame, bootstyle="secondary-round")
#         self.scrollbar.pack(side=RIGHT, fill=Y)

#         # Use the standard tk.Listbox here, NOT ttk.Listbox
#         self.video_listbox = tk.Listbox(
#             listbox_frame,
#             yscrollcommand=self.scrollbar.set,
#             font=("Helvetica", 11),
#             height=8,
#             bg="#2e2e2e",       # Optional dark background
#             fg="white",         # White text
#             selectbackground="#5e5e8a"  # A highlight color
#         )
#         self.video_listbox.pack(side=LEFT, fill=BOTH, expand=YES)
#         self.scrollbar.configure(command=self.video_listbox.yview)

#         # Play Button
#         self.play_button = ttk.Button(
#             main_frame,
#             text="▶ Play Video",
#             command=self.play_selected_video,
#             bootstyle="danger outline",
#             width=20
#         )
#         self.play_button.pack(pady=10)

#     def start_recording(self):
#         self.record_button.configure(state=DISABLED, text="🎙️ Recording...")
#         threading.Thread(target=self.process_voice_command, daemon=True).start()

#     def process_voice_command(self):
#         record_audio()
#         transcribed_text = transcribe_audio()
#         corrected_query = correct_query_with_llm(transcribed_text)
#         self.transcription_var.set(corrected_query)
#         self.record_button.configure(state=NORMAL, text="🎙️ Record Voice")

#     def search_youtube(self):
#         query = self.transcription_var.get().strip()
#         if not query:
#             messagebox.showwarning("Warning", "Please provide a query first!")
#             return

#         self.video_listbox.delete(0, tk.END)
#         self.videos = search_youtube(query)

#         for idx, video in enumerate(self.videos):
#             self.video_listbox.insert(idx, f"{video['title']} ({video['duration']})")

#     def play_selected_video(self):
#         selection = self.video_listbox.curselection()
#         if not selection:
#             messagebox.showwarning("Warning", "Please select a video first!")
#             return

#         video = self.videos[selection[0]]
#         webbrowser.open(video["url"])


# if __name__ == "__main__":
#     app = ttk.Window(themename="cyborg")  # You can change the theme here
#     YouTubeVoiceAssistantUI(app)
#     app.mainloop()



import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
import threading
import webbrowser
from tkinter import messagebox

# Import your modules
from src.speech_to_text import record_audio, transcribe_audio
from src.llm_query_correction import correct_query_with_llm
from src.youtube_search import search_youtube

class YouTubeVoiceAssistantUI:
    def __init__(self, root):
        style = ttk.Style("cyborg")  # Example theme
        root.title("YouTube Voice Assistant")
        root.geometry("650x400")

        main_frame = ttk.Frame(root, padding=20)
        main_frame.pack(fill=BOTH, expand=YES)

        # Title
        self.title_label = ttk.Label(
            main_frame,
            text="🎤 YouTube Voice Assistant",
            font=("Helvetica", 24, "bold"),
            bootstyle="inverse-primary"
        )
        self.title_label.pack(pady=(0, 20))

        # Record Button
        self.record_button = ttk.Button(
            main_frame,
            text="🎙️ Record Voice",
            command=self.start_recording,
            bootstyle="success outline",
            width=20
        )
        self.record_button.pack(pady=10)

        # Transcribed Query
        transcribed_frame = ttk.Frame(main_frame)
        transcribed_frame.pack(fill=X, pady=10)

        self.transcription_label = ttk.Label(
            transcribed_frame,
            text="Transcribed Query:",
            font=("Helvetica", 12, "bold")
        )
        self.transcription_label.pack(anchor=W)

        self.transcription_var = tk.StringVar()
        self.transcription_entry = ttk.Entry(
            transcribed_frame,
            textvariable=self.transcription_var,
            font=("Helvetica", 12),
            width=50
        )
        self.transcription_entry.pack(pady=5, fill=X)

        # Search Button
        self.search_button = ttk.Button(
            main_frame,
            text="🔍 Search YouTube",
            command=self.search_youtube,
            bootstyle="info outline",
            width=20
        )
        self.search_button.pack(pady=10)

    def start_recording(self):
        self.record_button.configure(state=DISABLED, text="🎙️ Recording...")
        threading.Thread(target=self.process_voice_command, daemon=True).start()

    def process_voice_command(self):
        record_audio()
        transcribed_text = transcribe_audio()
        corrected_query = correct_query_with_llm(transcribed_text)
        self.transcription_var.set(corrected_query)
        self.record_button.configure(state=NORMAL, text="🎙️ Record Voice")

    def search_youtube(self):
        query = self.transcription_var.get().strip()
        if not query:
            messagebox.showwarning("Warning", "Please provide a query first!")
            return

        videos = search_youtube(query)
        if not videos:
            messagebox.showwarning("Warning", "No results found for this query!")
            return

        top_result = videos[0]
        print(f"🔗 Opening: {top_result['url']}")
        webbrowser.open(top_result["url"])

if __name__ == "__main__":
    app = ttk.Window(themename="cyborg")
    YouTubeVoiceAssistantUI(app)
    app.mainloop()
