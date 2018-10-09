data=[int(i) for i in input().split(" ")]
print("No" if (data[0]*data[1]) % 2 == 0 else "Yes")