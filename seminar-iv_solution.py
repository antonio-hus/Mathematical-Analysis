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
def lists_generator(limit: int) -> (list, list):

    v_pos = []
    v_neg = []
    for i in range(1, limit, 2):
        v_pos.append(1/i)
    for j in range(2, limit, 2):
        v_neg.append(-1*(1/j))

    v_pos.reverse()
    v_neg.reverse()
    return v_pos, v_neg


def one_positive_one_negative_arrangement(limit: int) -> float:

    v_pos, v_neg = lists_generator(limit)

    s = 0.0
    while v_pos != [] and v_neg != []:
        s += v_pos[-1]
        s += v_neg[-1]
        v_pos.pop()
        v_neg.pop()
    return s


def two_positive_two_negative_arrangement(limit: int) -> float:

    v_pos, v_neg = lists_generator(limit)

    s = 0.0
    while len(v_pos) >= 2 and len(v_neg) >= 2:

        s += v_pos[-1]
        v_pos.pop()
        s += v_pos[-1]
        v_pos.pop()

        s += v_neg[-1]
        v_neg.pop()
        s += v_neg[-1]
        v_neg.pop()

    return s


def one_positive_two_negative_arrangement(limit: int) -> float:

    v_pos, v_neg = lists_generator(limit)

    s = 0.0
    while v_pos != [] and len(v_neg) >= 2:

        s += v_pos[-1]
        v_pos.pop()

        s += v_neg[-1]
        v_neg.pop()
        s += v_neg[-1]
        v_neg.pop()

    return s


def two_positive_one_negative_arrangement(limit: int) -> float:

    v_pos, v_neg = lists_generator(limit)

    s = 0.0
    while len(v_pos) >= 2 and v_neg != []:

        s += v_pos[-1]
        v_pos.pop()
        s += v_pos[-1]
        v_pos.pop()

        s += v_neg[-1]
        v_neg.pop()

    return s


def one_positive_three_negative_arrangement(limit: int) -> float:

    v_pos, v_neg = lists_generator(limit)

    s = 0.0
    while v_pos != [] and len(v_neg) >= 3:

        s += v_pos[-1]
        v_pos.pop()

        s += v_neg[-1]
        v_neg.pop()
        s += v_neg[-1]
        v_neg.pop()
        s += v_neg[-1]
        v_neg.pop()

    return s


def three_positive_one_negative_arrangement(limit: int) -> float:

    v_pos, v_neg = lists_generator(limit)

    s = 0.0
    while len(v_pos) >= 3 and v_neg != []:

        s += v_pos[-1]
        v_pos.pop()
        s += v_pos[-1]
        v_pos.pop()
        s += v_pos[-1]
        v_pos.pop()

        s += v_neg[-1]
        v_neg.pop()

    return s


def one_positive_five_negative_arrangement(limit: int) -> float:
    v_pos, v_neg = lists_generator(limit)

    s = 0.0
    while v_pos != [] and len(v_neg) >= 5:

        s += v_pos[-1]
        v_pos.pop()

        s += v_neg[-1]
        v_neg.pop()
        s += v_neg[-1]
        v_neg.pop()
        s += v_neg[-1]
        v_neg.pop()
        s += v_neg[-1]
        v_neg.pop()
        s += v_neg[-1]
        v_neg.pop()

    return s


def five_positive_one_negative_arrangement(limit: int) -> float:

    v_pos, v_neg = lists_generator(limit)

    s = 0.0
    while len(v_pos) >= 5 and v_neg != []:

        s += v_pos[-1]
        v_pos.pop()
        s += v_pos[-1]
        v_pos.pop()
        s += v_pos[-1]
        v_pos.pop()
        s += v_pos[-1]
        v_pos.pop()
        s += v_pos[-1]
        v_pos.pop()

        s += v_neg[-1]
        v_neg.pop()

    return s


def one_positive_tf_negative_arrangement(limit: int) -> float:
    v_pos, v_neg = lists_generator(limit)

    s = 0.0
    while v_pos != [] and len(v_neg) >= 25:

        s += v_pos[-1]
        v_pos.pop()

        times = 1
        while times <= 25:
            times = times + 1
            s += v_neg[-1]
            v_neg.pop()


    return s


