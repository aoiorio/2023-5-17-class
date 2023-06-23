def flatten(nested):
    for sublist in nested:
        for element in sublist:
            yield element # 関数とまるよ

nested = [[1, 2], [3, 4], [5]]
# for num in flatten(nested):
#     print(num)
# print("-" * 10) # ハイフンを十個並べる
gen = flatten(nested)
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
# print(next(gen)) StopIteration


print(list(flatten(nested)))