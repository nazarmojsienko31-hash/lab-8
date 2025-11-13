from Functions import uniq_words

#Збір рядків
lines = []
while True:
    s = input("Введіть рядок слів (порожній рядок = завершення циклу): ")
    if s == "":
        break
    lines.append(s) #Якщо рядок не порожній, додаємо його до списку.

#Обробка рядків
result = uniq_words(lines)

#Виведення результату
print("Унікальні слова в одному рядку:")
print(result)