class Solution:
    # @param {string[]} strs
    # @return {string[]}
    def anagrams(self, strs):
        check = {}
        result = []
        for word in strs:
            #key = list(word).sort()
            key = ''.join(sorted(word))
            if key in check:
                check[key] = check[key] + [word]
            else:
                check[key] = [word]
        
        for item in check:
            if len(check[item]) >= 2:
                result += check[item]
        return result