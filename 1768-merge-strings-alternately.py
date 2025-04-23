# Example 1:

# Input: word1 = "abc", word2 = "pqr"
# Output: "apbqcr"
# Explanation: The merged string will be merged as so:
# word1:  a   b   c
# word2:    p   q   r
# merged: a p b q c r
# Example 2:

# Input: word1 = "ab", word2 = "pqrs"
# Output: "apbqrs"
# Explanation: Notice that as word2 is longer, "rs" is appended to the end.
# word1:  a   b 
# word2:    p   q   r   s
# merged: a p b q   r   s
# Example 3:

# Input: word1 = "abcd", word2 = "pq"
# Output: "apbqcd"
# Explanation: Notice that as word1 is longer, "cd" is appended to the end.
# word1:  a   b   c   d
# word2:    p   q 
# merged: a p b q c   d

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        # merge string 1 -> 2 -> 1 -> 2 until reach the max length
        # check if i is not more than length
        # ex. 1 = abcde, 2 = qwe -> 5 iterations 
        # will be O(n)
        result = []
        longest = max(len(word1), len(word2))
        for i in range(longest):
            if i < len(word1):
                result.append(word1[i])
            if i < len(word2):
                result.append(word2[i])
        
        return ''.join(result)
    
    

# Test the solution with examples
if __name__ == "__main__":
    solution = Solution()
    
    # Example 1
    print("Example 1:")
    print(solution.mergeAlternately("abc", "pqr"))  # Expected: "apbqcr"
    
    # Example 2
    print("\nExample 2:")
    print(solution.mergeAlternately("ab", "pqrs"))  # Expected: "apbqrs"
    
    # Example 3
    print("\nExample 3:")
    print(solution.mergeAlternately("abcd", "pq"))  # Expected: "apbqcd"
