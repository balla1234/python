#while loop

i = 1
while i <= 5:
    print(i)
    i = i + 1
    
i = 1
while i <= 5:
    print(i * "*" )
    i = i + 1    
    
i = 5
while i >= 0:
    print(i * "*" )
    i = i - 1     
    
 #for loop
for i in range(5):
    print(i)
for item in range(5):
    print(item + 1)
 
#for loop    
marks = [93,91,99]    
for score in marks:
    print(score)
    
 #append funct
    
marks = [93,91,99]    
marks.append(92)
print(marks)  
    
 #insert funct  
marks = [93,91,99] 
marks.insert(0,11) 
print(marks)
print(99 in marks)
print(len(marks))
    
marks = [93,91,99]   

i = 0
while i < len(marks):
    print(marks[i])
    i = i + 1
    
#to clear contents
i = 0
while i < len(marks):
    print(marks[i])
    i = i + 1
    
marks.clear()        
print(marks)   

#for and if
students = ["ram", "seet", "shree", "ashu", "raju"]

for student in students:
    if student == "ram":
        continue;
    print(student)
    
#for and if
students = ["ram", "seet", "shree", "ashu", "raju"]

for student in students:
    if student == "ashu":
        break;
    print(student) 
    
#Tuple
marks = (95,98,97,97,97)
print(marks.count(97))
print(marks.index(97))
 
person = "ram", "sham", "abhi"
print(person)
 
#Sets
marks = {95,98,97,97,97}

for score in marks:
    print(score)
    
#Dictionary
marks = {"english" : 95, "chemistry" : 92, } 
print(marks["chemistry"])  
marks["physics"] = 96
print(marks)

n = 0
while n < 10:
  print(n)
  n += 1
  
n = 0
while n < 6:
  print(n)
  if n == 3:
    break
  n += 1  
  