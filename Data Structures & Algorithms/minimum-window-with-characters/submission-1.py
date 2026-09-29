class Solution:
    def minWindow(self, s: str, t: str) -> str:

        lookup = {}

        # Characters we need
        for char in t:
            lookup[char] = lookup.get(char, 0) + 1

        window = {}

        left = 0
        right = 0

        have = 0
        need = len(lookup)

        minimum = ""
        
        while right < len(s):

            # Add s[right] to window
            char = s[right]

            window[char] = window.get(char, 0) + 1

            # Did this character satisfy its required frequency?
            if char in lookup and window[char] == lookup[char]:
                have += 1

            # Current window is valid
            while have == need:

                current = s[left:right + 1]

                # Save if this is the first
                # or smaller than previous answer
                if minimum == "" or len(current) < len(minimum):
                    minimum = current

                # Remove s[left]
                left_char = s[left]

                window[left_char] -= 1

                # We lost a required character
                if (
                    left_char in lookup
                    and window[left_char] < lookup[left_char]
                ):
                    have -= 1

                left += 1

            right += 1

        return minimum
    

s = Solution()
print(s.minWindow("OUZODYXAZV", "XYZ"))