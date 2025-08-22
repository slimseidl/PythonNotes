# Takes two lists of input and multiplies them together, then outputs the sum 

list1 = [int(i) for i in input().split()]
list2 = [int(i) for i in input().split()]

list3 = []

for i in range(len(list1)):
    list3.append(list1[i] * list2[i])
    
print(sum(list3))