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
    i = 0
    while (i < len(str)):
        if (str[i] >= '0' and str[i] <= '9'):
            number = number * 10 + (ord(str[i]) - ord('0'))
        else:
            print ("ERROR")
            return ;
        i = i + 1
    return (sign * number);

def whois():
    if (get_argc() > 1):
        print("ERROR")
        return ;
    elif (get_argc() == 0):
        return
    else:
        number = atoi(sys.argv[1]);
        if (number):
            if (number == 0):
                print ("I'm Zero.")
            elif (number % 2 == 0):
                print ("I'm Even.")
            else:
                print ("I'm Odd.")

if __name__ == "__main__":
    whois();
