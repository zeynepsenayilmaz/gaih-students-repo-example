List1 = [1,3,5,7,9]
List2 = [0,2,4,6,8]
print(List1)
print(List2)
NewList = List1 + List2
print(NewList)
NewList.sort()
print(NewList)
squares = [i*2 for i in NewList]
print(squares)
for değer in NewList:
  print("{} adlı değerin veri tipi: {}".format(değer, type(değer)))
