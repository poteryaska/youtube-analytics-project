from helper.youtube_api_manual import channel, youtube
import json

class Channel:
    """Класс для ютуб-канала"""

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.__channel_id = channel_id
        self.channel = channel
        items = channel["items"][0]
        self.description = items["snippet"]["description"]
        self.title = items["snippet"]["title"]
        self.url = "https://www.youtube.com/channel/" + "UCMCgOm8GZkHp8zJ6l7_hIuA"
        self.subscriberCount = items["statistics"]["subscriberCount"]
        self.video_count = items["statistics"]["videoCount"]
        self.viewCount = items["statistics"]["viewCount"]

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        self.channel = channel
        print(self.channel)

    @property
    def channel_id(self):
        return self.__channel_id

    @staticmethod
    def get_service():
        '''Возвращает объект для работы с YouTube API'''
        return youtube

    def to_json(self, json_file):
        '''Сохраняет в файл значения атрибутов экземпляра `Channel`'''
        dict_channel = {}
        dict_channel['id'] = self.__channel_id
        dict_channel['description'] = self.description
        dict_channel['title'] = self.title
        dict_channel['url'] = self.url
        dict_channel['subscriberCount'] = self.subscriberCount
        dict_channel['video_count'] = self.video_count
        dict_channel['viewCount'] = self.viewCount
        with open("vdud.json", "w", encoding='utf-8') as write_file:
            json.dump(dict_channel, write_file, indent=4, ensure_ascii=False)




