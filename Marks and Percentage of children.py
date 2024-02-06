#Find the total percentage and marks of the Student
Rollno=int(input("Enter the Roll Number:"))
name=input("Enter the Student Name:")
sub1=int(input("Enter the Marks of Telugu:"))
sub2=int(input("Enter the marks of Hindi:"))
sub3=int(input("Enter the marks of the English:"))
Total=sub1+sub2+sub3
percentage=Total/3/100
print("Total:",Total)
print("percentage:",percentage)
print("Roll no:",Rollno,"Student name:",name,"Telugu:",sub1,"Hindi",sub2,"English",sub3)