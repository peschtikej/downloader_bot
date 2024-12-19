from yandex_music import Client
from django.conf import settings
from urllib.parse import urlparse, parse_qs


def get_track_id(yandex_music_url):
    try:
        # Parse the URL
        parsed_url = urlparse(yandex_music_url)
        # Extract the path
        path_parts = parsed_url.path.split('/')
        # The last part of the path after '/track/' is the track ID
        if 'track' in path_parts:
            track_id_index = path_parts.index('track') + 1
            track_id = path_parts[track_id_index]
            return track_id
        else:
            raise ValueError("Track ID not found in the URL.")
    except Exception as e:
        print(f"Error: {e}")
        return None

def download_yandex_music_track(track_id):
    try:
        token = settings.YA_TOKEN
        client = Client(token).init()

        track = client.tracks([get_track_id(track_id)])[0]

        file_path = settings.BASE_DIR / 'temp' / f"{track.artists[0].name} - {track.title}.mp3"
        track.download(file_path, bitrate_in_kbps=None)
        
        return file_path
    
    except Exception as e:
        print(f"An error occurred: {e}")
