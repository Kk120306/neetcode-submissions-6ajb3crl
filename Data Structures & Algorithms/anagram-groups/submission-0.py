class Solution:

    def getSignature(self, word: str) -> List[int]:
        result = [0] * 26
        for c in word:
            result[ord(c) - ord('a')] += 1
        return result

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # do the anagram but the key is a array of index 
        # do the anagram only if word is not found 
        table = {}
        for word in strs:
            signature = tuple(self.getSignature(word))
            if signature in table:
                table[signature].append(word)
            else:
                table[signature] = [word]
        
        return list(table.values())