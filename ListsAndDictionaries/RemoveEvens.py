def remove_evens(nums):
    oddList = []
    for i in nums:
        if i % 2 != 0:
            oddList.append(i)
            # using the remove function does not work because of how it iterates while using .remove()
            # when removing an item, the indices shift to the left, thus missing iterations
        else: continue
    return oddList



nums = input("Enter a list of numbers:\n").split()

nums = [int(i) for i in nums]

result = remove_evens(nums)

print(f'The resulting list with even numbers removed is:\n{result}')