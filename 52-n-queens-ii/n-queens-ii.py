class Solution:
    def totalNQueens(self, n: int) -> int:
        # Sets jo track rakhenge ki kaunse columns aur diagonals block ho chuke hain
        cols = set()
        pos_diag = set() # (r + c)
        neg_diag = set() # (r - c)
        
        self.count = 0
        
        def backtrack(r):
            # Base Case: Agar hum saari rows (0 se n-1) par queen baitha chuke hain
            if r == n:
                self.count += 1
                return
            
            # Har ek column par check karo is row 'r' ke liye
            for c in range(n):
                # Agar yeh column ya diagonals pehle se attacked hain, toh skip karo
                if c in cols or (r + c) in pos_diag or (r - c) in neg_diag:
                    continue
                
                # Queen ko rakhne ke liye positions ko block karo (Choose)
                cols.add(c)
                pos_diag.add(r + c)
                neg_diag.add(r - c)
                
                # Agli row par jao (Explore)
                backtrack(r + 1)
                
                # Wapas aate waqt position ko unblock karo taaki doosre raaste check ho sakein (Backtrack)
                cols.remove(c)
                pos_diag.remove(r + c)
                neg_diag.remove(r - c)
                
        # 0th row se shuru karein
        backtrack(0)
        return self.count