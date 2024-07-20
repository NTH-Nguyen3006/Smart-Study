from .encode import EncodePython
from django.conf import settings
from ...Action import sendMessage
from .... import fbchat


def encode(thread_id, message_id):
    url = "https://smartstudyai.io.vn/encode"
    fbchat.Reply(
        message_text=f"Vào URL và nhập code hoặc tải lên file code của bạn: {url}",
        thread_id=thread_id,
        message_id=message_id
    )


def get_URL_website(thread_id, message_id):
    url = "https://smartstudyai.io.vn/"
    fbchat.Reply(text=f'Đây là URL Website: {url}', 
                 thread_id= thread_id, message_id=message_id)


def report_error(sender_id, message_error):
    sendMessage(
        sender_id, 
        'Cảm ơn bạn đã báo cáo lỗi cho admin. Xin lỗi bạn về lỗi bạn đã gặp. Chúng tôi sẽ sửa trong thời gian sớm nhất.')
    
    id_admin = [6312817428801561, 6169255926506657]
    for _id in id_admin:
        sendMessage(
            send_to_id=_id, 
            message_text=f'''
◆ Người dùng có id "{sender_id}" vừa báo lỗi.
● Với nội dung như sau: 
    → {message_error}
'''
        )
