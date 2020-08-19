def prime(n):
    if n > 1:
        for i in range(2, n):
            if (n % i) == 0:
                break
        else:
            print(n, "prime number")


for num in range(1, 100):
    result = ""
    if prime(num):
        result += "Prime"
    else:
        if num % 3 == 0 and num % 5 == 0:
            result += "FizzBuzz"
            print(num, result)
        elif num % 3 == 0:
            result += "Fizz"
            print(num, result)
        elif num % 5 == 0:
            result += "Buzz"
            print(num, result)
        else:
            print(num)


if __name__ == '__main__':

    print('All done')
