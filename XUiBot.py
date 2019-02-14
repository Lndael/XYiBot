import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
import random

def write_msg(user_id, random_id, message):
    vk_session.method('messages.send', {'user_id': user_id, 'random_id': randomint, 'message': message})

vk_session = vk_api.VkApi(token = 'd4457584837a3418117a2cae708cad50d8f2ecd708c6fc56351e24d22d9aeace09e2af75551ce774ce687')
vk_session._auth_token()
vk = vk_session.get_api()
while True:
    
    longpoll = VkLongPoll(vk_session)
    for event in longpoll.listen():
        randomint = random.randint(0, 1000000)
    # Если пришло новое сообщение
        if event.type == VkEventType.MESSAGE_NEW:
    
        # Если оно имеет метку для меня( то есть бота)
            if event.to_me:
                
            # Сообщение от пользователя
                request = event.text
                
                if request == "привет":
                 write_msg(event.user_id, randomint, "Хай")
                elif request == "пока":
                 write_msg(event.user_id, randomint, "Пока(")
                else:
                 write_msg(event.user_id, randomint, "Не понял вашего ответа...")

