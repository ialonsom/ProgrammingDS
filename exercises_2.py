def exercise1():

    """
    Exercise 1: Write an algorithm that given the following list of integers
    a = [12,67,1,89,3,0,100,23,65,34,64,98,12,27]
    counts the number of integers below '11' and returns a
    sublist of those elements that are less than half of the
    average of the elements in the list.

    """

    print("\n")
    print("EXERCISE 1")

    # Declare the list of integers
    a = [12,67,1,89,3,0,100,23,65,34,64,98,12,27]

    # Filter all elements bellow 11
    numbers = [x for x in a if x<11]

    # Calculate the average of the numbers that are bellow 11
    avg = sum(numbers)/len(numbers)

    # Store in a list the numbers of those elements that are less than half of the
    # average of the elements in the list.
    numbers_bellow_avg = [x for x in numbers if x<(avg/2)]

    # Print the result
    print("List of numbers: ",numbers_bellow_avg)

def exercise2():
    """
    Exercise 2:
        Write an algorithm that:
        1. Prints the names of the miRNAs (-mir-) with gene copy
        number values exceeding the average copy number value
        for all the genes.
        2. Prints the names of the miRNA genes with 0 copy numbers
        3. Prints what is the value of the highest copy number for all
        the genes
        4. Constructs a dictionary gene_name -> gene_copy_number

    """

    print("\n")
    print("EXERCISE 2")

    # Declare the list of names and their corresponding gene names
    gene_copy_numbers = [32,3,5,12,45,23,88,1,8,5,10,0,32,0,88]
    gene_names = ["has-let-7a","has-mir-9" ,"has-mir-121" ,"has-mir-23",
    "has-mir-19", "has-mir-221", "has-mir-89" , "has-mir-1034", "has-mir-12",
    "has-mir-2088", "has-mir-56" , "has-mir-55a" , "has-mir-55b" ,
    "has-mir-127", "has-mir-17"]

    ###### FIRST POINT ######

    # Calculate the average ofall the numbers
    avg = sum(gene_copy_numbers)/len(gene_copy_numbers)

    # Filter the mirRNAs
    gene_names_first, gene_copy_numbers_first = zip(*((gene_names, gene_copy_numbers) for gene_names, gene_copy_numbers in zip(gene_names, gene_copy_numbers) if ('-mir-' in gene_names) and (gene_copy_numbers > avg)))
    
    print("Numbers filtered: ", gene_copy_numbers_first)
    print("Name of the numbers filtered: ", gene_names_first)

    ###### SECOND POINT ######

    # Filter the mirRNAs
    gene_names_sec, gene_copy_numbers_sec = zip(*((gene_names, gene_copy_numbers) for gene_names, gene_copy_numbers in zip(gene_names, gene_copy_numbers) if ('-mir-' in gene_names) and (gene_copy_numbers == 0)))
    
    print("Numbers filtered: ", gene_names_sec)
    print("Name of the numbers filtered: ", gene_copy_numbers_sec)

    ###### THIRD POINT ######
    
    for highest in range(0, len(gene_copy_numbers)):
        if gene_copy_numbers[highest] == max(gene_copy_numbers):
            print(gene_copy_numbers[highest], gene_names[highest])


    ###### FOURTH POINT ######

    genes_dictionary = []

    for i in range(len(gene_names)):
        gene = {
            "name": gene_names[i],
            "number": gene_copy_numbers[i]
        }
        genes_dictionary.append(gene)
    
    print("Dictionary of the names and numbers of the genes", genes_dictionary)

def exercise3():
    print("\n")
    print("EXERCISE 3")

    # Aqui va el ejercicio 3


