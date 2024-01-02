### Higher Order Functions ###


def sum_one(value):
    return value + 1
def sum_five(value):
    return value + 5


def sum_two_values_and_one(first_value,second_value, f_sum_algo): 
    return f_sum_algo(first_value + second_value)

print(sum_two_values_and_one(5,2, sum_one))

print(sum_two_values_and_one(5,2, sum_five))


### Clouseres ###

def sum_ten(original_value):
    def add(value):
            return value + 10 + original_value 
    return add

add_clousure = sum_ten(1)
print(add_clousure(5))

print(sum_ten(5)(1)) 



### Built-in Higher Order Functions ###

numbers = [2, 5, 10, 21]
# Map

def multiply_two(number):
     return number * 2

print(list(map(multiply_two,numbers)))
print(list(map(lambda number: number * 3,numbers)))

#Filter

def filter_greater_than_ten(number):
    if number > 10:
        return True
    return False


print(list(filter(filter_greater_than_ten,numbers)))
print(list(filter(lambda number: number > 10,numbers)))


#Reduce

def sum_two_values(number_one, number_two):
    return number_one + number_two


from functools import reduce

print(reduce(sum_two_values,numbers))

