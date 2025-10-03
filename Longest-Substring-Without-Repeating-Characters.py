class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_index = {}
        max_length = 0
        left = 0
        
        for right in range(len(s)):
            current_char = s[right]
            
            if current_char in char_index and char_index[current_char] >= left:
                left = char_index[current_char] + 1
            
            char_index[current_char] = right
            current_length = right - left + 1
            max_length = max(max_length, current_length)
        
        return max_length


# Test the solution
if __name__ == "__main__":
    solution = Solution()
    
    # Test cases
    print(solution.lengthOfLongestSubstring("abcabcbb"))  # Output: 3
    print(solution.lengthOfLongestSubstring("bbbbb"))     # Output: 1
    print(solution.lengthOfLongestSubstring("pwwkew"))    # Output: 3
    print(solution.lengthOfLongestSubstring(""))          # Output: 0
    print(solution.lengthOfLongestSubstring("dvdf"))      # Output: 3
