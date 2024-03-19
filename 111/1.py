import re
def process_file(filename):
    with open(filename, 'r') as file:
        data = file.read()
    # Поиск всех целых четных чисел
    numbers = re.findall(r'\b\d+[02468]\b', data)
    sum = 0
    count = 0
    for number in numbers:
        # Поиск последовательности "122" в числе
        sequences_122 = re.findall(r'122', number)
        # Если последовательность встречается минимум 2 раза
        if len(sequences_122) >= 2:
            sum += int(number)  #
            count += 1
    return sum, count

filename = 'text.txt'
sum, count = process_file(filename)

print("Сумма целых  '122':", sum)
print("Количество целых '122':", count)
