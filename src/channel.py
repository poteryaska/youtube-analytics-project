from helper.youtube_api_manual import channel

class Channel:
    """Класс для ютуб-канала"""

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.__channel_id = channel_id
        self.channel = channel
        items = channel["items"][0]
        self.id = items["id"]
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
