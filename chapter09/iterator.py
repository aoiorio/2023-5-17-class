season = ["spring", "summer", "fall", "winter"]
iter_season = iter(season)
print(type(iter_season))

# for文で回すのと同じ処理です
# print(next(iter_season))
# print(next(iter_season))
# print(next(iter_season))
# print(next(iter_season))

for x in iter_season:
    print(x)
# StopIteration
# print(next(iter_season)) >>>StopIteration