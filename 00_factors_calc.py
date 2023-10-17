# functions go here

# FIND OUT HOW TO STOP YOU FROM ENTERING A NUMBER HIGHER THAN 200

# puts a series of symbols at start and end of text
def statement_generator(text, decoration):
    # Make a string with five characters
    ends = decoration * 5

    # add decoration to start and end of statement
    statement = "{} {} {}".format(ends, text, ends)

    print()
    print(statement)
    print()

    return ""


# Displays instructions / information
def instructions():
    statement_generator("Instructions / Information", "=")
    print("This program will ask users to enter an integer between ")
    print("1 and 200 (inclusive) and will then output the factors of ")
    print("the integer")
    print()
    return ""


# Checks input is a number more than a given value
def num_check(question, low, high):
    valid = False
    while not valid:

        error = "Please enter an integer that is more than {} or lower than {} and isn't a decimal".format(low, high)

        try:

            # ask user to enter a number
            response = int(input(question))

            # checks number is more than zero & less than 200
            if low <= response <= high:
                return response

            # outputs error if input is invalid
            else:
                print(error)
                print()

        except ValueError:
            print(error)

# gets factors, returns a sorted list


def get_factors(to_factor):

    # List to hold factors

    factors_list = []

    # Square root to_factor to find 'half-way'

    limit = int(to_factor ** 0.5)

    # Find factor pairs and add to list

    for item in range(1, limit + 1):

        # Check factor is not 1 (unity)

        if to_factor == 1:
            break

        # Check if number is a factor

        result = to_factor % item

        factor_1 = int(to_factor // item)

        # Add factor to a list if it is not already in there

        if result == 0:
            factors_list.append(item)

        if factor_1 != item and result == 0:
            factors_list.append(factor_1)

    # output

    factors_list.sort()

    return factors_list


# main  routine goes here

# heading
statement_generator("factors calculator", "-")

# Display instructions if user has not used the program before
first_time = input("press <enter> to see the instructions or any key to continue ")

if first_time == "":
    instructions()

# Loop to allow multiple calculations per session
keep_going = ""
while keep_going == "":

    comment = ""

    # ask user for number to be factored
    var_to_factor = num_check("Number? ", 1, 200)

    if var_to_factor != 1:
        factor_list = get_factors(var_to_factor)
    else:
        factor_list = ""
        comment = "One is UNITY! It only has one factor. Itself :D"

    # comments for squares / primes
    if len(factor_list) == 2:
        comment = "{} is a prime number.".format(var_to_factor)
    elif len(factor_list) % 2 == 1:
        comment = "{} is a perfect square".format(var_to_factor)

    # output factors and comment

    # Generate heading
    if var_to_factor == 1:
        heading = "One is special..."

    else:
        heading = "factors of {}".format(var_to_factor)

    # Output factors and comment
    statement_generator(heading, "-")
    print()
    print(factor_list)
    print(comment)

    print()
    keep_going = input("Press <enter> to continue or any key to quit")
    print()

print()
print("Thankyou for using the factors calculator")
print()
