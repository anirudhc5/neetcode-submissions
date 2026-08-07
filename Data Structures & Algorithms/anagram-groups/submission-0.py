class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = {}
        ans = []

        for word in strs:
            wordset = "".join(sorted(word))
            if wordset in result: result[wordset].append(word)
            else:
                result[wordset] = [word]
        
        for key in result:
            ans.append(result[key])

        return ans