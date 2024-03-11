from typing import List

class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        def is_palindrome(check):
            return check == check[::-1]
        
        words_dict = {word: i for i, word in enumerate(words)}
        palindrome_pairs = []

        for word, k in words_dict.items():
            n = len(word)
            for j in range(n+1):
                pref = word[:j]
                suf = word[j:]
                if is_palindrome(pref):
                    back = suf[::-1]
                    if back != word and back in words_dict:
                        palindrome_pairs.append([words_dict[back], k])
                if j != n and is_palindrome(suf):
                    back = pref[::-1]
                    if back != word and back in words_dict:
                        palindrome_pairs.append([k, words_dict[back]])

        return palindrome_pairs
