import random
from ..Action import sendMessage
from .utils import Json

def save_user_for_upd(sender_id):
  try:
    sendMessage(sender_id, "SSBot thành thật xin lỗi bạn. Hiện tại Bot đang được admin bảo trì, có thể đang fix Tôi hoặc cập nhật thêm chức năng, quay lại sau nhé .\n\nCập nhật tại: https://www.facebook.com/permalink.php?story_fbid=pfbid02jovq1jP1WRp5VYy89vroxiYGhSh7B449NZFMK48Gb8EfNR8jkueYE9ivSaK5HhB6l&id=100092647046498")
    
    mes = Json().load("Json/save_message.json")
    mes += [sender_id]
    Json().save("Json/save_message.json", mes)
  except Exception as e:
    print(e)
    pass

def run_JsonUser():
  try:
    mes = Json().load("Json/save_message.json")
  
    text = [
      'Bot vừa được admin cập nhật xong, bạn có vấn đề gì để hỏi nhỉ? 😊',
      'Hình như vừa nãy tôi thấy bạn đang thắc mắc gì đó, bạn hỏi lại được không ạ?',
      'Xin lỗi vì đã để bạn đợi lâu, bạn có vấn về thắc mắc gì ạ.',
      'Hi, Bot đã được hoạt động như bình thường, bạn có vấn đề gì ha?',
      'Hé lô, Mình hoạt động bình thường ùi nè, bạn có vấn đề gì hỏi nữa không?',
      "Bot vừa được cập nhật để cải thiện trải nghiệm người dùng, có điều gì bạn muốn biết thêm không?",
      "Thấy bạn còn nhiều câu hỏi, mình ở đây để giúp đỡ. Cần tôi giải đáp thêm điều gì không?",
      "Xin lỗi vì sự chờ đợi. Bây giờ tôi đã sẵn sàng để trợ giúp bạn. Có gì bạn cần tôi giúp không?",
      "Đã đến lúc trò chuyện! Có gì mới hay có thắc mắc gì bạn muốn thảo luận với bot không?",
      "Chào bạn! Bot đã được nâng cấp và sẵn sàng đáp ứng mọi thắc mắc của bạn. Bạn muốn thảo luận về điều gì?",
      "Xin lỗi về sự chậm trễ. Bây giờ mình đã sẵn sàng để giúp đỡ. Bạn có câu hỏi gì cần trợ giúp không?",
      "Chào bạn! Mình đã được cập nhật, có gì mới hoặc có thắc mắc gì bạn muốn chia sẻ với bot không?"
    ]
    
    for userId in list(set(mes)):
      sendMessage(userId, random.choice(text))
    mes = []

    Json().save("Json/save_message.json", mes)

  except Exception as e:
    print("Lỗi ->" ,e)
     
