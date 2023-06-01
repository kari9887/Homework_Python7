def word(words):
    str = words.lower().split()
    a = lambda x: sum(1 for i in x if i in "аоуыэеёиюя")
    temp = a(str[0])
    if all([a(i) == temp for i in str]):
        return 'Парам пам-пам'
    else :
        return 'Пам парам'


print(word("Хорошо-живет-на-свете-Винни-Пух!} "))
