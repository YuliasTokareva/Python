line = input("Введите строку: ")

result = line.replace('a', '').replace('e', '').replace('i', '').replace('o', '').replace('u', '') \
             .replace('A', '').replace('E', '').replace('I', '').replace('O', '').replace('U', '')

print("Строка без гласных:", result)