i=20
while i<31:
  if i==27:
     break
  print(i)
  i+=1
i=20
while i<31:
  print(i)
  i+=1
  if i==27:
    break
i=20
while i<31:
     print(i)
     if i==27:
       break
     i+=1
i=20
while i<31:
     if i==27:
       print(i)
       break
     i+=1


     i=20
while i<31:
     if i==27:
      continue
      print(i)
      i+=1

      i=20
while i<31:
     i+=1
     if i==27:
      continue
      print(i)
      
      
    



i= 20
sum=0
count=0
while i+30:
  sum = sum+i
  count+=1
  i+=1
print(sum/count)
ex;1

for i in range (1,3):
      for j in range (1,4):
          print(i,j)
          
ex :2




 for row in range (6,0,-1):
   for col in range(0,row):
     print("*", end="")
   print()


   for row in range (0,6):
   for col in range(0,row+1):
     print("*", end="")
    print()





   for row in range(5):
   for col in range(5):
    if col==0 or col==5-1 or row==0 or row ==5-1:
       print ("*",end=" ")
    else:
         print(" ",end=" ")
   print()





   for row in range(0,5):
   for col in range(0,6):
     if  (row==0 and col==3) or (row==1 and(col>=2 and col<=4)) or  (row==2 and (col>=1 and col<=5)):
       print("*",end=" ")
     else:
      print(" ",end=" ")
   print()




   -->list 
1. if the collection of elements are sounded by square brakets ,it is considerd
# to be list  
# example 1 
#11=[4,7,9,9,89, "HELLO",7+9],[8,9,0]
#charactristics of list 
1.list have to be sourended by []
2.it is mutable(the eliment in the list are changed)
3. every element inside list is  indexd 
4.the element inside list will be ordered forment
5. it can hold duplicate Value
6. its heterogenous




# To access the element in list 
lst1 = [1,4,1,7,89.7,7.5, "p" "i"]

#...> indexing
# 
# In the collection datatype like list, tuple, string . the elements will be aollowtd 
# with predefined unique valu called index valu
#  We have 2 types of indexing
# Positive indexing --. starts with 0 from left hand side 
# Negtive  indexing --> strats  with -1  from rigth had side

# positive indexing.
# print[lst1[0]]
# print (lst1[4])
# print ( lst1[20])-->error






# ?---->slicing
list =[1,4,1,7,89.7,7.5,"p","i"]
#lst1[start_index:end_index:step]
#print(lst1[0.4])
#print(lst1[6:8])
#print(lst1[3:6])
#print(lst1[:5])


print(lst1[0:7:1])
print(lst1[0:7:2])



# trail=int(input())

lst1 =[1,4,1,7,89.7,7.5,"p","i"]
#print([lst1[-4:-1]])
#print([lst1[-1:-4])-->[]
print(lst1[-7:-1])
print(lst1[-7:-1:2])

#! to insert ot add element insid list
# append()--> used to add element at last  position of list
l1=[9,8,0,6]
l1.append ("car")
print(l1)
