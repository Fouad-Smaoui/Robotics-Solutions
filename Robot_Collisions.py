class Solution:  # Define a class named Solution
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        # Combine positions, healths, directions, and indices into a list of tuples
        robots = list(zip(positions, healths, directions, range(len(positions))))
        # Sort the robots list by positions (the first element of each tuple)
        robots.sort(key=lambda x: x[0])
        stack = []  # Initialize an empty stack to manage robots moving to the right
        
        # Iterate through each robot in the sorted list
        for pos, health, dir, index in robots:
            if dir == 'R':  # If the robot is moving to the right
                stack.append((pos, health, dir, index))  # Add it to the stack
            else:  # If the robot is moving to the left
                # Process collisions with robots in the stack (moving to the right)
                while stack and stack[-1][2] == 'R' and health > 0:
                    # Pop the top robot from the stack to compare
                    top_pos, top_health, top_dir, top_index = stack.pop()
                    if top_health > health:  # If the top robot has more health
                        # Decrease the top robot's health by one and mark the current robot as defeated
                        stack.append((top_pos, top_health - 1, top_dir, top_index))
                        health = -1
                    elif top_health < health:  # If the current robot has more health
                        health -= 1  # Decrease the current robot's health by one
                    else:  # If both robots have the same health
                        health = -1  # Mark the current robot as defeated
                if health > 0:  # If the current robot survives
                    stack.append((pos, health, dir, index))  # Add it to the stack
        
        # Initialize the result list with None values, sized to the number of robots
        result = [None] * len(positions)
        # Fill in the health values of surviving robots in their original indices
        for pos, health, dir, index in stack:
            result[index] = health
        
        # Return the list of surviving robots' health, filtering out None values
        return [health for health in result if health is not None]
