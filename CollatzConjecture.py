"""
Program that calculated the total steps in a collatz conjecture sequence 
given a positive integer n
"""
def CollatzConjecture(n):
    sequence = []
    steps = 0
    while n != 1:
        if n % 2 == 0:
            n /= 2
        else:
            n *= 3
            n += 1
        sequence.append(int(n))
        steps += 1
    return (steps, sequence)

number = int(input("Input an integer greater than 1: "))
collatz = CollatzConjecture(number)
print(f"Total Steps: {collatz[0]} \nCollatz Sequence: {collatz[1]}")

