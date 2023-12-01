# https://adventofcode.com/2023/day/1

with open('/Users/sh/Documents/Advent_of_Code_2023/day01_input.txt') as f: 
   data = f.readlines() # or f.read()

####################
## PART I:
####################

answer=[]

for row in data:
   left = 0
   right = len(row)-1
   lval = ""
   rval = ""
   val = ""
  
   #assumption is that there are always two distinct numeric characters first and last in the string
   while lval=="" or rval=="":   # two pointers

      if row[left].isnumeric():
         lval=row[left]
      else:
         left+=1
      if row[right].isnumeric():
         rval=row[right]
      else:
         right-=1
   val=lval+rval
   answer.append(int(val))
 
print(sum(answer))  #54, 697

####################
## PART II:
####################


answer=[]


for row in data:

   row= row.replace('one','one1one').replace('two','two2two').replace('three','three3three').replace('four','four4four')\
   .replace('five','five5five').replace('six','six6six').replace('seven','seven7seven').replace('eight','eight8eight').replace('nine','nine9nine')

   #replace words with digits and then do the same as in part 1

   left = 0
   right = len(row)-1
   lval = ""
   rval = ""
   val = ""
  
   #print(row)
   #assumption is that there are always two distinct numeric characters first and last in the string
   while lval=="" or rval=="":   # two pointers

      if row[left].isnumeric():
         lval=row[left]
      else:
         left+=1
      if row[right].isnumeric():
         rval=row[right]
      else:
         right-=1
   val=lval+rval
   answer.append(int(val))
  
print(sum(answer))  #answer -- 54885
  


      

