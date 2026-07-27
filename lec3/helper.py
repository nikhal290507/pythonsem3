import statistics as st
def analyze_salaries(salaries):
    print("data: ", salaries)
    print()
    print("Mean  :", round(st.mean(salaries), 2),"<- pulled up by outliner 90000")
    print("Median:", st.median(salaries), "<- unaffected by outliner")
    print("Mode  :", st.mode(salaries))
    print()
    print("Variance:", round(st.variance(salaries), 2))
    print("std deviation:", round(st.stdev(salaries), 2), "<- large because of outliner")
