def SWAPPER(list1):
    list2=[]
    l=int(len(list1)/2)
    for i in range (l):
        list2.append(list1[i])
    del list1[0:l]
    list1.extend(list2)
    print(list1)
list1=[35,67,89,23,12,45]
SWAPPER(list1)