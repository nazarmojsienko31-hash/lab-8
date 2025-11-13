#Функція, яка об'єднує всі слова з кількох рядків, видаляючи повтори
def uniq_words(lines):
    words_set = set()
    for line in lines:
        words = line.split()
        words_set.update(words)  #Додавання слів до множини

    #Перетворення множини на рядок
    return " ".join(words_set)