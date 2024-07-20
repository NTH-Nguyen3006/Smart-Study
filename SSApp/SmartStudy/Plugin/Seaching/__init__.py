from .Chemical import *
from .IrregularVerb import getContent_IrregularVerb
from .EngWord import *
from .Nation import *
from .Weather import *
from ...Action import sendMessage, sendMedia

#__all__ = ['element', 'vocabulary', 'country', 'irregularVerb', 'weather']

def element(send_to_id, element) -> None:
    data: list|None = Chemical.content(element=element)
    if data:
        content = data[0]
        image = data[1]
        summary = data[-1]
        sendMessage(send_to_id=send_to_id, message_text=content)
        sendMedia(send_to_id, 'image', image)  
        sendMessage(send_to_id, summary)
    else: 
        sendMessage(send_to_id, 'Có thể nguyên tố này không có trong bảng tuần hoàn hóa học, bạn hãy nhập lại đúng tên nguyên tố nhé!')

def vocabulary(send_to_id, word) -> None:
    data: list = EngWord.content(word=word)
    for content in data:
        sendMessage(send_to_id, content)

def country(send_to_id, nation) -> None: 
    sendMessage(send_to_id, 'Đang xử lý...')
    data = Nation.getContent(nation=nation)
    if data: 
        content = data[0]
        flagUrlImage = data[1]
        sendMessage(send_to_id, f'Đây là cờ của nước {nation.title()}')
        
        sendMedia(send_to_id, "image", str(flagUrlImage))
        sendMessage(send_to_id, content)
    else: 
        sendMessage(send_to_id, "Có vẻ bạn nhập không đúng tên của 1 quốc gia")

def irregularVerb(send_to_id, verb) -> None:
    content = getContent_IrregularVerb(verb_input=verb)
    if content:
        sendMessage(send_to_id, content)
    else:
        sendMessage(send_to_id, f'Có thể từ *{verb}* không có trong dữ liệu động từ bất quy tắt.')

def weather(send_to_id, city) -> None:
    content = Weather.content(city=city)
    if content:
        sendMessage(send_to_id, content)
    else: 
        sendMessage(send_to_id, 'Có vẻ bạn nhập tên thành phố không đúng. Hãy nhập lại.')

