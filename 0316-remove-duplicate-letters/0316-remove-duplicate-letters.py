class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        # Frequency map to count occurrences of each character
        freq = {char: 0 for char in s}
        for char in s:
            freq[char] += 1
        
        # Stack to build the result
        stack = []
        # Set to track characters already in the stack
        seen = set()
        
        for char in s:
            # Decrease the frequency of the current character
            freq[char] -= 1
            
            # If the character is already in the stack, skip it
            if char in seen:
                continue
            
            # Ensure lexicographical order by removing larger characters
            # from the stack if they still occur later
            while stack and char < stack[-1] and freq[stack[-1]] > 0:
                removed = stack.pop()
                seen.remove(removed)
            
            # Add the current character to the stack and mark it as seen
            stack.append(char)
            seen.add(char)
        
        # Join the stack to form the result string
        return ''.join(stack)

        