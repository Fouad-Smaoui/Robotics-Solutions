class Solution:
    def judgeCircle(self, moves: str) -> bool:
        # Define a dictionary to map moves to their corresponding coordinate changes
        move_map = {'R': (1, 0), 'L': (-1, 0), 'U': (0, 1), 'D': (0, -1)}
        
        # Initialize the starting position
        x, y = 0, 0
        
        # Process each move and update coordinates accordingly
        for move in moves:
            dx, dy = move_map[move]  # Get the coordinate changes for the current move
            x += dx
            y += dy
        
        # Check if the robot is back at the origin
        return x == 0 and y == 0

# Example usage
solution = Solution()
print(solution.judgeCircle("UD"))  # Output: True
print(solution.judgeCircle("LL"))  # Output: False