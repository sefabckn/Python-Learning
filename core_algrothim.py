############################################
#  *Core Algortihms                        #
#  *Author:Benj4min                        #
#                                          #
#                                          #
#                                          #
############################################


#finding max value in a list algorithm
def max_val(list):
  """
  this is most important thing in this algorithm.
  Firstly we defining zero index as max_value in list.
  This defining is aiming to decide an argument for to create if statement
  for to determine maximum value
    """
  
  max_value = list_e[0] 
  """
  Then we can start to create loop on this list  for to create if statement with
  previous defined max_values which defined as max_val
  """
  for i in range(0, len(list_e), 1):
    if max_value <list_e[i]:
      """
      if max_value is lower than list[i] Python will replaced new max value as 
      'i' index of list.
      then Python will continue till to find maximum value of list
      """
      
      max_value = list_e[i]
      """
      Here we are defining maximum value as list 'i' index which determined in for loop.
      """
  return max_value #we returning max_value 


  """
  According to previous algortihm we can find minimum value in list which given to function
  
  """
  def min_val(list_e):
    min_value = list_e[0]
    
    for i in range(0, len(list_e), 1):
      if list_e[i] < min_value:
        
        min_value  = liste[i]
    return min_value

  
  
  
#if you want to execute a function you have to call this function.
list_e = [5,8,9,7,8,5,2,6,5,8,10,2,5]
min_val(list_e)
max_val(list_e)

        



