class MissingValueException(Exception):
    """Создаем свое исключения при отсутствии переменных окружения."""


class GetAPIException(Exception):
    """Создаем свое исключение при сбое запроса к API отправки сообщений."""