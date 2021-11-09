# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    filterwords.py                                     :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: cmariot <cmariot@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/11/09 10:41:18 by cmariot           #+#    #+#              #
#    Updated: 2021/11/09 11:23:34 by cmariot          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys
import re

def atoi(str):
    number = 0
    sign = 1;
    if (str[0] == '-'):
        sign = -1;
        str = str[1:];
    elif (str[0] == '+'):
        str = str[1:];
    if (len(str) == 0):
        return None;
    i = 0
    while (i < len(str)):
        if (str[i] >= '0' and str[i] <= '9'):
            number = number * 10 + (ord(str[i]) - ord('0'))
        else:
            return None;
        i = i + 1
    return (sign * number);

def filterwords(str, str2):
    len_to_filter = atoi(str2);
    if (len_to_filter == None):
        print("ERROR")
        return ;
    str_list = re.findall(r'\w+', str)
    i = 0
    while (i < len(str_list)):
        if len(str_list[i]) <= len_to_filter:
            del(str_list[i]);
        else:
            i = i + 1
    print(str_list)


if __name__ == "__main__":
    if (len(sys.argv) <= 2):
        print("Usage : python filterwords.py [str] [len]")
    elif (len(sys.argv) >= 4):
        print("Error, too many args");
    else:
        filterwords(sys.argv[1], sys.argv[2]);
