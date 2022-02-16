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
