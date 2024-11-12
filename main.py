import os

from bot import RockPaperScissorsBot
from dotenv import load_dotenv

load_dotenv()


if __name__ == '__main__':
    token = os.getenv('TOKEN')

    try:
        bot = RockPaperScissorsBot(token)
        bot.start()
    except KeyboardInterrupt:
        pass
    except Exception as e:
        print(e)
