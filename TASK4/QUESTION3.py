c = int (input("enter number of students"))
b =[["roll number", "Name", "Score"]]
for i in range(c):
    roll= input("enter Roll number")
    studentname= input("enter the student name")
    marks= int (input("enter marks"))
    b.append([roll, studentname, marks])
for i in range(len(b)):
    for j in range (len(b[i])):
        k = b[i][j]
        print (k, end="\t")
    print("\c")
h= int(input("enter row to be printed"))
for i in b[h]:
    print(i, end="\t")
