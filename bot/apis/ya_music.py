from yandex_music import Client
from django.conf import settings
from urllib.parse import urlparse


def get_album_and_track_id(yandex_music_url):
    """
    Extracts the album ID and track ID from a Yandex Music URL.
    """
    try:
        # Parse the URL
        parsed_url = urlparse(yandex_music_url)
        # Split the path into parts
        path_parts = parsed_url.path.split('/')
        
        # Extract album ID
        if 'album' in path_parts:
            album_id_index = path_parts.index('album') + 1
            album_id = path_parts[album_id_index]
        else:
            raise ValueError("Album ID not found in the URL.")
        
        # Extract track ID
        if 'track' in path_parts:
            track_id_index = path_parts.index('track') + 1
            track_id = path_parts[track_id_index]
        else:
            raise ValueError("Track ID not found in the URL.")
        
        return album_id, track_id
    except Exception as e:
        print(f"Error extracting album and track IDs: {e}")
        return None, None

def download_yandex_music_track(yandex_music_url):
    """
    Downloads a track from Yandex Music given its URL.
    """
    try:
        aldum_id, track_id = get_album_and_track_id(yandex_music_url)
        
        if track_id and aldum_id:
            token = settings.YA_TOKEN  
            client = Client(token).init()

            # Fetch the track metadata
            track = client.tracks([str(f"{track_id}:{aldum_id}")])[0]

            file_name = f"{track.artists[0].name} - {track.title}"
            artist = track.artists[0].name
            title = track.title
            cover = track.get_cover_url()

            file_path = settings.BASE_DIR / 'temp' / file_name

            # Download the track
            track.download(file_path)

            return file_path, artist, title, cover
    
    except Exception as e:
        print(f"An error occurred: {e}")
