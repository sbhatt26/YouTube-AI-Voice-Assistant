from src.speech_to_text import listen_to_user
from src.llm_query_correction import correct_query_with_llm
from src.youtube_search import search_youtube
from src.video_player import play_video

def youtube_voice_assistant():
    user_query = listen_to_user()
    if not user_query:
        print("No input detected. Try again.")
        return

    corrected_query = correct_query_with_llm(user_query)
    video_results = search_youtube(corrected_query)

    if not video_results:
        print("No results found.")
        return

    for idx, video in enumerate(video_results):
        print(f"{idx + 1}. {video['title']} ({video['duration']}) - {video['url']}")

    choice = int(input("\nEnter the number of the video you want to play: ")) - 1
    play_video(video_results[choice]["url"])

if __name__ == "__main__":
    youtube_voice_assistant()
