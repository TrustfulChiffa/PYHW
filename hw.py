# Задача 34:  Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. 
# Поскольку разобраться в его кричалках не настолько просто, насколько легко он их придумывает, Вам стоит написать программу. 
# Винни-Пух считает, что ритм есть, если число слогов (т.е. число гласных букв) в каждой фразе стихотворения одинаковое. 
# Фраза может состоять из одного слова, если во фразе несколько слов, то они разделяются дефисами. 
# Фразы отделяются друг от друга пробелами. Стихотворение  Винни-Пух вбивает в программу с клавиатуры. 
# В ответе напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, если с ритмом все не в порядке

# *Пример:*

# **Ввод:** пара-ра-рам рам-пам-папам па-ра-па-да    
#     **Вывод:** Парам пам-пам  

def check_rhythm(poem):
    lines = poem.split()
    syllable_counts = []

    for line in lines:
        words = line.split('-')
        syllables = sum(count_syllables(word) for word in words)
        syllable_counts.append(syllables)

    if all(count == syllable_counts[0] for count in syllable_counts):
        return "Парам пам-пам"
    else:
        return "Пам парам"

def count_syllables(word):
    vowels = "AEIOUYaeiouy"
    count = 0

    if word[0] in vowels:
        count += 1

    for index in range(1, len(word)):
        if word[index] in vowels and word[index - 1] not in vowels:
            count += 1

    if word.endswith("e") and word[-2] not in vowels:
        count -= 1

    return count

poem = input("Введите стихотворение Винни-Пуха: ")
result = check_rhythm(poem)
print(result)