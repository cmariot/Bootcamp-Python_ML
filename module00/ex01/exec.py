# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    exec.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: cmariot <cmariot@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/11/08 17:16:19 by cmariot           #+#    #+#              #
#    Updated: 2021/11/08 17:16:20 by cmariot          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

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
