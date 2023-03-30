import datetime

import isodate

from helper.youtube_api_manual import youtube


class PlayList:
    '''Класс для получения данных из плейлиста'''

    def __init__(self, playlist_id):
        '''Инициализация по ID плейлиста
        атррибут: название плейлиста и ссылка на плейлист
        '''
        self.__playlist_id = playlist_id

    @property
    def title(self):
        '''Перебираем плейлисты канала чтобы вытащить нужный и выводим название плейлиста'''
        for playlist in self.get_playlists_channel()['items']:
            if playlist['id'] == self.__playlist_id:
                self.__title = playlist['snippet']['title']
                break
            else:
                self.__title = None
        return self.__title

    @property
    def url(self):
        '''Получаем ссылку на плейлист'''
        self.__url = 'https://www.youtube.com/playlist?list=' + self.__playlist_id
        return self.__url

    @property
    def total_duration(self):
        '''Получаем общую длительность всех видео в плейлисте'''
        self.__total_duration = datetime.timedelta()
        for video in self.get_video_response()['items']:
            # YouTube video duration is in ISO 8601 format
            iso_8601_duration = video['contentDetails']['duration']
            duration = isodate.parse_duration(iso_8601_duration)
            self.__total_duration += duration
        return self.__total_duration

    def show_best_video(self):
        '''Возвращает ссылку на самое популярное видео из плейлиста (по количеству лайков)'''
        max_likes = 0
        for video in self.video_response['items']:
            if int(video['statistics']['likeCount']) > max_likes:
                max_likes = int(video['statistics']['likeCount'])
                self.__url_best_video = "https://youtu.be/" + video['id']
        return self.__url_best_video

    def get_playlists_channel(self):
        '''Получаем данные плейлистов канала'''
        self.playlist = youtube.playlistItems().list(playlistId=self.__playlist_id,
                                                     part='snippet',
                                                     maxResults=50,
                                                     ).execute()
        # Находим ID канала
        self.channel_id = self.playlist['items'][0]['snippet']['channelId']
        # Вытаскиваем все плейлисты канала
        self.playlists_channel = youtube.playlists().list(channelId=self.channel_id,
                                                          part='contentDetails,snippet',
                                                          maxResults=50,
                                                          ).execute()
        return self.playlists_channel

    def get_video_response(self):
        '''Получаем данные всех видео плейлиста'''
        self.playlist_videos = youtube.playlistItems().list(playlistId=self.__playlist_id,
                                                            part='contentDetails',
                                                            maxResults=50,
                                                            ).execute()
        # получить все id видеороликов из плейлиста
        self.video_ids: list[str] = [video['contentDetails']['videoId'] for video in self.playlist_videos['items']]
        self.video_response = youtube.videos().list(part='contentDetails,statistics',
                                                    id=','.join(self.video_ids)
                                                    ).execute()
        return self.video_response
