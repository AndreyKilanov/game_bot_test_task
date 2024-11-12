import json
import logging

import requests


class TelegramBot:
    """
    Telegram bot Base class.
    """
    def __init__(self, token):
        self.token = token
        self.url = f'https://api.telegram.org/bot{self.token}/'
        self.offset = None
        self.logger = logging.getLogger("TelegramBot")
        self.logger.setLevel(logging.INFO)

        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        sh = logging.StreamHandler()
        sh.setFormatter(formatter)
        self.logger.addHandler(sh)

    def _keyboard(self, buttons: list[str], resize_keyboard=True) -> dict:
        """
        Метод для добавления клавиатуры.
        resize_keyboard - изменяет размер клавиатуры.
        """
        return {
            'keyboard': [[button] for button in buttons],
            'one_time_keyboard': True,
            'resize_keyboard': resize_keyboard
        }

    def _get_updates(self) -> dict:
        """
        Метод для получения сообщений от пользователя.
        """
        try:
            response = requests.get(f'{self.url}getUpdates', params={'offset': self.offset}).json()
            return response['result']
        except requests.RequestException as e:
            self.logger.error(f'An error occurred while getting updates: {e}')

    def send_message(self, chat_id: int, text: str, reply_markup=None, parse_mode=None):
        """
        Метод для отправки сообщений пользователю.
        reply_markup - клавиатура.
        parse_mode - форматирование текста 'HTML', 'Markdown', 'MarkdownV2'.
        """
        try:
            reply_markup = json.dumps(reply_markup) if reply_markup else None
            requests.post(
                f'{self.url}sendMessage',
                data={
                    'chat_id': chat_id,
                    'text': text,
                    'reply_markup': reply_markup,
                    'parse_mode': parse_mode,
                }
            )
        except requests.RequestException as e:
            self.logger.error(f'An error occurred while sending message: {e}')

    def handler(self, *args, **kwargs):
        """
        Метод для обработки сообщений от пользователя.
        """
        pass

    def start(self):
        """
        Интерфейс для обработки сообщений от пользователя.
        """
        while True:
            try:
                updates = self._get_updates()

                for update in updates:
                    self.offset = update['update_id'] + 1
                    message = update['message']
                    user_id = message['from']['id']
                    text = message.get('text')
                    self.handler(text, message, user_id)

            except Exception as e:
                self.logger.error(f'An error occurred: {e}')
