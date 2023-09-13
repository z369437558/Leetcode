class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        list1=[]
        for i in key.replace(' ',''):
            if i not in list1:
                list1.append(i)
        transTable = message.maketrans(str(list1),str(list(map(lambda x:chr(ord('a')+x),range(26)))),"")
        message = message.translate(transTable)
        return message
a = Solution()
a.decodeMessage(key = "the quick brown fox jumps over the lazy dog", message = "vkbs bs t suepuv")