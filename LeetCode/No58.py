class Solution(object):
    def lengthOfLastWord(self, s):
        result = 0
        split_s = s.split(" ")
        for each in split_s:
            if each != "":
                result = len(each)
        return result

class Solution(object):
    def lengthOfLastWord(self, s):
        return 0 if not s.split() else len(s.split()[-1])