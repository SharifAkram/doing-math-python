'''
Even Odd Vending Machine
'''


def even_odd_vending(num):

    if (num % 2) == 0:
        print('Even')
    else:
        print('Odd')
    count = 1
    while count <= 9:
        num += 2
        print(num)
        # increment the count of numbers printed
        count += 1

if __name__ == '__main__':
    try:
        num = float(input('Enter an integer: '))
        if num.is_integer():
            even_odd_vending(int(num))
        else:
            print('Please enter an integer')
    except ValueError:
        print('Please enter a number')