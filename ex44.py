#list.append method 
# Ta add element in list

list1 = ['cow','cat','dog']
print list1


list1.append('goat')
print list1

list1.append(12345)
print list1

#list.extend method
#to merge one list to other list

list2 =["penguin","parrot","crane"]
list3 =["sparrow","goat"]
print list2
print list3

list2.extend(list3)
print list2


#list.inser method
#it method allow you to add the element in list 
#it takes two parameter 1= range 2= value

list2.insert(2,'elephant')
print list2


#list.index method
# to fetch the index number of value


elephanteindex = list2.index('elephant')
print elephanteindex

list2.insert(elephanteindex+1, 'duck')
print list2


#list.remove method
#remove the value from list

list2.remove('crane')
print list2

#list.pop method
#remove last element of list

popped=list2.pop()
print(popped)
print(list2)


#list.sort method
#sort the list acending and descending order

list4 = [1,2,7,9,3,4,5,6]
print list4
list4.sort()
print list4
list4.sort(reverse=True)
print list4


#list.reverse method is used to reverse the list items

list5 = [5,1,3,7,9,0]
print(list5)
list5.reverse()
print list5


#len method to get the length or number of items in a list

list6 = ['parrot','cow','mango','goat','elephant','tiger','carrot',]
print list6

lenght = len(list6)
print lenght

#min and max fuctions to find the the minimum or maximum value in list

list7 = [7,8,4,6,9,45,7,98]
print list7

maxvalue = max(list7)
print maxvalue

minvalue = min(list7)
print minvalue


#list.count method to find how many times an item appears in the list
list8 = ['a','a','c','d','a']
print list8
countA = list8.count('a')
print countA

#list.clear method to remove all the elements in the list

#list9 = ["i","am","learning","python"]
#list9.clear()
#print list9

