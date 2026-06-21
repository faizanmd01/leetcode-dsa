class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        # Find the maximum cost to define our frequency array size
        max_cost = max(costs)
        
        # Create a frequency array to count occurrences of each cost
        # Size is max_cost + 1 to account for 0-indexed positioning
        freq = [0] * (max_cost + 1)
        for cost in costs:
            freq[cost] += 1
            
        ice_cream_count = 0
        
        # Iterate through all possible costs starting from the cheapest (1)
        for cost in range(1, max_cost + 1):
            if freq[cost] == 0:
                continue
                
            # If we can't even afford a single one at this price, stop
            if coins < cost:
                break
                
            # Calculate how many bars of this cost we want vs how many we can afford
            count_to_buy = min(freq[cost], coins // cost)
            
            # Update our totals
            ice_cream_count += count_to_buy
            coins -= count_to_buy * cost
            
        return ice_cream_count