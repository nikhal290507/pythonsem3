from sklearn.linear_model import LinearRegression
import numpy as np

# hours studied vs marks scored (training data)

hours = np.array([1,2,3,4,5,6,7,8]).reshape(-1 , 1)
marks = np.array([35,45,50,60,65,72,80,88])

model = LinearRegression()
model.fit(hours,marks)

print(f"slope (conefficient) : {model.coef_[0]:.2f}")
print(f"Intercept : {model.intercept_:.2f}")
print(f"R2 score : {model.score(hours,marks):.4f}")
print()

# predict marks for a student who studied 9 hours

prediction = model.predict([[9]])[0]
print(f"predicted marks for 9 hours of study: {prediction:.1f}")


