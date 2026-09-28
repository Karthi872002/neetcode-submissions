class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        window = {}
        left = 0
        max_frequency = 0
        maximum = 0

        for right in range(len(s)):
            # Add current character
            window[s[right]] = window.get(s[right], 0) + 1

            # Highest frequency of a character in the window
            max_frequency = max(max_frequency, window[s[right]])

            # Number of characters we need to replace
            replacements = (right - left + 1) - max_frequency

            # Window is invalid
            while replacements > k:
                window[s[left]] -= 1

                if window[s[left]] == 0:
                    del window[s[left]]

                left += 1

                replacements = (right - left + 1) - max_frequency

            # Valid window
            maximum = max(maximum, right - left + 1)

        return maximum