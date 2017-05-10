number = 15
def build(number):
    all_factorials = []
    if number <= 0 or number >= 100:
        return "1 - 100 is only acceptable"
    if number == 1:
        all_factorials.append(1)
        return all_factorials
    elif number == 2:
        all_factorials.append(1)
        all_factorials.append(2)
        return all_factorials
    else:
        all_factorials.append(1)
        all_factorials.append(2)
        factorial = 2
        for i in range(2, number):
            input_number = i + 1
            factorial = input_number * factorial
            all_factorials.append(factorial)
        return all_factorials