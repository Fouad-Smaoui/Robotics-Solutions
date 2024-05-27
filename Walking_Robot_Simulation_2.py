class Robot:  # Defines a class named Robot to create robot objects
    def __init__(self, width, height):  # Constructor method that initializes object properties
        self.width = width  # Sets the width property of the robot
        self.height = height  # Sets the height property of the robot
        self.x = 0  # Initializes the x-coordinate of the robot
        self.y = 0  # Initializes the y-coordinate of the robot
        self.direction_index = 0  # Initializes the direction index, representing the robot's orientation (0 for East)
        self.directions = ["East", "North", "West", "South"]  # Defines the cardinal directions
        self.dx = [1, 0, -1, 0]  # Defines changes in x-coordinate for each cardinal direction
        self.dy = [0, 1, 0, -1]  # Defines changes in y-coordinate for each cardinal direction
    
    def step(self, num):  # Method to move the robot a certain number of steps
        total_perimeter = 2 * (self.width + self.height) - 4  # Calculates the total perimeter of the robot's path
        num %= total_perimeter  # Adjusts num to account for complete perimeter cycles

        while num > 0:  # Iterates until the desired number of steps is reached
            next_x = self.x + self.dx[self.direction_index]  # Calculates the next x-coordinate
            next_y = self.y + self.dy[self.direction_index]  # Calculates the next y-coordinate

            if next_x < 0 or next_x >= self.width or next_y < 0 or next_y >= self.height:
                # Checks if the next step goes out of bounds
                self.direction_index = (self.direction_index + 1) % 4  # Updates the direction if out of bounds
            else:
                self.x = next_x  # Updates the x-coordinate
                self.y = next_y  # Updates the y-coordinate
                num -= 1  # Decrements the number of steps
    
    def getPos(self):  # Method to retrieve the current position of the robot
        return [self.x, self.y]  # Returns a list containing the current x and y coordinates
    
    def getDir(self):  # Method to retrieve the current direction the robot is facing
        return self.directions[self.direction_index]  # Returns the cardinal direction based on the direction index
