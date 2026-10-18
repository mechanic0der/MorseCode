import os

en_morse = {"a": "._","b": "_...","c": "_._.","d": "_..","e":".","f":".._.","h":"....","i":"..","j":".___","k":"_._",
"l":"._..","m":"__","n":"_.","o":"___","p":".__.","q":"__._","r":"._.","s":"...","t":"_","u":".._","v":"..._","w":".__",
"x":"_.._","y":"_.__","z":"__..", }

ru_morse = {'а': '.-','б': '-...','в': '.--','г': '--.','д': '-..','е': '.','ё': '.','ж': '...-',
            'з': '--..','и': '..','й': '.---','к': '-.-','л': '.-..','м': '--','н': '-.','о': '---','п': '.--.','р': '.-.','с': '...',
            'т': '-','у': '..-','ф': '..-.','х': '....','ц': '-.-.','ч': '---.','ш': '----','щ': '--.-','ъ': '--.--','ы': '-.--',
            'ь': '-..-','э': '..-..','ю': '..--','я': '.-.-',}

digit_morse = {"1":".____","2":"..__..","3":"...__","4":"...._","5":".....",
               "6":"_....","7":"__...","8":"___..","9":"____.","0":"_____"}


def encode(text: str):
    s = []
    for i in text:
        if i in en_morse.keys():
            s.append(en_morse[i])
        elif i in ru_morse.keys():
            s.append(ru_morse[i])
        elif i in digit_morse.keys():
            s.append(digit_morse[i])
        else:
            s.append(i)
    return " ".join(s)


def decode(letter: str, language: str):
    decode_dict = en_morse
    if language == "ru":
        decode_dict = ru_morse
    for key, value in decode_dict.items():
        if letter == value:
            return key
    for key, value in digit_morse.items():
        if letter == value:
            return key
    return letter


def main():
    user_text = ""
    while True:
        language = 'en'
        language_user_input = input("\n1. На каком языке текст?\n\t1 - Русский\n\t2 - Английский\n\t3. Выйти\n>>> ")
        if language_user_input == '1':
            language = 'ru'
        elif language_user_input == '3':
            break
        user_input_1 = int(input("2. Откуда взять текст?\n\t1 - ввести вручную\n\t2 - прочитать из файла\n>>> "))
        match user_input_1:
            case 1:
                user_text = input("Введите текст: ")
            case 2:
                in_file_name = input("Введите имя файла: ")
                if not os.path.exists(in_file_name):
                    print("Файл не найден")
                    continue
                with open(in_file_name, "r") as file:
                    user_text = file.read()
        user_text = user_text.lower()
        result = ""
        d = int(input("3. Что делаем?\n\tЗашифровать - 1\n\tРасшифровать - 2:\n>>> "))
        match d:
            case 1:
                result = '|'.join(list(map(encode, user_text.split(' '))))
            case 2:
                words = user_text.split('|')
                result = " ".join([
                    ''.join(list(map(lambda s: decode(s, language=language), word.split(' '))))
                    for word in words
                ]).capitalize()
        user_input_2 = int(input("4. Куда вывести результат?\n\t1 - в консоль\n\t2 - сохранить в файл\n>>> "))
        match user_input_2:
            case 1:
                print("Результат: ",result)
            case 2:
                out_file_name: str = input("Введите имя файла: ")
                with open(out_file_name, 'w') as out_file:
                    out_file.write(result)


if __name__ == "__main__":
    main()
