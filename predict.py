#!/usr/bin/python3

from linear_regression import predict

if __name__ == "__main__":
    try:
        with open("thetas.txt", "r") as file:
            lines = file.readlines()
    except:
        print("thetas.txt does not exist. run 'train_model.py' first. using default theta0 and theta1 values of 0")
        lines = [0, 0]

    m = float(lines[0])
    c = float(lines[1])
    print("theta1 =" , m , "\ntheta0 =" , c)

    mileage = "None"
    while not (mileage.isnumeric() and 0 < int(mileage) < 1000000000):
        mileage = input("input a mileage to estimate the price:\n")

    price = predict(int(mileage), m, c)
    print("for a mileage of" , mileage, ", the estimated price is: " , price)
