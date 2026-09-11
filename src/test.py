import yt_dlp

url = "https://www.youtube.com/watch?v=EK0hksG9VHI"

try:
    # Configure yt-dlp with options
    ydl_opts = {
        'quiet': False,
        'no_warnings': False,
    }
    
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=False)
    
    print(f"Title: {info.get('title', 'N/A')}")
    print(f"Duration: {info.get('duration', 'N/A')} seconds")
    
except yt_dlp.utils.DownloadError as e:
    print(f"Download Error: {str(e)}")
    print("\nNote: YouTube may require:")
    print("1. Browser cookies (--cookies-from-browser)")
    print("2. A JavaScript runtime (Node.js/Deno)")
    print("3. Authentication with valid credentials")
    
except Exception as e:
    print(f"Error: {type(e).__name__}: {str(e)}")



import yt_dlp

url = "https://www.youtube.com/watch?v=EK0hksG9VHI"

with yt_dlp.YoutubeDL() as ydl:
    info = ydl.extract_info(url, download=False)

print(info["title"])

