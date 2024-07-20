from ..Action import sendMessage
from ..Sundry import Json, run_JsonUser

def on_block_user_on_update(admin_id):
  try:
    tool = Json().load("Json/tools.json") or {}
    tool["update_bot"] = True
    Json().save("Json/tools.json", tool)
    sendMessage(admin_id, "Bật CĐ update Bot thành công. admin Minh Tuấn, Hoàng Nguyên, Khang Phan")
  except:
    sendMessage(admin_id, "Bật chế độ update Bot không thành công")


def off_block_user_on_update(admin_id): 
  try:
    tool = Json().load("Json/tools.json") or {}
    tool["update_bot"] = False
    Json().save("Json/tools.json", tool)
    sendMessage(admin_id, "Tắt CĐ update Bot thành công")

    run_JsonUser()

  except:
    sendMessage(admin_id, "Tắt chế độ update Bot không thành công")

  
