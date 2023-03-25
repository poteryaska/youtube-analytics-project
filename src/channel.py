from helper.youtube_api_manual import youtube, printj
import json


class Channel:
    """Класс для ютуб-канала"""

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.__channel_id = channel_id
        channel = youtube.channels().list(id=self.__channel_id, part='snippet,statistics').execute()
        self.__channel = channel
        self.__items = self.__channel["items"][0]
        self.__description = self.__items["snippet"]["description"]
        self.__title = self.__items["snippet"]["title"]
        self.__url = "https://www.youtube.com/channel/" + self.__channel_id
        self.__subscriberCount = self.__items["statistics"]["subscriberCount"]
        self.__video_count = self.__items["statistics"]["videoCount"]
        self.__viewCount = self.__items["statistics"]["viewCount"]

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        printj(self.channel)

    @property
    def channel_id(self):
        return self.__channel_id

    @property
    def channel(self):
        return self.__channel

    @property
    def items(self):
        return self.__items

    @property
    def description(self):
        return self.__description

    @property
    def title(self):
        return self.__title

    @property
    def url(self):
        return self.__url

    @property
    def subscriberCount(self):
        return self.__subscriberCount

    @property
    def video_count(self):
        return self.__video_count

    @property
    def viewCount(self):
        return self.__viewCount

    @staticmethod
    def get_service():
        '''Возвращает объект для работы с YouTube API'''
        return youtube

    def to_json(self, json_file):
        '''Сохраняет в файл значения атрибутов экземпляра `Channel`'''
        dict_channel = {}
        dict_channel['id'] = self.__channel_id
        dict_channel['description'] = self.__description
        dict_channel['title'] = self.__title
        dict_channel['url'] = self.__url
        dict_channel['subscriberCount'] = self.__subscriberCount
        dict_channel['video_count'] = self.__video_count
        dict_channel['viewCount'] = self.__viewCount
        with open("vdud.json", "w", encoding='utf-8') as write_file:
            json.dump(dict_channel, write_file, indent=4, ensure_ascii=False)

    def __str__(self):
        return f"{self.__title} ({self.__url})"

    def __add__(self, other):
        return int(self.__subscriberCount) + int(other.subscriberCount)

    def __sub__(self, other):
        return int(self.__subscriberCount) - int(other.subscriberCount)

    def __ge__(self, other):
        if int(self.__subscriberCount) >= int(other.subscriberCount):
            return True

    def __gt__(self, other):
        if int(self.__subscriberCount) > int(other.subscriberCount):
            return True