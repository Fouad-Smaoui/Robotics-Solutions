class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        # Directions represented as (dx, dy) corresponding to North, East, South, and West
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        # Initial position (x, y) at the origin (0, 0)
        x, y = 0, 0
        
        # Initial direction index (0: North, 1: East, 2: South, 3: West)
        direction_index = 0
        
        # Process each instruction in the given instructions string
        for instruction in instructions:
            if instruction == 'G':
                # Move forward in the current direction
                dx, dy = directions[direction_index]
                x += dx
                y += dy
            elif instruction == 'L':
                # Turn left (counter-clockwise), update direction index
                direction_index = (direction_index - 1) % 4
            elif instruction == 'R':
                # Turn right (clockwise), update direction index
                direction_index = (direction_index + 1) % 4

        # Check if the robot is back at the origin (0, 0) or not facing North
        return (x == 0 and y == 0) or (direction_index != 0)

# Create an instance of the Solution class
solution = Solution()

# Print the result of the isRobotBounded method
print(solution.isRobotBounded(instructions))  # Expected output: True
