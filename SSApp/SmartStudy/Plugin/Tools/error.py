from ...Action import sendMessage

def error(sender_id, message_text):
    sendMessage(
        sender_id, 
        'Cảm ơn bạn đã gửi báo cáo cho admin. Xin lỗi bạn về lỗi bạn đã gặp. Chúng tôi sẽ sửa trong thời gian sớm nhất.')
    
    id_admin = [6312817428801561, 6169255926506657]
    
    sendMessage(
        id_admin[0], 
        f'◆ Người dùng có id "{sender_id}" vừa báo lỗi.\n● Với nội dung như sau:\n→ {message_text}'
    )
    
    sendMessage(
        id_admin[1], 
        f'◆ Người dùng có id "{sender_id}" vừa báo lỗi.\n● Với nội dung như sau:\n→ {message_text}'
    )