def exercise4():

    """
    Exercise 4:
    Using reviewed Python Data Structures:
        - Implement a binary tree as the one in the figure
        - Create 'statically' one as in the figure
        - Define a function for 'pretty printing'
    Notes:
        - Simply design and implement the tree
        - Forget about tree ops. for the moment ...
    """

    print("\n")
    print("EXERCISE 4")

    class Tree:
 
        def __init__(self, value=None, left=None, right=None):
    
            self.left = left
            self.right = right
            self.value = value
    
        def PrintTree(self):
            print(self.value)
            if self.left:
                self.left.PrintTree()
            if self.right:
                self.right.PrintTree()
    root = Tree(3)
    root.left = Tree(2)
    root.right = Tree(1)
    root.left.left = Tree(5)
    root.left.right = Tree(4)
    root.right.right = Tree(6)
    
    root.PrintTree()


















def exercise1dfdfd():
    """
    Exercise 1: Write a program which will raise any number x to a positive
    power n using a 'for loop'

    """
    print("EXERCISE 1")

    # Introduce the number you want to use
    x = int(input("Enter a number: "))
    # Introduce the power to which you want to raise the number
    n = int(input("Enter the power to which you want to raise the number: "))

    # Print the result of the calculation
    print( f"The value of {x} to the power of {n} is: {x**n}")

def exercise2ihjhjhk():
    """
    Exercise 2: Write a program for printing n rows that contains
    the same number of asterisks as the number of the row.

    """
    print("EXERCISE 2:")

    # Introduce the number of rows that you want to create
    rows = int(input("Enter number of rows for Exercise 2: "))

    # Create a loop that prints the n number of rows
    for i in range(1, rows+1):

        # Print the asterisks for each row by multiplying by the number of the row
        print("*"*i)

def exercise3ddd():
    """
    Exercise 3: Write a program that calculates the area of a circle from
    the radius. The radius will be an integer read in from the
    keyboard. You will need to use the constant math.pi
    (import math)

    """

    print("EXERCISE 3:")

    # Import the library math to use the number Pi
    import math

    # Introduce the radius of the circle
    r = int(input("Enter radius of the circle: "))

    # Print the area of the circle. We have use the function round to calculate the area using only 4 decimals
    print( f"The area of a circle with a radius of {r} is: {round(math.pi*(r**2), 4)}")

def exercise4dddddddd():
    """
    Exercise 4: Write an algorithm that asks the users how many numbers
    he/she wants to type. Then read these numbers and print
    out the smallest number, the sum, the average and the
    largest number (watch for possible errors).

    """

    print("EXERCISE 4:")

    # Introduce how many numbers the user wants to type
    n = int(input("Enter how many numbers you want to type: "))
    numbers = []

    # Create a loop to enter the numbers that the user has indicated
    for i in range(n):
        number = n = int(input( f"Introduce the value of the number {i+1}: "))
        numbers.append(number)


    # Print the smallest number
    print( f"The smallest number is: {min(numbers)}")

    # Print the sum of the numbers
    print( f"The sum of the numbers is: {sum(numbers)}")

    # Print the average of the numbers. We have use the function round to calculate the area using only 2 decimals
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

    print("EXERCISE 7:")

    import re

    # DNA sequence
    sequence = "AAACGCTGTCAATACAATCTTYCTAGATATTCGGATTTGAATTTTGCAAAA"

    # Split the DNA sequence in triplets and print it

    print(re.findall(r'.{1,3}',sequence,re.DOTALL))
    


def exercise8():
    """
    Exercise 8: Create a program for printing a pyramid of asterisks

    """

    print("EXERCISE 8:")
    # Introduce the number of rows of the pyramid
    rows = int(input("Enter the number of rows of the pyramid: "))
    
    # Create a loop to create the rows
    for i in range(1, rows+1):
        # Print each of the rows
        print(f"{(rows-i)*' '} {'*'*(i*2-1)}")
    




if __name__ == '__main__':

    # Call method for Exercise 1
    exercise4()
    # Call method for Exercise 2
    # exercise2()
    # # Call method for Exercise 3
    # exercise3()
    # # Call method for Exercise 4
    # exercise4()
    # # Call method for Exercise 5
    # exercise5()
    # # Call method for Exercise 6
    # exercise6()
    # # Call method for Exercise 7
    # exercise7()
    # # Call method for Exercise 8
    # exercise8()
