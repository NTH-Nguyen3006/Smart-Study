from ....models import Irregular_Verb, Q

def get_IrregularVerb(verb_input):
    listWord = verb_input.split()
    if len(listWord) > 1:
        verb_input = "-".join(listWord)

    data = Irregular_Verb.objects.filter(
        Q(verb1__icontains=verb_input) |
        Q(verb2__icontains=verb_input) |
        Q(verb3__icontains=verb_input)
    )
    return data


def getContent_IrregularVerb(verb_input) -> str:
    data = get_IrregularVerb(verb_input=verb_input)

    if data: 
        return f'''● Động từ bất quy tắc của "{verb_input.title()}" là:
        ☞ V1:  {data[0].verb1}
        ☞ V2:  {data[0].verb2}
        ☞ V3:  {data[0].verb3}
        ☞ Nghĩa:  {data[0].mean}'''
    return