class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        counter = 0
        for i in words:
            word_count = Counter(i)
            letters_count = Counter(chars)
            if all(word_count[char] <= letters_count[char] for char in word_count):
                counter+=len(i)
        return counter
