class Solution(object):
    def countConsistentStrings(self, allowed, words):
        count = len(words)
        for word in words:
            for w in word:
                if w not in allowed:
                    count-=1
                    break
        return count