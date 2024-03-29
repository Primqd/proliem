from googleapiclient.discovery import build

# sys.stdout = open("yotoob.txt", "w")

DEVELOPER_KEY = 'AIzaSyDYkolVCwve3ijI2hAHro2i0up-jtNzwnE' # our api key, please don't steal :pleadingface:
YOUTUBE_API_SERVICE_NAME = 'youtube'
YOUTUBE_API_VERSION = 'v3'

youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,developerKey=DEVELOPER_KEY)

def search_videos(key_words):
    key_word = "|".join(key_words)
    # search_response = youtube.search().list(
    # q = key_word,
    # part='snippet',
    # maxResults= 25
    # ).execute()
    return youtube.search().list(
    q = key_word,
    part='snippet',
    maxResults= 25
    ).execute()