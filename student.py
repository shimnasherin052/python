student={
    "name":"anna",
    "roll_number":"53",
    "register number":"REG202432",
    "department":"computer application",
    "semester":"s1",
}
print("student details\n",student)
print()
total_marks=int(input("enter the marks:"))
student["total_mark"]=total_marks
print("student detail with total mark\n",student)
print()
if student["total_mark"] >= 90:
    student["grade"] = "A"
elif student["total_mark"] >= 82:
    student["grade"] = "B"
elif student["total_mark"] >= 75:    
    student["grade"] = "C"              
elif student["total_mark"] >= 60:
    student["grade"] = "D"
elif student["total_mark"] >= 50:      
    student["grade"] = "P"
else:
    student["grade"] = "F"
print("student details by deleting grade",student)
print()
del student["roll_number"]
print("student details by deleting roll no\n",student)
print()
