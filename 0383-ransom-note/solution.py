class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        word_count = Counter(ransomNote)
        letters_count = Counter(magazine)
        if all(word_count[char] <= letters_count[char] for char in word_count):
                return True
        return False