import os
import sys

import yt_dlp


DEFAULT_URL = "https://www.youtube.com/watch?v=SMKiELjUrlI"


def print_video_title(url: str, cookie_file: str = "cookies.txt"):
  ydl_opts = {
      # extract_flat speeds up the process since we only need basic metadata
      "extract_flat": True,
  }

  # Automatically use cookies.txt if it exists in the folder
  if os.path.exists(cookie_file):
    ydl_opts["cookiefile"] = cookie_file
    print("🍪 Using cookies.txt for authentication.")

  try:
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
      info = ydl.extract_info(url, download=False)
      title = info.get("title", "Unknown Title")
      print(f"\n📌 Video Title: {title}\n")
  except Exception as e:
    print(f"❌ An error occurred: {e}")


if __name__ == "__main__":
  target_url = sys.argv[1] if len(sys.argv) > 1 else DEFAULT_URL
  print_video_title(target_url)