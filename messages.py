# main messages

start_msg = 'Привет, <a href="tg://user?id={user_id}">{name}</a>!\n'
start_msg_game = start_msg + 'Давай поиграем в камень-ножницы-бумага!'

# game messages

draw_msg = '<b>Ничья!</b>'
win_msg = '<b>Вы победили!</b>'
lose_msg = '<b>Вы проиграли!</b>'
game_result_msg = 'Вы выбрали {player_choice}<br>Бот выбрал {bot_choice}<br>{result}'
result_msg = 'Вы выбрали {player_choice}, бот выбрал {bot_choice}. {result}'
err_msg = 'Пожалуйста, выберите камень, ножницы или бумагу!'
