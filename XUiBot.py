import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
import random
randint = random.randint(0, 1000000)
def write_msg(user_id, random_id, message):
    vk_session.method('messages.send', {'user_id': user_id, 'random_id': randint, 'message': message})

vk_session = vk_api.VkApi(token = 'd4457584837a3418117a2cae708cad50d8f2ecd708c6fc56351e24d22d9aeace09e2af75551ce774ce687')
vk_session._auth_token()
vk = vk_session.get_api()
longpoll = VkLongPoll(vk_session)

while true:
    for event in longpoll.listen():
    # Если пришло новое сообщение
        if event.type == VkEventType.MESSAGE_NEW:
    
        # Если оно имеет метку для меня( то есть бота)
            if event.to_me:
        
            # Сообщение от пользователя
                request = event.text
            
            # Каменная логика ответа
                if request == "привет":
                write_msg(event.user_id, randint, "Хай")
                elif request == "пока":
                write_msg(event.user_id, randint, "Пока((")
                else:
                write_msg(event.user_id, randint, "Не поняла вашего ответа...")
