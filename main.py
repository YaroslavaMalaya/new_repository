def conversion_to_binary(number):              # переведення в двійкове
    NUMBER = 2
    remainder = int(number) % NUMBER                # остача
    integer = int(number) // NUMBER                 # ціла частина
    x = [remainder]
    while integer != 0:
        remainder = integer % NUMBER
        integer //= NUMBER
        x.insert(0, remainder)                   # зберігти елемнт на початку списка
    print(f'This is 0b{"".join(map(str, x))}')  # об'єдную усі елементи як стрінг в списку і прінчу


def conversion_to_decimal(number):               # переведення в десяткове
    decimal_number = 0
    binary_number = number.split('b')[-1]
    len_number = len(str(binary_number))
    for i in range(0, len_number):
        decimal_number += int(binary_number[i]) * (2 ** (int(len_number) - i - 1))
    print(f'This is {decimal_number}')


def transformation():
    number = input('Enter your number: ')
    if number[:2] == '0b':
        conversion_to_decimal(number)
    else:
        conversion_to_binary(number)


transformation()
answer = input('Do you wanna continue? ')
while True:
    if answer.lower() == 'yes':
        transformation()
        answer = input('Do you wanna continue? ')
    elif answer.lower() == 'no':
        print('Ok, goodbye.')
        break
