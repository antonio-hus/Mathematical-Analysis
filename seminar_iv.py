"""
Homework for Seminar IV - Exercise 7

[Python]
Show numerically that sum of (−1)^n+1 / n = ln 2 with n>=1.
Change the order of summation in this series – for example by first adding p positive terms,
then q negative terms, and so on – and show numerically that the rearrangement gives a different sum
(depending on p, q)

"""


# Imports Section
import math


# Back End Section

# Default Configuration - One Positive / One Negative
def compute_normal_config(limit: int) -> float:
    s = 0.0
    for i in range(1, limit):
        if i % 2 != 0:
            s = s + 1/i
        else:
            s = s - 1/i
    return s


# Second Configuration - One Positive / Two Negative
def compute_second_config(limit: int) -> float:
    s = 0.0
    for i in range(1, limit, 2):
        if i % 2 != 0:
            s += 1/i
            s -= 1/(2*i)
            s -= 1/(2*(i+1))
    return s


# Third Configuration - One Positive / Three Negatives
def compute_third_config(limit: int) -> float:
    s = 0.0
    k = 1
    for i in range(1, limit, 2):
        if i % 2 != 0:
            s += 1/i
            s += 1/(i+2)
            s -= 1/(2*k)
        k = k+1
    return s


# Fourth Configuration - Positive First / Then Negative
def compute_fourth_config(limit: int) -> float:
    s = 0.0
    for i in range(1, limit, 2):
        s += 1/i
    for i in range(2, limit, 2):
        s -= 1/i
    return s


# Fifth Configuration - Negative First / Then Positive
def compute_fifth_config(limit: int) -> float:
    s = 0.0
    for i in range(2, limit, 2):
        s -= 1/i
    for i in range(1, limit, 2):
        s += 1/i
    return s

# Front End Section
def gen_table_normal_config():

    print()
    print("Default Configuration: One positive - One Negative")

    result1 = compute_normal_config(50000)
    result2 = compute_normal_config(250000)
    result3 = compute_normal_config(500000)
    result4 = compute_normal_config(1000000)
    result5 = compute_normal_config(2500000)
    result6 = compute_normal_config(5000000)
    result7 = compute_normal_config(10000000)

    print("    50.000 Elements:", result1)
    print("   250.000 Elements:", result2)
    print("   500.000 Elements:", result3)
    print(" 1.000.000 Elements:", result4)
    print(" 2.500.000 Elements:", result5)
    print(" 5.000.000 Elements:", result6)
    print("10.000.000 Elements:", result7)

    print()
    print("The mathematical results of the series in the default arrangement is ln(2)")
    print("Official Approximation of ln(2): ", math.log(2))


def gen_table_second_config():

    print()
    print("Second Configuration: One positive - Two Negative")

    result1 = compute_second_config(50000)
    result2 = compute_second_config(250000)
    result3 = compute_second_config(500000)
    result4 = compute_second_config(1000000)
    result5 = compute_second_config(2500000)
    result6 = compute_second_config(5000000)
    result7 = compute_second_config(10000000)

    print("    50.000 Elements:", result1)
    print("   250.000 Elements:", result2)
    print("   500.000 Elements:", result3)
    print(" 1.000.000 Elements:", result4)
    print(" 2.500.000 Elements:", result5)
    print(" 5.000.000 Elements:", result6)
    print("10.000.000 Elements:", result7)

    print()
    print("The mathematical results of the series in the default arrangement is ln(2)/2")
    print("Official Approximation of ln(2)/2: ", math.log(2)/2)
    print("Official Approximation of ln(2): ", math.log(2))


def gen_table_third_config():

    print()
    print("Third Configuration: Two positive - One Negative")

    result1 = compute_third_config(50000)
    result2 = compute_third_config(250000)
    result3 = compute_third_config(500000)
    result4 = compute_third_config(1000000)
    result5 = compute_third_config(2500000)
    result6 = compute_third_config(5000000)
    result7 = compute_third_config(10000000)

    print("    50.000 Elements:", result1)
    print("   250.000 Elements:", result2)
    print("   500.000 Elements:", result3)
    print(" 1.000.000 Elements:", result4)
    print(" 2.500.000 Elements:", result5)
    print(" 5.000.000 Elements:", result6)
    print("10.000.000 Elements:", result7)


def gen_table_fourth_config():

    print()
    print("Fourth Configuration: Positive First - Negative Last")

    result1 = compute_fourth_config(50000)
    result2 = compute_fourth_config(250000)
    result3 = compute_fourth_config(500000)
    result4 = compute_fourth_config(1000000)
    result5 = compute_fourth_config(2500000)
    result6 = compute_fourth_config(5000000)
    result7 = compute_fourth_config(10000000)

    print("    50.000 Elements:", result1)
    print("   250.000 Elements:", result2)
    print("   500.000 Elements:", result3)
    print(" 1.000.000 Elements:", result4)
    print(" 2.500.000 Elements:", result5)
    print(" 5.000.000 Elements:", result6)
    print("10.000.000 Elements:", result7)


def gen_table_fifth_config():

    print()
    print("Fifth Configuration: Negative First - Positive Last")

    result1 = compute_fifth_config(50000)
    result2 = compute_fifth_config(250000)
    result3 = compute_fifth_config(500000)
    result4 = compute_fifth_config(1000000)
    result5 = compute_fifth_config(2500000)
    result6 = compute_fifth_config(5000000)
    result7 = compute_fifth_config(10000000)

    print("    50.000 Elements:", result1)
    print("   250.000 Elements:", result2)
    print("   500.000 Elements:", result3)
    print(" 1.000.000 Elements:", result4)
    print(" 2.500.000 Elements:", result5)
    print(" 5.000.000 Elements:", result6)
    print("10.000.000 Elements:", result7)


def gui():
    print("An official approximate for the value of ln(2) is: ")
    print(math.log(2))
    print()
    print("Mathematically we have demonstrated that the alternating sum of (-1)^(n+1) / n converges to ln(2)")
    print("However, we know that this series is only conditionally ( or semi ) convergent")
    print()
    print("In this program we will test the Riemann Series Theorem ( also known as the Riemann Rearrangement Theorem")
    print("Which states as follows: ")
    print()
    print("If an infinite series is conditionally convergent, then its terms can be arranged in a permutation")
    print("so that the series converges to any given value, or even diverges")
    print()
    print("We are unable to test on an infinite set of numbers, but we will use sets of >10.000 numbers in order to")
    print("approximate the sum of the series arranged in some different configurations: ")


def main():
    gui()
    gen_table_normal_config()
    gen_table_second_config()
    gen_table_third_config()
    gen_table_fourth_config()
    gen_table_fifth_config()

main()
