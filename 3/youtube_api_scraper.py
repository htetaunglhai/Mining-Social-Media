import csv, json, requests


#channel_id1 = 'UCJFp8uSYCjXOMnkUyb3CQ3Q'
channel_id2 = 'UCpko_-a4wgz2u_DgDgd9fqA'
youtube_api_key = 'AIzaSyC5FYz5NdRX7Y8Jbj1jtluW1iAo2pab5IY'

def make_csv(page_id):

    base = 'https://www.googleapis.com/youtube/v3/search?'
    fields = '&part=snippet&channelId='
    api_key = '&key=' + youtube_api_key
    api_url = base + fields + page_id + api_key
    api_response = requests.get(api_url)
    videos = json.loads(api_response.text)

    with open('%syoutube_videos.csv' % page_id, 'w') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow([
        'publishedAt',
        'title',
        'description',
        'thumbnailurl'
        ])
        has_another_page = True
        while has_another_page:
            if videos.get('items') is not None:
                for video in videos.get('items'):
                    video_data_row = [
                        video['snippet']['publishedAt'],
                        video['snippet']['title'],
                        video['snippet']['description'],
                        video['snippet']['thumbnails']['default']['url']
                    ]
                    csv_writer.writerow(video_data_row)
            if 'nextPageToken' in videos.keys():
                next_page_url = api_url + '&nextPageToken=' + videos['nextPageToken']
                next_page_posts = requests.get(next_page_url)
                videos = json.loads(next_page_posts.text)
            else:
                print('No more videos')
                has_another_page = False

#make_csv(channel_id1)
make_csv(channel_id2)
