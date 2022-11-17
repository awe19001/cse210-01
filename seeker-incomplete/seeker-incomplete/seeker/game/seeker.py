# TODO: Implement the Seeker class as follows...
import random
# 1) Add the class declaration. Use the following class comment.

class Seeker:
    """The person looking for the Hider. 
    
    The responsibility of a Seeker is to keep track of its location and distance travelled.
    
    Attributes:
        location (int): The location of the Seeker (1-1000).
        distance (list): The distance travelled with each move.    def __init__(self):
    """

# 2) Create the class constructor. Use the following method comment.
def __init__(self):
        """Constructs a new Seeker.

        Args:
            self (Seeker): An instance of Seeker.
        """
       
# 3) Create the get_location(self) method. Use the following method comment.
        self.location = random.randint(1, 1000)
        """Gets the current location.
        
        Returns:
            number: The current location,
        """
        self.distance = [0, 0]
        
# 4) Create the move_location(self, location) method. Use the following method comment.
def move(self, location):
        """Moves to the given location.

        Args:
            self (Seeker): An instance of Seeker.
            location (int): The given location.
        """
        distance = abs(self.location - location)
        self.distance.append(distance)
        self.location = location