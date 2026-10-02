class Solution:
    def convert(self, s: str, numRows: int) -> str:
        growth = 1
        zig_in = 0

        word_lis=[]
        for _ in range(numRows):
            word_lis.append([])

        if numRows==1:
            return s
        
        for i in range(len(s)):


            word_lis[zig_in].append(s[i])

            zig_in += growth
            if zig_in == numRows-1:
                growth=-1
            if zig_in == 0:
                growth=1


        return "".join("".join(row) for row in word_lis)
            
        







str1="PAYPALISHIRING"

s=Solution()
print(s.convert(str1, 3))
