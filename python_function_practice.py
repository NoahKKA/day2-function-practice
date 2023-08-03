def max_num(x,y,z):
    return max([x,y,z])

# print(max_num(4,56,6))

def mult_list(my_list):
    current_prod = 1
    for i in my_list:
        current_prod *= i
    return current_prod

# print(mult_list([4,5,6,2,6]))


def rev_string(str):
    new_str = str
    return new_str[::-1]


# print(rev_string('hello world'))


def num_within(x,y,z):
    return x in range(y, z+1)

# print(num_within(3,2,4))
# print(num_within(3,1,3))
# print(num_within(10,2,5))

def pascal(x):
    if x <= 0:
        return

    def generate_next_row(prev_row):
        next_row = [1]
        for i in range(1, len(prev_row)):
            next_row.append(prev_row[i - 1] + prev_row[i])
        next_row.append(1)
        return next_row

    current_row = [1]
    print(current_row)

    for _ in range(1, x):
        current_row = generate_next_row(current_row)
        print(current_row)

pascal(5)
