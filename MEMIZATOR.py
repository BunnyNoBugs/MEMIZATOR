def suck_inator(text):
    for i, word in enumerate(text):
        if word.rstrip(".,\"'!?:;1234567890—()«»").endswith("шь"):
            splitted_word = word.partition("ется")
            text[i] = "(" + splitted_word[0] + "еться" + ")" + splitted_word[2]
            text[i-1] = text[i-1] + ":"
    text = " ".join(text)


def mouse_inator(text):
    for i, word in enumerate(text):
        if not i == 0:
            if "ется" in word:
                splitted_word = word.partition("ется")
                text[i] = "(" + splitted_word[0] + "еться" + ")" + splitted_word[2]
                text[i-1] = text[i-1] + ":"
    text = " ".join(text)
    return text


def main():
    text = input("Введите, пожалуйста, текст для мышезации: ")
    text = text.split()
    print(mouse_inator(text))


if __name__ == '__main__':
    main()