mid_list = input().split()

if len(mid_list) > 9:
    print("Too many inputs")
else:
    # example of using a loop to modify elements in place
    mid_list = [int(i) for i in mid_list]
    mid_list.sort()
    mid = len(mid_list) // 2
    print(mid_list[mid])