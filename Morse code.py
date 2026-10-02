morse = {"a": "._","b": "_...","c": "_._.","d": "_..","e":".","f":".._.","h":"....","i":"..","j":".___","k":"_._",
"l":"._..","m":"__","n":"_.","o":"___","p":".__.","q":"__._","r":"._.","s":"...","t":"_","u":".._","v":"..._","w":".__",
"x":"_.._","y":"_.__","z":"__..","1":".____","2":"..__..","3":"...__","4":"...._","5":".....","6":"_....","7":"__...",
"8":"___..","9":"____.","0":"_____"}


def encode(text: str):
    s = []
    for i in text:
        for m in morse.keys():
            if i.lower() == m:
                s.append(morse[m])
    return " ".join(s)


def decode(text: str):
    s = []
    for i in text.split():
        for key, value in morse.items():
            if i == value:
                s.append(key)
    return ("".join(s)).capitalize()


def main():
    print("1. зашифровать\n2. расшифровать\n3. выйти\nВыберите действие: ",)
    n = int(input())
    while True:
        match n:
            case 1:
                return encode(input("Введите текст: "))
            case 2:
                return decode(input("Введите текст: "))
            case 3:
                return 0


if __name__ == "__main__":
    print(main())



