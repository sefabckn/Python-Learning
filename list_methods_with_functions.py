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
  and i want to remove "Blue".
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


  
  
  
  
  
  
  #In this case i will write index function for to make anything easier  
"""
Previously on remove function we've used  built-in funciton named as 'enumerate'
We will use this function again so i will not explain that how its working and how to use it in any loop
If you do not remember you should check out 'remove function'up there.
Well, Lets talk about our new function is 'INDEX'
as you know python is sorting all datas which in lists or tuples as starting from zero till ending value
So in this case i would like to show you how Python doing that and how can you create this algorithm as so simple
"""
#I've created a index function and i asking a value from user
#this value is can be anything so we can run it on loop
def index(str1):
  #I will give a list for to test this function
  default_list = ["Red", "Green", "Blue", "White", "Walter", "Junior","Skyler"]
  #now i will start to trip on this values by using for loop :)
  for index_number, value in enumerate(default_list):
   """
   I gave 2 variable,First variable is controlling -as you see- number of index and second variable is cont-
   rolling value of 'index number'.So you can see that index function is aiming to find index of given string 
   (str1)
  Lets keep coding and see how python does this
   """
      #here i will create a statement which is controlling str1 is equal to value or not
      #so we can find result
       if str1 == value:
        #if given value is equal to enumerated value 
        # we will add our result index_number which belong to enumerated value
          result = index_number
       else:
           pass
    return "Index number of {} = {}".format(str1, result)
  """
  as return we've used a string method is formatting
  This method were using as '%' in Python 2.x.x ,this method still working on Python 3 but i think it will
  be removed by developers in future.'format' method is most usefull i guess.Choose your side :D
  """
 #if you want to see result check this code pieces below
print(index("Green"))
  Expected Output  : 1
print(index("Blue"))
  Expected Output : 2
print(index("White"))
  Expected Output  : 3
print(index("Walter"))
  Expected Output : 4

  
  
  
  
  
  
  
  

  
    
    
    
    
    
  

  
  
  
  
  
  






  

