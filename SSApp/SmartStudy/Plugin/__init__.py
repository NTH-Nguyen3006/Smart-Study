import json
from .AI import *
from .Conversion import *
from .Seaching import * 
from .Tools import *
# from ... import fbchat


commands = {
	'.in4': {
		'name': 'Chemical',
		'func_name': 'element',
		'using': 'Gửi .in4 <tên/kí tự nguyên tố> ',
		'content': 'Tra cứu nguyên tố hóa học',
		'table': 'search'
	},
	'.word': {
		'name': 'Vocabulary',
		'func_name': 'vocabulary',
		'using': 'Gửi .word <từ vựng>',
		'content': 'Tra cứu từ vựng tiếng Anh',
		'table': 'search'
	},
	'.nation': {
		'name': 'Nation',
		'func_name': 'country',
		'using': 'Gửi .nation <quốc gia>',
		'content': 'Tra cứu của một quốc gia',
		'table': 'search'
	},
	'.bqt': {
		'name': 'Irregular Verb',
		'func_name': 'irregularVerb',
		'using': 'Gửi .bqt <động từ>',
		'content': 'Tra cứu động từ bất quy tắc V1 V2 V3',
		'table': 'search'
	},
	'.thoitiet': {
		'name': 'Weather',
		'func_name': 'weather',
		'using': 'Gửi .thoitiet <thành phố>',
		'content': 'Tra cứu thời tiết hiện tại của thành phố',
		'table': 'search'
	},
    
	'.qr': {
		'name': 'QR code',
		'func_name': 'QR_Code',
		'using': 'Gửi .qr <nội dung>',
		'content': 'Chuyển text/url sang QR Code',
		'table': 'conversion'
	},
    '.tomorse': {
        'name': 'Characters to Morse',
		'func_name': 'textToMorse',
		'using': 'Gửi .tomorse <kí tự>',
		'content': 'Chuyển kí tự sang mã Morse',
		'table': 'conversion'
	},
    '.totext': {
        'name': 'Morse/Binary To Text',
		'func_name': 'ToText',
		'using': 'Gửi .totext <nội dung>',
		'content': 'Chuyển nhị phân/morse sang văn bản',
		'table': 'conversion'
	},
    '.tobinary': {
        'name': 'Characters To Binary',
		'func_name': 'ToBinary',
		'using': 'Gửi .tobinary <nội dung>',
		'content': 'Chuyển kí tự/số sang nhị phân',
		'table': 'conversion'
	},
    '.toroman': {
        'name': 'Number To Roman',
		'func_name': 'numToRoman',
		'using': 'Gửi .toroman <số>',
		'content': 'Chuyển số sang La Mã',
		'table': 'conversion'
	},
    '.tonum': {
        'name': 'Binary/Roman To Number',
		'func_name': 'ToNum',
		'using': 'Gửi .tonum <nội dung>',
		'content': 'chuyển (nhị phân/ la mã) sang số',
		'table': 'conversion'
	},
    
    '.encode': {
        'name': 'Encode Python',
		'func_name': 'encode',
		'using': 'Gửi .encode',
		'content': 'Mã hóa code Python',
		'table': 'other'
	},
    
	'.web': {
        'name': 'Website SmartStudy',
		'func_name': 'get_URL_website',
		'using': 'Gửi .web',
		'content': 'Truy cập url website của Bot',
		'table': 'other'
	},
	'play.noitu': {
		'name': 'Connect Word',
		'func_name': 'connect_noitu',
		'using': 'Gửi play.noitu',
		'content': 'Trò chơi nối từ',
		'table': 'other'
	},
	'.help': {
		'name': 'Connect Word',
		'func_name': 'show_commands',
		'using': 'Gửi play.noitu',
		'content': 'Trò chơi nối từ',
		'table': 'other'
	},
	'.change': {
		'name': 'Connect Word',
		'func_name': 'fbchat.change_emoji',
		'using': 'Gửi change <emoji>',
		'content': 'Chuyển biểu tượng cảm xúc của đoạn chat',
		'table': 'other'
	},
}


def show_commands(thread_id, message_id):
	try:
		text = ""
		for cmd, describe in commands.items():
			# if describe['table'] == choice:
				text += f"""
● Cú pháp: {cmd}
- Cách dùng: {describe['using']}
- Công dụng: {describe['content']}
"""
				
		fbchat.Reply(text=text, thread_id=thread_id, message_id=message_id)
	except Exception as e:
			print(e)

	

