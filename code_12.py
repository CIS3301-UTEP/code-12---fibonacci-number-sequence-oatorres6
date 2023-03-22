def get_fibonacci_number(position):
   if position == 1 or position == 2:
        return 1
   else:
        return ((get_fibonacci_number(position-1)) + (get_fibonacci_number(position-2)))
    
def get_fibonacci_number_sequence(number):
   sequence_list=[]
   for i in range(0,number):  
        sequence_list.append(get_fibonacci_number(i+1))
   return sequence_list
    

if __name__ == "__main__":
   print(get_fibonacci_number(3))
   print(get_fibonacci_number_sequence(15))

   #base case
#       the list cannot be further divided 
# boolean if, else, elif 

#   Recursive call
#   As long as the list can be divided, do it
#