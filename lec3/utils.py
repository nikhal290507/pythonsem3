import statistics as st

def analyze_marks(marks):
    print("Marks:", marks)
    print("Count of students:", len(marks))
    print("Total marks:", sum(marks))
    print("Average (mean) : ", st.mean(marks))
    print("Middle value (median) : ", st.median(marks))
    print("highest marks (max) : ", max(marks))
    print("lowest marks (min) : ", min(marks))
    print("Range of marks : ", max(marks)-min(marks))