from helper.youtube_api_manual import youtube
import datetime
import isodate

class PlayList:
    '''Класс для получения данных из плейлиста'''
    def __init__(self, playlist_id):
        '''Инициализация по ID плейлиста
        атррибуты: название плейлиста и ссылка на плейлист
        '''

        self.__playlist_id = playlist_id
        # Данные плейлиста
        playlist = youtube.playlistItems().list(playlistId=playlist_id,
                                               part='snippet',
                                               maxResults=50,
                                               ).execute()
        # Находим ID канала
        channel_id = playlist['items'][0]['snippet']['channelId']
        # Вытаскиваем все плейлисты канала
        playlists_channel = youtube.playlists().list(channelId=channel_id,
                                          part='contentDetails,snippet',
                                          maxResults=50,
                                          ).execute()
        # Перебираем плейлисты канала чтобы вытащить нужный и вывести название плейлиста
        for playlist in playlists_channel['items']:
            if playlist['id'] == playlist_id:
                self.title = playlist['snippet']['title']
                break
            else:
                self.title = None
        self.url = 'https://www.youtube.com/playlist?list=' + self.__playlist_id

        # Вытаскиваем все видео для подсчета общей длительности плейлиста
        self.playlist_videos = youtube.playlistItems().list(playlistId=self.__playlist_id,
                                                       part='contentDetails',
                                                       maxResults=50,
                                                       ).execute()
        # получить все id видеороликов из плейлиста
        self.video_ids: list[str] = [video['contentDetails']['videoId'] for video in self.playlist_videos['items']]
        self.video_response = youtube.videos().list(part='contentDetails,statistics',
                                               id=','.join(self.video_ids)
                                               ).execute()
        # Складываем время каждого видео
        self.__total_duration = datetime.timedelta()
        for video in self.video_response['items']:
            # YouTube video duration is in ISO 8601 format
            iso_8601_duration = video['contentDetails']['duration']
            duration = isodate.parse_duration(iso_8601_duration)
            self.__total_duration += duration

    @property
    def total_duration(self):
        return self.__total_duration

    def show_best_video(self):
        max_likes = 0
        url_best_video = ''
        for video in self.video_response:
            if video['items']['statistics']['likeCount'] > max_likes:
                max_likes = int(video['items']['statistics']['likeCount'])
                url_best_video = "https://youtu.be/" + video['items']['id']
        return url_best_video


a = PlayList('PLguYHBi01DWr4bRWc4uaguASmo7lW4GCb')
print(a.show_best_video())