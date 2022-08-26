import json
def hint(num):
    num = str(num)
    file = open('Hints/hint_messages.json')
    hint_messages = json.load(file)
    file.close()
    try:
        message = hint_messages[num]
    except:
        message = "Hints unavailable"
    print(message)