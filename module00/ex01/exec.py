import sys

def get_argc():
    return (len(sys.argv) - 1);

def reverse(str):
  return str[::-1]

def rev_alpha():
    i = get_argc();
    while (i > 0):
        if (i == 1):
            print(reverse(sys.argv[i]).swapcase())
        else:
            print(reverse(sys.argv[i]).swapcase(), end= ' ');
        i = i - 1

if __name__ == "__main__":
    rev_alpha();
