class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        s_len, p_len = len(s), len(p)
        s_idx, p_idx = 0, 0
        
        # '*' मिलने पर pointers को ट्रैक करने के लिए variables
        star_idx = -1
        s_tmp_idx = -1
        
        while s_idx < s_len:
            # 1. अगर कैरेक्टर मैच होते हैं या पैटर्न में '?' मिलता है, तो दोनों पॉइंटर्स को आगे बढ़ाएं
            if p_idx < p_len and (p[p_idx] == s[s_idx] or p[p_idx] == '?'):
                s_idx += 1
                p_idx += 1
                
            # 2. अगर पैटर्न में '*' मिलता है, तो इसकी पोजीशन याद रखें
            elif p_idx < p_len and p[p_idx] == '*':
                star_idx = p_idx
                s_tmp_idx = s_idx
                p_idx += 1  # अभी के लिए मान लेते हैं कि '*' खाली स्ट्रिंग (0 characters) मैच कर रहा है
                
            # 3. अगर मैच नहीं हुआ और पहले कोई '*' मिल चुका था (Backtracking)
            elif star_idx != -1:
                p_idx = star_idx + 1  # पैटर्न पॉइंटर को '*' के ठीक बाद वाले कैरेक्टर पर ले जाएं
                s_tmp_idx += 1        # '*' को स्ट्रिंग का एक और कैरेक्टर मैच करने दें
                s_idx = s_tmp_idx
                
            # 4. अगर न तो मैच हुआ और न ही कोई '*' बैकअप है, तो मैच नामुमकिन है
            else:
                return False
        
        # स्ट्रिंग पूरी चेक होने के बाद, अगर पैटर्न में बचे हुए कैरेक्टर्स सिर्फ '*' हैं, तो उन्हें स्किप करें
        while p_idx < p_len and p[p_idx] == '*':
            p_idx += 1
            
        # अगर पैटर्न भी पूरा खत्म हो गया, तो इसका मतलब मैच सफल रहा
        return p_idx == p_len