def tf_positive_one_negative_arrangement(limit: int) -> float:

    v_pos, v_neg = lists_generator(limit)

    s = 0.0
    while len(v_pos) >= 25 and v_neg != []:

        times = 1
        while times <= 25:
            times = times + 1
            s += v_pos[-1]
            v_pos.pop()

        s += v_neg[-1]
        v_neg.pop()

    return s


def one_positive_hun_negative_arrangement(limit: int) -> float:
    v_pos, v_neg = lists_generator(limit)

    s = 0.0
    while v_pos != [] and len(v_neg) >= 100:

        s += v_pos[-1]
        v_pos.pop()

        times = 1
        while times <= 100:
            times = times + 1
            s += v_neg[-1]
            v_neg.pop()


    return s


def hun_positive_one_negative_arrangement(limit: int) -> float:

    v_pos, v_neg = lists_generator(limit)

    s = 0.0
    while len(v_pos) >= 100 and v_neg != []:

        times = 1
        while times <= 100:
            times = times + 1
            s += v_pos[-1]
            v_pos.pop()

        s += v_neg[-1]
        v_neg.pop()

    return s


# Front End Section

def generate_result_table(configuration: int):
    if configuration == 0:
        print()
        print("Default Configuration: One positive - One Negative")

        result1 = one_positive_one_negative_arrangement(50000)
        result2 = one_positive_one_negative_arrangement(250000)
        result3 = one_positive_one_negative_arrangement(500000)
        result4 = one_positive_one_negative_arrangement(1000000)
        result5 = one_positive_one_negative_arrangement(2500000)
        result6 = one_positive_one_negative_arrangement(5000000)
        result7 = one_positive_one_negative_arrangement(10000000)

        print("    50.000 Elements:", result1)
        print("   250.000 Elements:", result2)
        print("   500.000 Elements:", result3)
        print(" 1.000.000 Elements:", result4)
        print(" 2.500.000 Elements:", result5)
        print(" 5.000.000 Elements:", result6)
        print("10.000.000 Elements:", result7)

        print()
        print("Second Default Configuration: Two positive - Two Negative")
        print("Notice that nothing has changed in this variation")

        result1 = two_positive_two_negative_arrangement(50000)
        result2 = two_positive_two_negative_arrangement(250000)
        result3 = two_positive_two_negative_arrangement(500000)
        result4 = two_positive_two_negative_arrangement(1000000)
        result5 = two_positive_two_negative_arrangement(2500000)
        result6 = two_positive_two_negative_arrangement(5000000)
        result7 = two_positive_two_negative_arrangement(10000000)

        print("    50.000 Elements:", result1)
        print("   250.000 Elements:", result2)
        print("   500.000 Elements:", result3)
        print(" 1.000.000 Elements:", result4)
        print(" 2.500.000 Elements:", result5)
        print(" 5.000.000 Elements:", result6)
        print("10.000.000 Elements:", result7)
    if configuration == 2:
        print()
        print("Modified Configuration: Two positive - One Negative")

        result1 = two_positive_one_negative_arrangement(50000)
        result2 = two_positive_one_negative_arrangement(250000)
        result3 = two_positive_one_negative_arrangement(500000)
        result4 = two_positive_one_negative_arrangement(1000000)
        result5 = two_positive_one_negative_arrangement(2500000)
        result6 = two_positive_one_negative_arrangement(5000000)
        result7 = two_positive_one_negative_arrangement(10000000)

        print("    50.000 Elements:", result1)
        print("   250.000 Elements:", result2)
        print("   500.000 Elements:", result3)
        print(" 1.000.000 Elements:", result4)
        print(" 2.500.000 Elements:", result5)
        print(" 5.000.000 Elements:", result6)
        print("10.000.000 Elements:", result7)
    if configuration == -2:
        print()
        print("Modified Configuration: One positive - Two Negative")

        result1 = one_positive_two_negative_arrangement(50000)
        result2 = one_positive_two_negative_arrangement(250000)
        result3 = one_positive_two_negative_arrangement(500000)
        result4 = one_positive_two_negative_arrangement(1000000)
        result5 = one_positive_two_negative_arrangement(2500000)
        result6 = one_positive_two_negative_arrangement(5000000)
        result7 = one_positive_two_negative_arrangement(10000000)

        print("    50.000 Elements:", result1)
        print("   250.000 Elements:", result2)
        print("   500.000 Elements:", result3)
        print(" 1.000.000 Elements:", result4)
        print(" 2.500.000 Elements:", result5)
        print(" 5.000.000 Elements:", result6)
        print("10.000.000 Elements:", result7)
    if configuration == 3:
        print()
        print("Modified Configuration: Three positive - One Negative")

        result1 = three_positive_one_negative_arrangement(50000)
        result2 = three_positive_one_negative_arrangement(250000)
        result3 = three_positive_one_negative_arrangement(500000)
        result4 = three_positive_one_negative_arrangement(1000000)
        result5 = three_positive_one_negative_arrangement(2500000)
        result6 = three_positive_one_negative_arrangement(5000000)
        result7 = three_positive_one_negative_arrangement(10000000)

        print("    50.000 Elements:", result1)
        print("   250.000 Elements:", result2)
        print("   500.000 Elements:", result3)
        print(" 1.000.000 Elements:", result4)
        print(" 2.500.000 Elements:", result5)
        print(" 5.000.000 Elements:", result6)
        print("10.000.000 Elements:", result7)
    if configuration == -3:
        print()
        print("Modified Configuration: One positive - Three Negative")

        result1 = one_positive_three_negative_arrangement(50000)
        result2 = one_positive_three_negative_arrangement(250000)
        result3 = one_positive_three_negative_arrangement(500000)
        result4 = one_positive_three_negative_arrangement(1000000)
        result5 = one_positive_three_negative_arrangement(2500000)
        result6 = one_positive_three_negative_arrangement(5000000)
        result7 = one_positive_three_negative_arrangement(10000000)

        print("    50.000 Elements:", result1)
        print("   250.000 Elements:", result2)
        print("   500.000 Elements:", result3)
        print(" 1.000.000 Elements:", result4)
        print(" 2.500.000 Elements:", result5)
        print(" 5.000.000 Elements:", result6)
        print("10.000.000 Elements:", result7)
    if configuration == 5:
        print()
        print("Modified Configuration: Five positive - One Negative")

        result1 = five_positive_one_negative_arrangement(50000)
        result2 = five_positive_one_negative_arrangement(250000)
        result3 = five_positive_one_negative_arrangement(500000)
        result4 = five_positive_one_negative_arrangement(1000000)
        result5 = five_positive_one_negative_arrangement(2500000)
        result6 = five_positive_one_negative_arrangement(5000000)
        result7 = five_positive_one_negative_arrangement(10000000)

        print("    50.000 Elements:", result1)
        print("   250.000 Elements:", result2)
        print("   500.000 Elements:", result3)
        print(" 1.000.000 Elements:", result4)
        print(" 2.500.000 Elements:", result5)
        print(" 5.000.000 Elements:", result6)
        print("10.000.000 Elements:", result7)
    if configuration == -5:
        print()
        print("Modified Configuration: One positive - Five Negative")

        result1 = one_positive_five_negative_arrangement(50000)
        result2 = one_positive_five_negative_arrangement(250000)
        result3 = one_positive_five_negative_arrangement(500000)
        result4 = one_positive_five_negative_arrangement(1000000)
        result5 = one_positive_five_negative_arrangement(2500000)
        result6 = one_positive_five_negative_arrangement(5000000)
        result7 = one_positive_five_negative_arrangement(10000000)

        print("    50.000 Elements:", result1)
        print("   250.000 Elements:", result2)
        print("   500.000 Elements:", result3)
        print(" 1.000.000 Elements:", result4)
        print(" 2.500.000 Elements:", result5)
        print(" 5.000.000 Elements:", result6)
        print("10.000.000 Elements:", result7)
    if configuration == 25:
        print()
        print("Modified Configuration: Twenty-Five positive - One Negative")

        result1 = tf_positive_one_negative_arrangement(50000)
        result2 = tf_positive_one_negative_arrangement(250000)
        result3 = tf_positive_one_negative_arrangement(500000)
        result4 = tf_positive_one_negative_arrangement(1000000)
        result5 = tf_positive_one_negative_arrangement(2500000)
        result6 = tf_positive_one_negative_arrangement(5000000)
        result7 = tf_positive_one_negative_arrangement(10000000)

        print("    50.000 Elements:", result1)
        print("   250.000 Elements:", result2)
        print("   500.000 Elements:", result3)
        print(" 1.000.000 Elements:", result4)
        print(" 2.500.000 Elements:", result5)
        print(" 5.000.000 Elements:", result6)
        print("10.000.000 Elements:", result7)
    if configuration == -25:
        print()
        print("Modified Configuration: One positive - Twenty-Five Negative")

        result1 = one_positive_tf_negative_arrangement(50000)
        result2 = one_positive_tf_negative_arrangement(250000)
        result3 = one_positive_tf_negative_arrangement(500000)
        result4 = one_positive_tf_negative_arrangement(1000000)
        result5 = one_positive_tf_negative_arrangement(2500000)
        result6 = one_positive_tf_negative_arrangement(5000000)
        result7 = one_positive_tf_negative_arrangement(10000000)

        print("    50.000 Elements:", result1)
        print("   250.000 Elements:", result2)
        print("   500.000 Elements:", result3)
        print(" 1.000.000 Elements:", result4)
        print(" 2.500.000 Elements:", result5)
        print(" 5.000.000 Elements:", result6)
        print("10.000.000 Elements:", result7)
    if configuration == 100:
        print()
        print("Modified Configuration: A Hundred Positive - One Negative")

        result1 = hun_positive_one_negative_arrangement(50000)
        result2 = hun_positive_one_negative_arrangement(250000)
        result3 = hun_positive_one_negative_arrangement(500000)
        result4 = hun_positive_one_negative_arrangement(1000000)
        result5 = hun_positive_one_negative_arrangement(2500000)
        result6 = hun_positive_one_negative_arrangement(5000000)
        result7 = hun_positive_one_negative_arrangement(10000000)

        print("    50.000 Elements:", result1)
        print("   250.000 Elements:", result2)
        print("   500.000 Elements:", result3)
        print(" 1.000.000 Elements:", result4)
        print(" 2.500.000 Elements:", result5)
        print(" 5.000.000 Elements:", result6)
        print("10.000.000 Elements:", result7)
    if configuration == -100:
        print()
        print("Modified Configuration: One Positive - A Hundred Negative")

        result1 = one_positive_hun_negative_arrangement(50000)
        result2 = one_positive_hun_negative_arrangement(250000)
        result3 = one_positive_hun_negative_arrangement(500000)
        result4 = one_positive_hun_negative_arrangement(1000000)
        result5 = one_positive_hun_negative_arrangement(2500000)
        result6 = one_positive_hun_negative_arrangement(5000000)
        result7 = one_positive_hun_negative_arrangement(10000000)

        print("    50.000 Elements:", result1)
        print("   250.000 Elements:", result2)
        print("   500.000 Elements:", result3)
        print(" 1.000.000 Elements:", result4)
        print(" 2.500.000 Elements:", result5)
        print(" 5.000.000 Elements:", result6)
        print("10.000.000 Elements:", result7)


def main():
    print("Mathematically we have demonstrated that the alternating sum of (-1)^(n+1) / n converges to ln(2)")
    print("However, we know that this series is only conditionally ( or semi ) convergent")
    print()
    print("In this program we will test the Riemann Series Theorem ( also known as the Riemann Rearrangement Theorem)")
    print("Which states as follows: ")
    print()
    print("If an infinite series is conditionally convergent, then its terms can be arranged in a permutation")
    print("so that the series converges to any given value, or even diverges")
    print()
    print("We are unable to test on an infinite set of numbers, but we will use sets of >10.000 numbers in order to")
    print("approximate the sum of the series arranged in some different configurations: ")
    print()
    print("Official ln(2) approximation: ", math.log(2))

    generate_result_table(0)
    print()

    generate_result_table(2)
    generate_result_table(-2)

    generate_result_table(3)
    generate_result_table(-3)
    print()

    generate_result_table(5)
    generate_result_table(-5)
    print()

    generate_result_table(25)
    generate_result_table(-25)
    print()

    generate_result_table(100)
    generate_result_table(-100)
    print()

    pass


main()
