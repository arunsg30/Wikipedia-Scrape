mix_list = [1,2,3,4,5,6,7,8,9]
ans = [x for x in mix_list if x%2 != 0]
print(ans)
square = [x*x for x in ans]
print(square)