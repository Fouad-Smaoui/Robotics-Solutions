class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        x, y = 0, 0  # Initial position
        dx, dy = 0, 1  # Initial direction: North
        obstacles_set = set(map(tuple, obstacles))
        max_distance_squared = 0

        for command in commands:
            if command == -2:  # Turn left
                dx, dy = -dy, dx
            elif command == -1:  # Turn right
                dx, dy = dy, -dx
            else:  # Move forward
                for _ in range(command):
                    if (x + dx, y + dy) in obstacles_set:
                        break  # Stop moving if obstacle encountered
                    x, y = x + dx, y + dy
                    max_distance_squared = max(max_distance_squared, x*x + y*y)

        return max_distance_squared

# Test the function
solution = Solution()
commands = [4, -1, 3]
obstacles = []
print(solution.robotSim(commands, obstacles))  # Output: 25

commands = [4, -1, 4, -2, 4]
obstacles = [[2, 4]]
print(solution.robotSim(commands, obstacles))  # Output: 65

commands = [6, -1, -1, 6]
obstacles = []
print(solution.robotSim(commands, obstacles))  # Output: 36