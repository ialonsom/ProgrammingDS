from random import randint
from xmlrpc.client import boolean
import logging
import string

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


class Film:
 
    # Initializer / Instance Attributes
    def __init__ (self, title: str, duration: int, min_age: int, director: str, price: float) -> None :
        self.title = title
        self.duration = duration
        self.min_age = min_age
        self.director = director
        self.price = price

class Spectator:
 
    # Initializer / Instance Attributes
    def __init__ (self, id: int, age: int, available_money: float) -> None :
        self.id = id
        self.age = age
        self.available_money = available_money

class Seat:
 
    # Initializer / Instance Attributes
    def __init__ (self, row: int, column: str, free: boolean, spectator_id: int) -> None :
        self.seat = [row, column]
        self.free = free
        self.spectator_id = spectator_id
    
    def ocupateSeat(self, spectator_id):
        """
        This method occupies the spectator on the seat. For that, it changes
        the status to 'not free' and save the spectator id

        """
        # Change the variable free to False
        self.free = False
        # Save the spectator id
        self.spectator_id = spectator_id


class Cinema:

    # Initializer / Instance Attributes
    def __init__ (self, num_rows: int, num_cols: int, film_shown: Film) -> None :

        # The maximum
        if num_rows > 10:
            logger.error(f"This cinema only has rooms with 9 rows maximum. Please, indicate another number of rows")
        else:
            self.num_rows = num_rows
            self.num_cols = num_cols
            self.film_shown = film_shown
            # Create the seats of the cinema
            self.list_seats = self.createSeats()

    def createSeats(self):

        """
        This method creates all the cinema seats

        """

        # Define an empty list with the size of the cinema
        list_seats = [[0 for x in range(self.num_cols)] for y in range(self.num_rows)]
        # Define a list with the alphabet to create the columns of the seats
        alphabet = string.ascii_uppercase

        # Create a loop to go through the rows of the cinema
        for i in range(self.num_rows):
            # Create a loop to go through the columns of each row of the cinema
            for j in range(self.num_cols):
                # For every seat (row, column) create a new seat as free and with an empty spectator id
                list_seats[i][j] =  Seat(i, alphabet[j], True, "")
        return list_seats

    def availableSeats(self):
        """
        This method checks if there is any seat available in the cinema

        """
        list_seats = self.list_seats
        # Create a loop to check if there are available seats
        for i in range(len(list_seats)):
            for j in range(len(list_seats[0])):
                # If there are at least one free seat, return True
                if (list_seats[i][j].free):
                    return True

        return False
    
    def allocateSpectators(self, spectatorList):

        """
        This method allocates a list of spectators according to the following conditions:
            - A spectator will be seated if: there are available seats, has
            enough money and has a proper age for the film
            - Seats must be assigned to spectators randomly

        """

        # Create a loop to allocate each spectator of the list
        for i in spectatorList:

            # Check if there are available seats
            available_seats = self.availableSeats()

            if (not available_seats):
                logger.error("There are not enough seats available")

                # If there are not enough sites we break the loop because we cannot allocate more spectators
                break

            canWatch=True
            # Check if the spectator has has enough money
            if(i.available_money < self.film_shown.price):
                logger.error(f"The spectator {i.id} has not enough money to watch this movie")
                # If the spectator does not have enough money we change the value of the variable canWatch to False
                canWatch=False

            # Check if the spectator has a proper age for the film
            if(i.age < self.film_shown.min_age):
                logger.error(f"The spectator {i.id} is not old enough to watch this movie")
                # If the spectator does not have enough age we change the value of the variable canWatch to False
                canWatch=False

            isFree = True
            # We create a while to allocate the spectator but only if he/she is able to whatch the film
            while(isFree&canWatch):
                # We select a random row and a random column
                row = randint(0, self.num_rows-1)
                col = randint(0, self.num_cols-1)
                # We check if the seat is free. If it is free we allocate the spectator, if it is not we try with another seat
                if(self.list_seats[row][col].free):
                    # Call the method 'ocupateSeat' to allocate the spectator in the specific seat
                    self.list_seats[row][col].ocupateSeat(i.id)
                    print(f"The spectator {i.id} has been alocated in the {row} row and column { self.list_seats[row][col].seat[1]}")
                    break
            
    def getAllocatedSpectators(self):

        """
        The method does not receive arguments and returns the list of those spectators that
        fulfilled the conditions to be seated

        """

        # Define the list of seats and the list of spectators
        list_seats = self.list_seats
        list_spectators = []

        # Create a loop to check the seats that are ocupated
        for i in range(len(list_seats)):
            for j in range(len(list_seats[0])):
                # Check if the seat is ocupated
                if (not list_seats[i][j].free):
                    # Add the id of the spectator to the list
                    list_spectators.append(list_seats[i][j].spectator_id)

        return list_spectators
    
    def showSeats(self):
        """
        This method displays the occupancy of the seats

        """
        
        row = ""
        print("\n")
        # Print the header
        print(12*self.num_cols*"#"+ "\n" + 
        "#" + (6*self.num_cols-4)*" " + "SCREEN" + (6*self.num_cols-4)*" " + "#" + "\n" 
        + 12*self.num_cols*"#" + "\n")

        # Create a loop to go through the rows of the cinema
        for i in range(len(self.list_seats)):
            # Create a loop to go through the columns of each row of the cinema
            for j in range(len(self.list_seats[0])):
                # Check if the seat is free
                if (self.list_seats[i][j].free == False):
                    # If the seat is not free we represent the seat as [*S ,*number ]
                    if(len(str(self.list_seats[i][j].spectator_id)) == 1):
                        row = row + f"[ *S,  *{self.list_seats[i][j].spectator_id} ] "
                    if (len(str(self.list_seats[i][j].spectator_id)) == 2):
                        row = row + f"[ *S,  *{self.list_seats[i][j].spectator_id}] "
                else:
                    # If the seat is free we represent the seat as [row,column]
                    row = row + f"[  {self.list_seats[i][j].seat[0]},    {self.list_seats[i][j].seat[1]}] "
            print(" "+ row)
            row = ""

    def getSeats(self):
        """
        The method does not receive any argument and returns a
        list of objects of type Seat with all seats in the cinema

        """

        return self.list_seats


if __name__ == '__main__':

    # Create films
    peterPan = Film("Peter Pan", 53, 5, "P.J Hogan", 12)
    blancanieves = Film("Blancanieves", 23, 10, "David Hand", 7)
    mulan = Film("Mulan", 115, 12, "Niki Caro", 12)

    # Create cinemas
    cinema1 = Cinema(10, 10, peterPan)
    cinema2 = Cinema(10, 5, blancanieves)
    cinema3 = Cinema(8, 7, mulan)
    
    num_spectators = int(input("How many spectators do you want to enter: "))

    list_spectators = []

    for i in range(num_spectators):
        # Insert the spectator
        print(f"Creating the spectator number {i+1}")
        id = int(input("Id of the spectator: "))
        age = int(input("Age of the spectator: "))
        available_money = int(input("Available money: "))
        # Create a new spectator
        spectator = Spectator(id, age, available_money)
        # Save the spectator in the list of spectators
        list_spectators.append(spectator)
        
    # Call method to allocate the spectator
    cinema1.allocateSpectators(list_spectators)

    # Call the method to see all the allocated spectators
    print("List the spectators that have been allocated: \n", cinema1.getAllocatedSpectators())

    # Call the method for displaying occupancy
    cinema1.showSeats()
