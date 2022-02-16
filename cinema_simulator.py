from random import randint
from xmlrpc.client import boolean


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
    def __init__ (self, id: str, age: int, available_money: float) -> None :
        self.id = id
        self.age = age
        self.available_money = available_money

class Seat:
 
    # Initializer / Instance Attributes
    def __init__ (self, row: int, column: str, free: boolean, spectator_id: str) -> None :
        self.seat = [row, column]
        self.free = free
        self.spectator_id = spectator_id
    
    def ocupacteSeat(self, spectator_id):
        self.free = False
        self.spectator_id = spectator_id


class Cinema:

    # Initializer / Instance Attributes
    def __init__ (self, num_rows: int, num_cols: int, film_shown: Film) -> None :
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.film_shown = film_shown

    def createSeats(self):
        list_seats = [[]]
        for i in range(self.num_rows):
            for j in range(self.num_cols):
                list_seats[i][j] =  Seat(i, j, True, "")
        return list_seats
    
    def allocateSpectators(self, spectatorList):

        # Check if there are available seats

        # Chack which spectators meet the conditions
        list_seats= self.createSeats()
        print("list_seats", list_seats)
        for i in spectatorList:
            itsFree = False
            while(itsFree):
                row = randint(0, self.num_rows)
                col = randint(0, self.num_cols)
                if(list_seats[row][col].free):
                    list_seats[row][col].ocupacteSeat(i.id)
                    break

        print("Allocator method")
    
    def getAllocatedSpectators():
        print("Allocated Spectators method")
    
    def showSeats():
        print("Show seats method")

    def getSeats():
        """
        The method does not receive any argument and returns a
        list of objects of type Seat with all seats in the cinema

        """

        # Define the list of seats
        list_seats = []

        for i in range(Cinema.num_rows):

            for j in range(Cinema.num_cols):
                list_seats.append(Seat(i, j))

        return list_seats
        print("Get seats method")


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
        name = input("Name of the spectator: ")
        age = int(input("Age of the spectator: "))
        available_money = int(input("Available money: "))
        # Create a new spectator
        spectator = Spectator(name, age, available_money)
        # Save the spectator in the list of spectators
        list_spectators.append(spectator)
        
    print("List of spectators", list_spectators)
    # Call method to allocate the spectator
    cinema1.allocateSpectators(list_spectators)

