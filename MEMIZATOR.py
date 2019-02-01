def dont_eat_inator(text):
    for i, word in enumerate(text):
        if word.rstrip(".,\"'!?:;1234567890—()«»").endswith("шь"):
            splitted_word = word.partition(word.rstrip(".,\"'!?:;1234567890—()«»"))
            text[i] = splitted_word[1][:-1] + splitted_word[2]
    return text


def suck_inator(text):
    for i, word in enumerate(text):
        if word.rstrip(".,\"'!?:;1234567890—()«»").endswith("ть"):
            splitted_word = word.partition(word.rstrip(".,\"'!?:;1234567890—()«»"))
            text[i] = splitted_word[1][:-1] + "б" + splitted_word[2]
    return text


def mouse_inator(text):
    for i, word in enumerate(text):
        if "ется" in word:
            splitted_word = word.partition("ется")
            text[i] = "(" + splitted_word[0] + "еться" + ")" + splitted_word[2]
            if not i == 0:
                text[i-1] = text[i-1] + ":"
    return text


def olivier_salad_inator(text):
    for i, word in enumerate(text):
        if word.strip(".,\"'!?:;1234567890—()«»").lower() == "хочу":
            text[i] = word.replace("очу", "ачю")
    return text


def main():
    text = input("Введите, пожалуйста, текст для мемизации: ")
    text = text.split()
    text = dont_eat_inator(text)
    text = suck_inator(text)
    text = mouse_inator(text)
    text = olivier_salad_inator(text)
    text = " ".join(text)
    print(text)


if __name__ == '__main__':
    main()
