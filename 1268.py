class Solution:
    def suggestedProducts(self, products: list[str], searchWord: str) -> list[list[str]]:
        products.sort()
        ans=[]
        for i in range(len(searchWord)):
            ans.append([])
            for word in products:
                if word[:i]==searchWord[:i]:
                    if len(ans[-1])<3:
                        ans[-1].append(word)
                    else:
                        break
        return ans
a = Solution()
a.suggestedProducts(products = ["mobile","mouse","moneypot","monitor","mousepad"], searchWord = "mouse")