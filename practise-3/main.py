# arr = [1,2,3,4,5,5,4,3,2,1]
# dict1 = {}
# i = 0 
# while i<len(arr):
#     count = 0
#     a = arr[i]
#     for j in range(i,len(arr)):
#         if arr[i]==arr[j]:
#             count = count + 1
#     up = dict({a:count})
#     if a not in dict1.keys():
#         dict1.update(up)
#     i = i+1

# print(dict1)




# def subString(Str,n):
#     li = []
#     for Len in range(1,n + 1):
#         for i in range(n - Len + 1):
#             j = i + Len - 1
#             for k in range(i,j + 1):
#                 li.append(Str[k])
#                 print(Str[k],end="")
#             print()


             
# Str = "aabcddefg"
# subString(Str,len(Str))

str = "(()(()))()"

for i in range(len(str)):
    if str[i] == "(":
        print(0,end="")
    else:
        print(1,end="")
print()

