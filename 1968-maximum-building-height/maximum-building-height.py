class Solution:
    def maxBuilding(self, n: int, restrictions: List[List[int]]) -> int:
        # Base cases handle karne ke liye boundary restrictions add karte hain
        # Building 1 ki height hamesha 0 honi chahiye
        restrictions.append([1, 0])
        
        # Restrictions ko building ID ke basis par sort karenge
        restrictions.sort()
        
        # Agar last building (n) restrictions mein nahi hai, toh ek dummy restriction add kar dete hain
        # Kyunki last building max n-1 height tak jaa sakti hai bina kisi restriction ke
        if restrictions[-1][0] != n:
            restrictions.append([n, n - 1])
            
        m = len(restrictions)
        
        # Pass 1: Left to Right
        # Kisi bhi building ki height pichli building ki height + unke beech ke distance se zyada nahi ho sakti
        for i in range(1, m):
            id1, h1 = restrictions[i-1]
            id2, h2 = restrictions[i]
            restrictions[i][1] = min(h2, h1 + (id2 - id1))
            
        # Pass 2: Right to Left
        # Kisi bhi building ki height agli building ki height + unke beech ke distance se zyada nahi ho sakti
        for i in range(m - 2, -1, -1):
            id1, h1 = restrictions[i]
            id2, h2 = restrictions[i+1]
            restrictions[i][1] = min(h1, h2 + (id2 - id1))
            
        # Ab har do consecutive restricted buildings ke beech ki max peak nikalenge
        max_height = 0
        for i in range(1, m):
            id1, h1 = restrictions[i-1]
            id2, h2 = restrictions[i]
            
            # Dono buildings ke beech ka gap
            gap = id2 - id1
            
            # Formula: Dono heights ko jitna badha sakte hain badhayenge jab tak woh beech mein meet na karein
            # Max height peak beech mein kahin banegi: (h1 + h2 + gap) // 2
            current_max = (h1 + h2 + gap) // 2
            max_height = max(max_height, current_max)
            
        return max_height