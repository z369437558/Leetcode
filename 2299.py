class Solution:
    def strongPasswordCheckerII(self, password: str) -> bool:
        if len(password)<8:
            return False
        low=0
        up=0
        num=0
        char=0
        for i in password:
            if i>='a' and i<='z':
                low=low+1
            if i>='A' and i<='Z':
                up=up+1
            if i>='0' and i<='9':
                num=num+1
            if i in "!@#$%^&*()-+":
                char = char+1
        if low==0:
            return False
        if up==0:
            return False
        for i in range(1,len(password)):
            if password[i]==password[i-1]:
                return False
        return True
a=Solution()
a.strongPasswordCheckerII("vpWkmkfSAcCLDBNRfH")