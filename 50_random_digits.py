'''
Create massive of random 50 digits. Assign to list variable.
Print all numbers from list signing them positive/negative values
'''
import random

COUNT = 50

def main():
    x = []
    for num in range(COUNT):
        numbers = random.randint(-100, 100)
        x.append(numbers)
    print(x)

    for digit in x:
        if digit > 0:
            print('Positive:', digit)
        elif digit < 0:
            print('Nagative:', digit)
        else:
            print('Zero is number too:', digit)

if __name__== "__main__":
    main()
