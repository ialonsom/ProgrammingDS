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
        self.free = False
        self.spectator_id = spectator_id


class Cinema:

    # Initializer / Instance Attributes
    def __init__ (self, num_rows: int, num_cols: int, film_shown: Film) -> None :
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.film_shown = film_shown
        self.list_seats = self.createSeats()

    def createSeats(self):

        # Define an empty list with the size of the cinema
        list_seats = [[0 for x in range(self.num_cols)] for y in range(self.num_rows)]
        # Define a list with the alphabet to create the columns of the seats
        alphabet = string.ascii_uppercase

        for i in range(self.num_rows):
            for j in range(self.num_cols):
                list_seats[i][j] =  Seat(i, alphabet[j], True, "")
        return list_seats

    def availableSeats(self):
        list_seats = self.list_seats
        # Create a loop to check if there are available seats
        for i in range(len(list_seats)):
            for j in range(len(list_seats[0])):
                # If there are at least one free seat, return True
                if (list_seats[i][j].free):
                    return True

        return False
    
    def allocateSpectators(self, spectatorList):

        # Create a loop to allocate each spectator of the list
        for i in spectatorList:

            # Check if there are available seats
            available_seats = self.availableSeats()

            if (not available_seats):
                logger.error("There are not enough sites available")

                # If there are not enough sites we break the loop because we cannot allocate more spectators
                break
            
            # Check if the spectator has has enough money
            if(i.available_money < self.film_shown.price):
                logger.error(f"The spectator {i.id} has not enough money to watch this movie")
                # If the spectator does not have enough money we go with the next spectator of the list
                continue

            # Check if the spectator has a proper age for the film
            if(i.age < self.film_shown.min_age):
                logger.error(f"The spectator {i.id} is not old enough to watch this movie")
                # If the spectator does not have enough age we go with the next spectator of the list
                continue

            itsFree = True
            while(itsFree):
                row = randint(0, self.num_rows)
                col = randint(0, self.num_cols)
                if(self.list_seats[row][col].free):
                    self.list_seats[row][col].ocupateSeat(i.id)
                    print(f"The spectator {i.id} has been alocated in the {row} row and {col} column")
                    break
            
    def getAllocatedSpectators(self):

        """
        The method does not receive arguments and returns the list of those spectators that
        fulfilled the conditions to be seated.

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
        print("Show seats method")

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
    cinema1 = Cinema(12, 10, peterPan)
    cinema2 = Cinema(10, 5, blancanieves)
    cinema3 = Cinema(14, 7, mulan)
    
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
