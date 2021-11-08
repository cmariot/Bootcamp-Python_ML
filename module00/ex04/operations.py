import sys

def get_argc():
    return (len(sys.argv) - 1);

def atoi(str):
    number = 0
    sign = 1;
    if (str[0] == '-'):
        sign = -1;
        str = str[1:];
    elif (str[0] == '+'):
        str = str[1:];
    if (len(str) == 0):
        print ("InputError: only numbers")
        print("Usage: python operations.py <number1> <number2>");
        print("Example:");
        print("\tpython operations.py 10 3");
        return None;
    i = 0
    while (i < len(str)):
        if (str[i] >= '0' and str[i] <= '9'):
            number = number * 10 + (ord(str[i]) - ord('0'))
        else:
            print ("InputError: only numbers")
            print("Usage: python operations.py <number1> <number2>");
            print("Example:");
            print("\tpython operations.py 10 3");
            return None;
        i = i + 1
    return (sign * number);

def elementary(str1, str2):
    number1 = atoi(str1);
    if (number1 == None):
        return ;
    number2 = atoi(str2);
    if (number2 == None):
        return ;
    print("Sum :\t\t", number1 + number2);
    print("Difference :\t", number1 - number2);
    print("Product :\t", number1 * number2);
    if (number2 != 0):
        print("Quotient :\t", number1 / number2);
        print("Remainder :\t", number1 % number2);
    else:
        print("Quotient :\t ERROR (div by zero)");
        print("Remainder :\t ERROR (modulo by zero)");

if __name__ == "__main__":
    if (len(sys.argv) == 0):
        print("Usage: python operations.py <number1> <number2>");
        print("Example:");
        print("\tpython operations.py 10 3");
    elif (len(sys.argv) > 3):
        print("InputError: too many arguments");
        print("Usage: python operations.py <number1> <number2>");
        print("Example:");
        print("\tpython operations.py 10 3");
    else:
        elementary(sys.argv[1], sys.argv[2]);
