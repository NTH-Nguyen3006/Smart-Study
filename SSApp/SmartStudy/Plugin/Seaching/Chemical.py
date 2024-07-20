from ....models import Chemicals, Q

def Elements(_input:str):
    _input = _input.capitalize()
    data = Chemicals.objects.filter(
        Q(symbol_chemical=_input) | Q(name_of_chemical=_input)
    )
    return data

def content(element) -> list | None:
    data = Elements(element.capitalize())
    if data:
        data = data[0]
        content = f'''
- Tên nguyên tố: {data.name_of_chemical}
- Phát hiện bởi: {data.discoverer}
- Nguyên tử khối (A): {data.atomic_mass}
- Số hiệu nguyên tử (Z): {data.id}
- Nhóm: {data.group}
- Chu kì: {data.period} 
- Phân loại: {data.classify}
- Khối lượng riêng: {data.density}
- Nhiệt độ sôi: {data.boil_K}
- Nhiệt độ nóng chảy: {data.melt_K}
- Độ âm điện: {data.electronegativity}
- Thể: {data.plase}
- Phân lớp: {data.block}
- Cấu hình (e): {data.configuration}
- Số oxi hóa: {data.oxidation}
- Hình dạng xuất hiện: {data.appearance}
'''
        image = data.image_URL
        summary = data.summary
        return [content, image, summary]
    return






def Elements(_input) -> list[dict]:
    _input = _input.capitalize()
    # commandDB = f"""
    # SELECT * FROM Chemistry 
    # WHERE Name = '{element}'  
    #     OR Symbol = '{element}' 
    #     OR Phase = '{element}' 
    #     OR Block = '{element}' 
    #     OR Period = '{element}'
    #     OR Groups = '{element}' 
    #     OR Electronegativity = '{element}'
    #     OR Classify = '{element}' 
    #     OR other_classification = '{element}'
    # """
    # data = DataBase(DataBaseName="DataBase/Elements.db").select(
    #     command=commandDB, selectAll=True)
    # if data != []:
    #     result = []
    #     for item in data:
    #         result.append({
    #             "name": item[2], #tên nguyên tố
    #             "symbol": item[3], # kí hiệu nguyên tố
    #             "discovered_by": item[1], # phát hiện bởi
    #             "phase": item[4], # thể (rắn, lỏng, khí)
    #             "classify": item[-2], # phân loại (pk hay kl)
    #             "other_classify": item[-1],
    #             "category": item[5], # loại
    #             "period": item[7], #chu kì
    #             "group": item[8], # nhóm
    #             "block": item[6], # khối (s,p,d hay f)
    #             "configuration": item[9], # cấu hình e
    #             "oxidation": item[-10] and item[-10].split(", "), # các chỉ số oxi hóa
    #             "electronegativity": item[10], # độ âm điện
    #             "density": item[-8], #tỉ trọng đơn vị (kg/m^3)
    #             "atomic_number": item[0], # số hiệu nguyên tử hay còn gọi số proton
    #             "atomic_mass": item[-9], # số khối hạt nhân A
    #             "boil": item[-7], # độ K SÔI
    #             "melt": item[-6], # độ K NÓNG CHẢY/TAN CHẢY 
    #             "appearance": item[-5], # mô tả hình dạng xuất hiện
    #             "summary": item[-4], # kết luận về khí này
    #             "image": item[-3], #ảnh nguyên tố
    #         })
    #     return result
    # return 
    data = Chemicals.objects.filter(
        Q(symbol_chemical=_input) | Q(name_of_chemical=_input)
    )
    return data