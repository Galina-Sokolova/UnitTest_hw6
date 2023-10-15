while True:
    number = int(input('Enter a whole number greater 1:'))
    if number <= 1:
        print('invalid input, try again')
    else:
        break
for i in range(1, 10):
    for j in range(1, number + 1):
        print(f'{j} * {i:2} = {i * j:2}', end=' ' * 5)
    print()
