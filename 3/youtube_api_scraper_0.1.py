import csv, json, requests

api_url = 'https://www.googleapis.com/youtube/v3/search?part=snippet&channelId=UCJFp8uSYCjXOMnkUyb3CQ3Q&key=AIzaSyC5FYz5NdRX7Y8Jbj1jtluW1iAo2pab5IY'

api_response = requests.get(api_url)
videos = json.loads(api_response.text)

with open('youtube_videos.csv', 'w') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow([
    'publishedAt',
    'title',
    'description',
    'thumbnailurl'
    ])
    if videos.get('items') is not None:
        for video in videos.get('items'):
            video_data_row = [
                video['snippet']['publishedAt'],
                video['snippet']['title'],
                video['snippet']['description'],
                video['snippet']['thumbnails']['default']['url']
            ]
            csv_writer.writerow(video_data_row)
