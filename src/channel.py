from helper.youtube_api_manual import channel

class Channel:
    """Класс для ютуб-канала"""

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.channel_id = channel_id
        self.channel = channel
        items = channel["items"][0]
        self.id = items["id"]
        self.description = items["snippet"]["description"]
        self.title = items["snippet"]["title"]
        self.url = items["snippet"]["thumbnails"]["default"]["url"]

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        self.channel = channel
        print(self.channel)
