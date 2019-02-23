class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        def patternmatch(word, pattern):
            if len(word) != len(pattern):
                return False
            mydict = {}
            i = 0
            while(i < len(word)):
                if pattern[i] in mydict:
                    if mydict[pattern[i]] == word[i]:
                        i += 1
                    else:
                        return False
                else:
                    if word[i] not in mydict.values():
                        mydict[pattern[i]] = word[i]
                        i += 1
                    else:
                        return False
                if i == len(word):
                    return True
            
        mylist = []
        for word in words:
            if patternmatch(word, pattern):
                mylist.append(word)
                
        #return patternmatch('ccc', 'abb')        
        return mylist