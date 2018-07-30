def find_no(list):
 length=len(list)
 list.sort()

 print("first largest no is:",list[length-1])
 print("second largest no is:",list[length-2])
 print("first smallest no is:",list[0])
 print("second smallest no is:",list[1])
list=[100,45,78,25,65,2,1,85,122,1000]
Largest = find_no(list)
