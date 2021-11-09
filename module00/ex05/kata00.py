# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    kata00.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: cmariot <cmariot@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/11/08 17:16:42 by cmariot           #+#    #+#              #
#    Updated: 2021/11/08 17:16:43 by cmariot          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

if __name__ == "__main__":
    t = (19,42,21)
    tuple_len = len(t);
    print("The", tuple_len, "numbers are:", end=' ')
    j = 0;
    for i in t:
        if (j != tuple_len - 1):
            print(i, end = ', ')
        else:
            print(i);
        j = j + 1;

