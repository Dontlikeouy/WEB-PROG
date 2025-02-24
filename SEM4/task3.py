array = ["зима", "весна", "лето", "осень", "зима"]


def num(num):
    if num > 12:
        return ""
    return (array[(num // 4)+1])


print(num(11))
