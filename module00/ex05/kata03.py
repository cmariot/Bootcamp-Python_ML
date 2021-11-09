# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    kata03.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: cmariot <cmariot@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/11/08 17:15:57 by cmariot           #+#    #+#              #
#    Updated: 2021/11/08 17:15:59 by cmariot          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

if __name__ == "__main__":
    phrase = "The right format"
    str_len = len(phrase);
    padding = 42 - str_len;
    i = 0;
    while (i < padding):
        print ('-', end='');
        i = i + 1;
    print(phrase, end='')
