class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        

        counts = [0]*26
        l = 0 
        r = 0 
        char = s[0]
        max_freq = 0
        max_length = 0 

        while r < len(s):

            new_char = s[r]
            current_char_idx = ord(new_char) - ord('A')
            counts[current_char_idx]+=1

            if counts[current_char_idx] > max_freq:
                max_freq = counts[current_char_idx]


            length_substr = r - l + 1

            number_of_replacement = length_substr - max_freq
            
            if number_of_replacement > k:
                outgoing_char_indx = ord(s[l]) - ord('A')
                counts[outgoing_char_indx] -=1
                l +=1
            else:
                max_length = max(max_length, r - l + 1)

            r+=1
        
        return max_length
        

            

            


            

            
            

        