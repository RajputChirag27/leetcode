class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        Here it is given we have to convert uppercase to lower case characters
        Here we have to remove all non-alphanumeric characters too
        Then we place two pointers one at start and one at end of the string
        and run until the left < right. If all characters are matching it's  palindrome else it's not we break the loop by returning false.

        Constraints
        1 <= s.length <= 2 * 105
        s consists only of printable ASCII characters.

        We have to do it in O(n)
        """
        n = len(s)
        left = 0
        right = n - 1

        while left < right:
            while left < right and not  (
                48 <= ord(s[left]) <= 57
                or 65 <= ord(s[left]) <= 90
                or 97 <= ord(s[left]) <= 122
            ):
                left += 1
            while left < right and not (
                48 <= ord(s[right]) <= 57
                or 65 <= ord(s[right]) <= 90
                or 97 <= ord(s[right]) <= 122
            ):
                right -= 1
            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1

        return True
