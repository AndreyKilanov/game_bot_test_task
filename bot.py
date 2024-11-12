import random

from core import TelegramBot
from keyboard import keyboard, keys
from messages import *


class RockPaperScissorsBot(TelegramBot):

    def handle_result_game(self, chat_id, button):
        if button in keyboard:
            self.play_game(chat_id, button)
        else:
            self.send_message(chat_id, err_msg)

    def play_game(self, chat_id, player_choice):
        choices = keyboard
        bot_choice = random.choice(choices)

        match (player_choice, bot_choice):
            case (keys.rock, keys.rock) | (keys.scissors, keys.scissors) | (keys.paper, keys.paper):
                result = draw_msg
            case (keys.rock, keys.scissors) | (keys.scissors, keys.paper) | (keys.paper, keys.rock):
                result = win_msg
            case _:
                result = lose_msg

        self.send_message(
            chat_id,
            result_msg.format(player_choice=player_choice, bot_choice=bot_choice, result=result),
            reply_markup=self._keyboard(keyboard),
            parse_mode='HTML'
        )

    def handler(self, text: str, message: dict, user_id: int):
        if text.lower() == '/start':
            name = message["from"]["first_name"]
            msg = start_msg_game.format(user_id=user_id, name=name)
            buttons = self._keyboard(keyboard)
            self.send_message(user_id, msg, buttons, 'HTML')
        else:
            self.handle_result_game(user_id, text)
