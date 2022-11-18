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
        self._location = random.randint(1, 1000)
        self._distance = [0, 0] # start with two so get_message always works
     
     
def get_message(self):
        """Gets a message from the seeker.
        Args:
            self (Seeker): An instance of Seeker.
        
        Returns:
            string: A message from the seeker.
        """
        message = "\nI'm going to find you!"
        if self._distance[-1] == 0:
            message = "\nI'm going to find you!"
        elif self._distance[-1] < self._distance[-2]:
            message = "\nShhh. I'm sneaking in now..."
        elif self._distance[-1] > self._distance[-2]:
            message = "\nI'm running around, but I'll find you..."
        return message
     
# 3) Create the get_location(self) method. Use the following method comment.
def get_location(self):
        """Gets the current location.
        
        Returns:
            number: The current location,
        """      
        return (self._distance[-1] == 0)        
        
# 4) Create the move_location(self, location) method. Use the following method comment.
def move(self, location):
        """Moves to the given location.

        Args:
            self (Seeker): An instance of Seeker.
            location (int): The given location.
        """
        distance = abs(self._location - location)
        self._distance.append(distance)
        self._location = location

