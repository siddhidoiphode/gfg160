
class Solution:
    def compress(self, chars) -> int:
        updated = ""
        i = 0
        while i < len(chars):
            c = 1  # count current char at least once
            # count consecutive same chars
            while i + 1 < len(chars) and chars[i] == chars[i+1]:
                c += 1
                i+=1
            # append char
            updated += chars[i]
            # append count if > 1
            if c > 1:
                updated += str(c)
            i += 1   # move to next new char
        print("--updated--", updated)
        return len(updated)





obj =Solution()
chars= ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
result = obj.compress(chars)
print("-->" , result)
