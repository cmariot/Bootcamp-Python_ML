import sys

def text_analyser(*args):
    """This function counts the number of upper characters, lower characters, punctuation and spaces in a given text."""
    if (len(args) == 0):
        str = input("What is the text to analyse ?\n")
    elif (len(args) > 1):
        print ("ERROR");
        return ;
    else:
        str = args[0];
    i = 0;
    characters = 0;
    upper_char = 0;
    lower_char = 0;
    punctuation = 0;
    spaces = 0;
    while (i < len(str)):
        if (str[i] == ' '):
            spaces = spaces + 1;
        elif (str[i] >= 'a' and str[i] <= 'z'):
            lower_char = lower_char + 1;
        elif (str[i] >= 'A' and str[i] <= 'Z'):
            upper_char = upper_char + 1;
        elif (str[i] >= '!' and str[i] <= '/'):
            punctuation = punctuation + 1;
        elif (str[i] >= ':' and str[i] <= '?'):
            punctuation = punctuation + 1;
        characters = characters + 1;
        i = i + 1;
    print("The text contains", characters, "characters :");
    print("-", upper_char, "upper letters");
    print("-", lower_char, "lower letters");
    print("-", punctuation, "punctuation marks");
    print("-", spaces, "spaces");
