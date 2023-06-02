import vk as vk
import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.utils import get_random_id

session = vk_api.VkApi(token='vk1.a.mvd-lcDrY37nLK0QA5hid_T3lfK3mmhIbEjSZ8QQKpwx8fLtLCTKT5JOJJYdRA4TTEiiBy1utPe5OgQmnKpFJ4e4PKgfH60Rs7VPW6kB9rk0V36sj3NwxLu8DQZUzSoHBWUxoviKbE93u4MlHecUtsuvXYDbM4hF5T_i8PclivariqZv5142nXElJ8Gd366sYSR1Kfj5d_LZ-8y9lmpNaQ')

def send_message(user_id, message):
    session.method("messages.send",{ #Обращаемся к методу method  и к методу messages.send, передаем данные (user_id, message)
        "user_id": user_id,
        "message": message,
        "random_id": get_random_id()
    })



for event in VkLongPoll(session).listen(): #Перебираем объекты событий в этом классе
    if event.type == VkEventType.MESSAGE_NEW and event.to_me: #Если полученое сообщение адресовано к боту, то выполняем
        text = event.text.lower() #Переводим текст в нижний регистр (чтобы не мучаться с регистром)
        user_id = event.user_id # Записываем id пользователя
        user_info = session.method("users.get", {"user_ids": user_id})
        user_name = user_info[0]["first_name"]  #Получение имени пользователя

        if text == "привет":
            send_message(user_id,"Привет, " + user_name) 

