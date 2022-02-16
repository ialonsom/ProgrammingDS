import sys
import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


def exercise1():
    """
    Exercise 1: Write a program which will raise any number x to a positive
    power n using a 'for loop'

    """

    print("\n")
    print("EXERCISE 1")

    # Introduce the number you want to use
    x = int(input("Enter a number: "))
    # Introduce the power to which you want to raise the number
    n = int(input("Enter the power to which you want to raise the number: "))

    # Check if the value of n is positive or negative
    if n>0:
        # Perform the calculation using a for loop for a positive value of n
        power=1
        for i in range(1, n + 1):
            power = power * x
    else:
        power=1
        # Perform the calculation using a for loop for a negative value of n
        for i in range(1, abs(n) + 1):
            power = power * (1/x)


    # Print the result of the calculation
    print( f"The value of {x} to the power of {n} is: {power}")

def exercise2():
    """
    Exercise 2: Create a program for printing
    *
    ***
    *****
    *******
    *********
    """
    print("\n")
    print("EXERCISE 2:")

    n = int(input("Introduce the number of lines: "))

    # Check that the entered number is valid
    if n<0:
        # If the number is negative, the code stops executing and prints an error log.
        logger.error("The number of lines cannot be negative")
        sys.exit()
    # Create a loop to print the pattern
    for i in range(1, n+1):
        print((i*2-1)*'*')

def exercise3():
    """
    Exercise 3: Write a program that calculates the area of a circle from
    the radius. The radius will be an integer read in from the
    keyboard. You will need to use the constant math.pi
    (import math)

    """
    print("\n")
    print("EXERCISE 3:")

    # Import the library math to use the number Pi
    import math

    # Introduce the radius of the circle
    r = int(input("Enter radius of the circle: "))

    # Check that the entered number is valid
    if r<0:
        # If the number is negative, the code stops executing and prints an error log.
        logger.error("The radius cannot be negative")
        sys.exit()

    # Print the area of the circle. We have use the function round to calculate the area using only 4 decimals
    print( f"The area of a circle with a radius of {r} is: {round(math.pi*(r**2), 4)}")

def exercise4():
    """
    Exercise 4: Write an algorithm that asks the users how many numbers
    he/she wants to type. Then read these numbers and print
    out the smallest number, the sum, the average and the
    largest number (watch for possible errors).

    """
    print("\n")
    print("EXERCISE 4:")

    # Introduce how many numbers the user wants to type
    n = int(input("Enter how many numbers you want to type: "))
    numbers = []

    # Check that the entered number is valid
    if n<0:
        # If the number is negative, the code stops executing and prints an error log.
        logger.error("The number cannot be negative")
        sys.exit()

    # Create a loop to enter the numbers that the user has indicated
    for i in range(n):
        number = n = int(input( f"Introduce the value of the number {i+1}: "))
        numbers.append(number)

    # Print the smallest number
    print( f"The smallest number is: {min(numbers)}")

    # Print the sum of the numbers
    print( f"The sum of the numbers is: {sum(numbers)}")

    # Print the average of the numbers. 
    print( f"The average of the numbers is: {round(sum(numbers)/len(numbers), 2)}")

    # Print the largest number
    print( f"The largest number is: {max(numbers)}")

def exercise5():
    """
    Exercise 5: Write a program that asks the user to enter two words. The
    program then prints out both words on one line, the length
    of both words and number of points added. The words will
    be separated by enought dots so that the total line length is
    30

    """
    print("\n")
    print("EXERCISE 5:")

    # Introduce the first word
    word1 = input("Enter the first word: ")

    # Introduce the second word
    word2 = input("Enter the second word: ")

    # Calculate the length of the two words
    words_len = len(word1) + len(word2)
    # Calculate the number of points that have to be added
    num_points = 30-words_len

    # Print the words
    print( f"First word: {word1}")
    print( f"Second word: {word2}")

    # Print out both words on one line, the length of both words and number of points added
    print(word1 + '·'*num_points + word2)

    # Print the lenght of the words and the number of points
    print( f"Length first word : {len(word1)}")
    print( f"Length first word : {len(word2)}")
    print( f"Number of points : {num_points}")

def exercise6():
    """
    Exercise 6: Given a  DNA sequence:
    An imaginary restriction enzyme cuts in "AAGTCA" find
    where in the sequence this enzyme will cut

    """
    print("\n")
    print("EXERCISE 6:")

    import re

    # DNA sequence
    sequence = "AAACGCTGTCAATACAATCTTYCTAGATATTCGGATTTGAATTTTGCAAAAAGTCCGAAGCTGCCCACCTCAAGTCATTGTTTCAACTCGCTTACGGTATATATATCTACTTTCATTGAGATATAAACAGCGCTGATACAATCTTTTTATATAAGTCTTTTGTACAAATAAAGCTAGGAAAAGCCCGACGTCATTATAGCTAT"
    # Where the restriction enzyme cuts
    enzyme = "AAGTCA"

    # Find where the restriction enzyme cuts in the previous sequence
    for cuts in re.finditer(enzyme, sequence):
        print( f"The restriction enzyme sequence is between position {cuts.start()} and {cuts.end()} in the original one")

def exercise7():
    """
    Exercise 7: Given a DNA sequence:
    write a loop that will split the above in triplets
    and print them?

    """
    print("\n")
    print("EXERCISE 7:")

    # DNA sequence
    sequence = "AAACGCTGTCAATACAATCTTYCTAGATATTCGGATTTGAATTTTGCAAAA"

    # Split the DNA sequence in triplets and print it
    for i in range(0, len(sequence), 3):
        print(sequence[i:i+3])
    


def exercise8():
    """
    Exercise 8: Create a program for printing a pyramid of asterisks

    """
    print("\n")
    print("EXERCISE 8:")
    # Introduce the number of rows of the pyramid
    rows = int(input("Enter the number of rows of the pyramid: "))

    # Check that the entered number is valid
    if rows<0:
        # If the number is negative, the code stops executing and prints an error log.
        logger.error("The number of rows cannot be negative")
        sys.exit()
    
    # Create a loop to create the rows
    for i in range(1, rows+1):
        # Print each of the rows
        print(f"{(rows-i)*' '} {'*'*(i*2-1)}")
    




if __name__ == '__main__':

    # Call method for Exercise 1
    exercise1()
    # Call method for Exercise 2
    exercise2()
    # Call method for Exercise 3
    exercise3()
    # Call method for Exercise 4
    exercise4()
    # Call method for Exercise 5
    exercise5()
    # Call method for Exercise 6
    exercise6()
    # Call method for Exercise 7
    exercise7()
    # Call method for Exercise 8
    exercise8()
