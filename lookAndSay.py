
# look and read off the digits
# write a function look_and_say(n, k) that starts with the provided number n
# and prints a new sequence by looking and saying the last one, k times

# for example, given n=1 and k=8:

# 1
# 11
# 21
# 1211
# 111221
# 312211
# 13112221
# 1113213211
# 31131211131221

def LookAndSay(n, k):
    # your code goes here
    n = str(n)
    print(n)
    j = 0
    while j < k:
        i = 0
        count = 0
        result = ""
        while i < len(n):
            count += 1
            if i < len(n) -1 and n[i] == n[i+1]:
                pass
            else:
                result += str(count) + n[i]
                count = 0
            i += 1
        print(result)
        n = result
        j += 1

if __name__ == "__main__":
    LookAndSay(1, 8)