###########################################################
#  *In This tutorial i will write some list methods       #
#   using functions for to improve my function skills     #
#                                                         #
#   *Author:Benj4min                                      #
#                                                         #
###########################################################


"""
Firstly i would like to explain this method stuffs.
In Python lists we have some methods (append,pop,remove...)
these methods is providing to make some process more simple.
for example:
list1 = [1,2,3,4,5,6,"Python"]
if you want to add something to in this list.There is a simple method in python as
list1.append("Learning Programming")
now if we check our list1;
[1,2,3,4,5,6,"Python","Learning Programming"]
"""

"""
Now I will coding some simple methods,Lets start
"""

def clear():
  """
  Clear method is deleting everything in a list
  """
  #defining a list 
  color_list=["Red", "Blue", "Green", "Black"]
  """
  In this section firstly we have to check lenght of list for to process clear method
  if our list is not empty -this color_list>0- we will proceeding color_list as a empty list
  then we will return color_list
  """
  
  
  if len(color_list > 0):
    #we are replacing color_list as a empty list and this makes our clear function run.
    color_list = []
  return color_list
"""
In this case we will coding remove function,This function removing a string or a value which given
in function.then function will remove this given argument.If you give one more argument it will give
you a error
"""

def remove(str1):#giving str1 as removing value
  color_list = ["Red", "Green", "Blue", "Black"]#our algorithm will process on this list
  """
  I will continue with for loops.In this loop we will define two argument
  because we need to learn index of given 'str1' there are some ways to learn index of list.
  I will show you usage for loops on dictionary
  but firstly i need to explain that What is dictionary?
  dictionary is a data type in Python which like lists.
  for example:
  simple_dictionary = {"one":1, "two":2,"three":3}
  according to in this example dictionary has two value first value is 'key' the keys taking a value
  after (:).
  dictionart building is like that = {"key":value,"key1":value1,.......}
 and if you want to run forr loops on a dictionary ,you need to define two object
 """
 


for index,value in enumerate(color_list):
  """
  we defined two variable in this for loop because we need to learn which value in which index
  also we need to sort all objects which in dictionary,In this case enumerate function is including to
  algorithm,enumerate function is a 'built-in funciton' which defined in Python3.SO we can use it for free :)
  enumerate makes sort and giving a number to every object.
  for example:
  for index, value in enumerate(color_list)
  if you run this code piece you will see an output like this:
  0:Red
  1:Green
  2:Blue
  3:Black
  in this case our first values(0,1,2,3) are equal to our index which defined in for loop,as
  normally other variable is equal to Values(Red,Green...)
  Well enumerate function is so usefull and making something easier,Thank you Python :)
  """
  
  #Here, we are controlling our given value is equal to value which in for loop
  #if our given string is equal to value 
  #we will define a new list for to make removing action
  #In this list we have used some list slicing
  #firstly we are taking all values till to index number then we will add 'index+1'
  #our str1(giving string) is will be between index and index+1
  """
  example: color_list=["Red", "Blue", "Green", "Black"]
  and i want to clear remove "Blue".
  this code piece is making this:
  ["Red",] + ["Green","Black"]
  ["0",] + ["2","3"]
  our "Blue" is between in two list slice
  
  """
  #this is a method for to remove given string
  if str1 == value:
    new_color_list = color_list[:index] + color_list[index+1:]
  #then returning new list
  return new_color_list

 
  
#a new function 
"""
I will write a function we call it as pop
This method making this :
if you call this pop method in a list you have to give index number and 
pop method will return your given index has equal to which value.
then we can start
"""
#i am defining a function as pop and this function takes an index number 
#for which value i want to return

def pop(index_number):
  #defining a simple list for example
  color_list = ["Red", "Green", "Blue", "Black"]
  #now i will start to chechk statements
  if color_list[x] in color_list:
    #i checked my 'x' index is in color_list or not?
    #then we can continue
    #i will define a new list for to realize pop action
    new_color_list = color_list[:x] + color_list[x+1:]
    #we used previous same tecnique where in remove function
  #now we returning your given index has equal to which value 
  return color_list[x]
#if i want to run this code:
print(pop(#any index which not out of range))
  



  
    
    
    
    
    
  

  
  
  
  
  
  






  

