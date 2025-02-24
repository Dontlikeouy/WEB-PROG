def sqrt(number):
    return int(number**0.5)


def is_prime(num):
    if num in (0, 1, 2):
        return True
    else:
        if num % 2 == 0:
            return False
        else:
            for i in range(3, sqrt(num)+1, 2):
                if num % i == 0:
                    return False
                else:
                    return True


print(is_prime(int(input("Введите число от 0 до 1000: "))))
    