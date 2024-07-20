import requests

def countries(nation) -> dict: 
    try:
        from unidecode import unidecode
        nation = unidecode(nation).lower()
        # sửa lại từ viet nam nếu người dùng nhập không đúng
        nation = nation if nation.lower() != "viet nam" else "vietnam"
        countries = requests.get("http://country.io/names.json").json()
        for code in countries:
            if nation.lower() == countries[code].lower():
                nationCode = code.lower()

        try: # khi tên quốc gia sai, phía dưới có kết quả gì thì bot sẽ không in ra
            phoneCodeAPI = requests.get("http://country.io/phone.json").json()
            currency_api = requests.get(f'http://country.io/currency.json').json()
            phone_code = phoneCodeAPI.get(nationCode.upper())
            currency = currency_api.get(nationCode.upper())
        except:
            return #lỗi
        api = requests.get(f'https://restcountries.com/v3.1/alpha/{nationCode}').json()

        nationName = api[0]["name"]["common"]
        capitain = api[0]["capital"][0]
        code_cca2 = api[0]["cca2"]
        acreage = "{:,.3f}".format(api[0]["area"])
        timezones = api[0]["timezones"][0]
        currency_name = api[0]["currencies"][currency]["name"]
        currency_symbol =  api[0]["currencies"][currency]["symbol"]
        
        dic_region = {"Europe": "Châu Âu", "Americas": "Châu Mỹ", "Antarctic": "Châu Nam Cực", "Africa": "Châu phi", "Asia": "Châu Á", "Oceania": "Châu Đại Dương"}
        region = dic_region.get(api[0]["region"])
        
        urlMap = api[0]["maps"]["googleMaps"] # chỗ này sẽ đưa ra link ggmap
        flag = api[0]["flags"]["png"] # link ảnh

        data = {
            'name': nationName,
            'urlFlag': flag, #url
            'cca2': code_cca2, #mã code 1 quốc gia
            'region': region,
            'caption': capitain,
            'acreage': acreage,
            'timezones': timezones,
            'currency': currency_name,
            'currency_symbol': currency_symbol,
            'phone_code': phone_code,
            'UrlMap': urlMap,
            'flag': flag
        }
        return data
    except Exception as e:
        import traceback, sys
        name_error = str(sys.exc_info()[1])
        tb = sys.exc_info()[2]
        line_number = traceback.extract_tb(tb)[-1][1]
        print(f"""ĐÃ CÓ LỖI XÃY RA!!!
        Tên Lỗi: {name_error}
        
        Tên file: {__name__} | Vị trí dòng thứ: {line_number}
        """)
        return

def getContent(nation) -> list:
    data = countries(nation=nation)
    if not data:
        return
    
    content: str = f'''Đây là thông tin của {nation.title()}:
    - Tên quốc gia: {data['name']}
    - Quốc gia (cca2): {data['cca2']}
    - Khu vực: {data['region']}
    - Thủ đô: {data['caption']}
    - Diện tích: {data['acreage']} km²
    - Múi giờ: {data['timezones']}
    - Tiền tệ (tên): {data['currency']}
    - Kí hiệu tiền tệ: {data['currency_symbol']}
    - Mã số thuê bao: {data['phone_code']}
    - Vị trí trên bản đồ (url): {data['UrlMap']} '''
    flagUrlImage = data['flag']
    
    return [content, flagUrlImage]