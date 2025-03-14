from yt_dlp import YoutubeDL

def search_youtube(query):
    if not query.startswith("ytsearch"):
        query = "ytsearch5:" + query

    print(f"🔍 DEBUG: Searching YouTube for '{query}'")

    ydl_opts = {
        'quiet': False,
        'default_search': 'ytsearch5',
        'extract_flat': True,
    }

    try:
        with YoutubeDL(ydl_opts) as ydl:
            result = ydl.extract_info(query, download=False)

        if not result or 'entries' not in result or not result['entries']:
            print("❌ DEBUG: No results found.")
            return []

        video_list = []
        for entry in result['entries']:
            video_list.append({
                "title": entry.get("title", "Unknown Title"),
                "url": entry.get("url", "No URL"),
                "duration": entry.get("duration", "Unknown"),
            })

        print(f"✅ DEBUG: Found {len(video_list)} videos.")
        return video_list

    except Exception as e:
        print(f"❌ DEBUG: Error fetching YouTube results: {e}")
        return []

