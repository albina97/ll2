from random import randint as rand

print('==== Задание 2: Метод одноразового блокнота ====')
print('==== Шифрование сообщения на русском языке =====')
original = input('Введите исходное сообщение: ')

#Генерирование псевдослучайного ключа
def keygen(key):
    for i in range(len(original)):
        key += alpha[rand(0, 33)]
    return key

#Преобразование русских букв в буквы нижнего регистра
def lower(text):
    new_text = ''
    for i in text:
        if i in alphaUpper:
            for j in range(33):
                if i == alphaUpper[j]:
                    new_text += alpha[j]
        else:
            new_text += i            
    return new_text

#Применение метода одноразового блокнота
def xor(message, key, mode):
    result = ''
    index_mes, index_key = 0, 0
    for i in range(len(message)):
        #Проверяем наличие буквы в русском алфавите
        if message[i] in alpha:
            index_mes = alpha.index(message[i])
            index_key = alpha.index(key[i])
            result += alpha[(index_mes + mode * index_key) % 33]
        #В режиме дешифрования меняем латинскую a на пробел
        elif message[i] == chr(97):
            result += ' '
        #Если в сообщении встречается пробел, заменяем его на латинскую a
        else:
            result += chr(97)
    return result

alpha = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
alphaUpper = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'

key = ''
key = keygen(key)
print('Сгенерирован псевдослучайный ключ: ' + key)

code = xor(lower(original), key, 1)
print('Зашифрованное сообщение: ' + code)

original = xor(code, key, -1)
print('Восстановленное сообщение: ' + original)
