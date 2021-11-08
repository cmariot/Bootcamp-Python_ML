if __name__ == "__main__":
    phrase = "The right format"
    str_len = len(phrase);
    padding = 42 - str_len;
    i = 0;
    while (i < padding):
        print ('-', end='');
        i = i + 1;
    print(phrase, end='')
