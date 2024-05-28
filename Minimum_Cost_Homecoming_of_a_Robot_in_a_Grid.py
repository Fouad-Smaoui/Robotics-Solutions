# Solution class definition
class Solution:
    # Method to calculate the minimum cost
    def minCost(self, startPos: List[int], homePos: List[int], rowCosts: List[int], colCosts: List[int]) -> int:
        # Extracting start and home positions
        startrow, startcol = startPos  # Decomposing start position into row and column
        homerow, homecol = homePos     # Decomposing home position into row and column

        # Calculate the cost of moving in the rows
        if startrow < homerow:  # Check if the robot needs to move down
            # If moving down, sum the row costs from startrow + 1 to homerow
            row_movement_cost = sum(rowCosts[startrow + 1:homerow + 1])
        else:
            # If moving up, sum the row costs from homerow to startrow
            row_movement_cost = sum(rowCosts[homerow:startrow])
        
        # Calculate the cost of moving in the columns
        if startcol < homecol:  # Check if the robot needs to move right
            # If moving right, sum the column costs from startcol + 1 to homecol
            col_movement_cost = sum(colCosts[startcol + 1:homecol + 1])
        else:
            # If moving left, sum the column costs from homecol to startcol
            col_movement_cost = sum(colCosts[homecol:startcol])
        
        # Total minimum cost is the sum of row and column movement costs
        total_cost = row_movement_cost + col_movement_cost

        return total_cost  # Return the total minimum cost
