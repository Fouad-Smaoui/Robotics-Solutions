class Solution:
    def sumDistance(self, nums: List[int], s: str, d: int) -> int:
        # Initialize a list to store the final positions of the robots
        final_positions = []
        
        # Compute the final positions based on the initial positions and directions
        for i in range(len(nums)):
            if s[i] == 'L': 
                # If the robot is moving to the left, subtract d from its position
                final_positions.append(nums[i] - d)
            else: 
                # If the robot is moving to the right, add d to its position
                final_positions.append(nums[i] + d)
        
        # Sort the final positions to make distance calculation easier
        final_positions.sort()

        # Define the modulo value to avoid large numbers
        MOD = 10**9 + 7
        # Initialize variables to keep track of the total sum of distances and the prefix sum
        total_sum = 0
        prefix_sum = 0

        # Iterate through the sorted final positions
        for i in range(len(final_positions)):
            # Calculate the contribution of the current position to the total distance
            total_sum += final_positions[i] * i - prefix_sum
            # Apply modulo to keep the total sum within bounds
            total_sum %= MOD
            # Update the prefix sum with the current position
            prefix_sum += final_positions[i]
            # Apply modulo to keep the prefix sum within bounds
            prefix_sum %= MOD

        # Return the total sum of distances modulo 10^9 + 7
        return total_sum

# Example usage:
# sol = Solution()
# print(sol.sumDistance([-2, 0, 2], "RLL", 3))  # Output: 8
# print(sol.sumDistance([1, 0], "RL", 2))  # Output: 5
