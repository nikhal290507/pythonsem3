import statistics as st
from utils import analyze_marks

marks = []
n = int(input("Enter the number of students: "))
for i in range(n):
    mark = int(input(f"Enter marks of student {i+1}: "))
    marks.append(mark)

analyze_marks(marks)