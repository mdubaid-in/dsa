from math import isqrt


num = int(input("Enter a number: "))
x, y = map(int, input("Enter two numbers separated by a space: ").split())


def count_digits(num):
    count = 0

    while num > 0:
        count += 1
        num //= 10
    return count


def reverse_number(num):
    reverse = 0

    while num > 0:
        reverse = reverse * 10 + num % 10
        num //= 10
    return reverse


def check_palindrome(num):
    return num == reverse_number(num)


def check_armstrong(num):
    sum = 0
    temp = num
    while temp > 0:
        sum += (temp % 10) ** count_digits(num)
        temp //= 10
    return sum == num


def check_prime(num):
    if num <= 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


# Euclidean Algorithm to find the greatest common divisor
def find_gcd(x, y):
    while x > 0 and y > 0:
        if x > y:
            x = x % y
        else:
            y = y % x
    return x if y == 0 else y


def divisors(num):
    divisors = []
    for i in range(1, isqrt(num) + 1):
        if num % i == 0:
            divisors.append(i)

            if i != num // i:
                divisors.append(num // i)
    return divisors


print(f"The number of digits in {num} is {count_digits(num)}")
print(f"The reverse of {num} is {reverse_number(num)}")
print(f"The number {num} is {'' if check_palindrome(num) else 'not '}a palindrome")
print(
    f"The number {num} is {'' if check_armstrong(num) else 'not '}an armstrong number"
)
print(f"The number {num} is {'' if check_prime(num) else 'not '}a prime number")
print(f"The GCD of {x} and {y} is {find_gcd(x, y)}")
print(f"The divisors of {num} are {divisors(num)}")
