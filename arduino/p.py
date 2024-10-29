import numpy as np
import matplotlib.pyplot as plt


# Load training data
A = np.loadtxt('training_data.txt')
X = np.hstack((np.ones((A.shape[0], 1)), A[:, [0]], A[:, [0]] ** 2))  # Feature matrix with bias and quadratic term
T = A[:, [0]]  # Temperature data
C = A[:, [1]]  # Output voltage data

# Least squares method
coefficients = np.linalg.lstsq(X, C, rcond=None)[0]  # Compute best-fit coefficients
print("Fitted coefficients (training):", coefficients)

# Plot training data and fit
plt.plot(T, X @ coefficients, label="Least Squares Fit", color='b')  # Plot the fit line
plt.plot(T, C, 'k.', label="Training Data")  # Plot training data points
plt.xlabel("Temperature (°C)")
plt.ylabel("Output Voltage (V)")
plt.title("Training Data and Least Squares Fit")
plt.grid()
plt.legend()

# Save the training plot
plt.tight_layout()
plt.savefig('train.png')
plt.close()  # Close figure after saving

# Load validation data
B = np.loadtxt('validation_data.txt')
Xv = np.hstack((np.ones((B.shape[0], 1)), B[:, [0]], B[:, [0]] ** 2))  # Validation feature matrix
Tv = B[:, [0]]  # Validation temperature data
Cv = B[:, [1]]  # Validation output voltage data

# Plot validation data and fit
plt.plot(Tv, Xv @ coefficients, label="Least Squares Prediction", color='b')  # Plot predicted values
plt.plot(Tv, Cv, 'k.', label="Validation Data")  # Plot validation data points
plt.xlabel("Temperature (°C)")
plt.ylabel("Output Voltage (V)")
plt.title("Validation Data and Prediction")
plt.grid()
plt.legend()

# Save the validation plot
plt.tight_layout()
plt.savefig('valid.png')
plt.close()  # Close figure after saving
