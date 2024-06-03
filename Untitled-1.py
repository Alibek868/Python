"""
A Simple Vertical Permutation Cipher (SVPC), but complicated.
For example, if the key is 1234, this is a Simple Vertical Cipher in which the text is distributed in 4 columns and 
the ciphertext is obtained by reading through the columns, starting from the 1st, sequentially.
If the key is, for example, 1342, then in this case, as well, the text is distributed in 4 columns, 
BUT the cipher is obtained by reading the columns as follows:
first from the 1st, then from the 3rd, then from the 4th, then from the 2nd.
"""

"""
Простой вертикальный перестановочный шифр (ПВПШ), но усложненный.
Например, если ключ равен 1234, это ПВПШ, в котором текст распределяется в 4 столбца и шифрограмма получается путем считывания по столбцам, начиная с 1-го, последовательно.
Если же ключ равен, например, 1342, то в этом случае тоже текст распределяется в 4 столбца, НО шифрограмма получается путем считывания по столбцам следующим образом:
сначала с 1-го, потом с 3-го, потом с 4-го, потом -- со 2-го.
"""

'''the str_split() function splits a string into characters'''
'''функция str_split() разбивает строку на символы'''
def str_split(seq, length):
    return [seq[i:i + length] for i in range(0, len(seq), length)]

'''the encode() function encrypts the text with a key that determines the number of columns, and prints the encrypted text by reading the characters across the columns'''
'''функция encode() шифрует текст с ключом, определяющим количество столбцов, и печатает зашифрованный текст, читая символы по столбцам'''
def encode(key, plaintext):
    order = {int(val): num for num, val in enumerate(key)}
    ciphertext = 'ыхсринсхсуэизеиулоцыьисфхгелхюкгнуэхэплрифпсхувргефитстэхнлесффскзгхюижсгожсулхп'
    for index in sorted(order.keys()):
        for part in str_split(plaintext, len(key)):
            try:ciphertext += part[order[index]]
            except IndexError:
                continue
    return ciphertext

'''Please implement the decode() function'''
'''Функцию decode() реализуйте сами'''
def decode(key, ciphertext):
    pass

'''Setting the key/Задаем ключ key:'''
key = '3214'

'''Setting the plaintext/Задаем открытый текст'''
Text = 'ьецэльийэдчгусзвсйфхъаоткяёщгуюыибрнмшпждч'

'''Let's add a non-significant text to the last row in the table (add the "$" sign)'''
'''Дополним незначащим текстом последнюю строку в таблице (допишем знак "$")'''
AddTextNum = len(Text) % len(key)
for k in range(AddTextNum):
    Text = Text + '$'
#print ("Plaintext: \n", Text, "\n")

'''We encrypt the plaintext supplemented with special, insignificant, text'''
'''Шифруем открытый текст, дополненный незначащим текстом'''
Encrypted = encode(key, Text)
print("\nCiphertext: \n", Encrypted, "\n")

'''We decrypt the ciphertext'''
'''Расшифруем криптограмму'''
Decrypted = decode(key, Encrypted)

print("Plaintext: \n", Decrypted, "\n")
print("Plaintext in a table form: \n")



