def IsValid(number):
    """
    Checks if a credit card number is valid using Luhn's algorithm
    """
    number = str(number)
    number = list(number)
    for i in range(0, len(number), 2):
        number[i] = str(int(number[i]) * 2)
    checksum = ''.join(number)
    checksum = list(checksum)
    final = [int(i) for i in checksum]
    if sum(final) % 10 == 0:
        return "Valid"
    else:
        return "Invalid"


number = input("Input card number: \n")
print(f"The card ending in {number[-4:]} is {IsValid(number)}")

