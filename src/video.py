from helper.youtube_api_manual import youtube


class Video:
    '''Класс для получения данных видео-ролика'''

    def __init__(self, video_id) -> None:
        """
        :param video_id: id видео
        Далее: название видео, ссылка на видео, количество просмотров, количество лайков
        """
        self.__video_id = video_id
        self.video_title = None
        self.url = None
        self.view_count = None
        self.like_count = None
        try:
            self.video_response = youtube.videos().list(part='snippet,statistics,contentDetails,topicDetails',
                                                        id=self.__video_id
                                                        ).execute()
            self.video_title: str = self.video_response['items'][0]['snippet']['title']
            self.url = "https://youtu.be/" + self.__video_id
            self.view_count: int = self.video_response['items'][0]['statistics']['viewCount']
            self.like_count: int = self.video_response['items'][0]['statistics']['likeCount']
        except IndexError:
            print("ID видео не сущестует")

    def __str__(self):
        '''Вывод названия видео'''
        return f"{self.video_title}"


class PLVideo:
    '''Класс для получения данных видео-ролика из плейлиста'''

    def __init__(self, video_id, playlist_id):
        """
        :param video_id: id видео
        :param playlist_id: id плейлиста
        Далее: название видео, ссылка на видео, количество просмотров, количество лайков
        """
        self.__video_id = video_id
        self.__playlist_id = playlist_id
        # получить данные по видеороликам в плейлисте
        playlist_videos = youtube.playlistItems().list(playlistId=playlist_id,
                                                       part='contentDetails',
                                                       maxResults=50,
                                                       ).execute()
        # получить все id видеороликов из плейлиста
        video_ids: list[str] = [video['contentDetails']['videoId'] for video in playlist_videos['items']]
        if video_id in video_ids:
            video_response = youtube.videos().list(part='snippet,statistics,contentDetails,topicDetails',
                                                   id=video_id
                                                   ).execute()

            self.video_title: str = video_response['items'][0]['snippet']['title']
            self.url = "https://youtu.be/" + self.__video_id
            self.view_count: int = video_response['items'][0]['statistics']['viewCount']
            self.like_count: int = video_response['items'][0]['statistics']['likeCount']

    def __str__(self):
        '''Вывод названия плейлиста'''
        return f"{self.video_title}"
