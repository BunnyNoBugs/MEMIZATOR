def donteat_inator(text):
    for i, word in enumerate(text):
        if word.rstrip(".,\"'!?:;1234567890—()«»").endswith("шь"):
            splitted_word = word.partition(word.rstrip(".,\"'!?:;1234567890—()«»"))
            text[i] = splitted_word[1][:-1] + splitted_word[2]
    return text


def mouse_inator(text):
    for i, word in enumerate(text):
        if not i == 0:
            if "ется" in word:
                splitted_word = word.partition("ется")
                text[i] = "(" + splitted_word[0] + "еться" + ")" + splitted_word[2]
                text[i-1] = text[i-1] + ":"
    return text


def main():
    text = input("Введите, пожалуйста, текст для мемизации: ")
    text = text.split()
    text = donteat_inator(text)
    text = mouse_inator(text)
    text = " ".join(text)
    print(text)


if __name__ == '__main__':
    main()
