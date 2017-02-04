def binarySearch(myList,item):
    first = 0
    last = len(myList) - 1
    found = False

    while not found and first<=last:
        midpoint = (first + last)//2
        if myList[midpoint] == item:
            found = True
        else:
            if item < myList[midpoint]:
                last = midpoint - 1
            else:
                first = midpoint + 1
    print midpoint

myList = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
myList2 = ['a','b','c','d','e','f','g','h','i','j','k','l','m','o','p','q','r']
myList3 = ['pepe','juan','alberto','pedro','elias','martin','martina','daniela','tito','elvira','seba','mari','isa','vinchu']

print sorted(myList3)
binarySearch(sorted(myList3),'martina')
