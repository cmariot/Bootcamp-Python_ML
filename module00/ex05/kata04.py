# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    kata04.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: cmariot <cmariot@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/11/08 17:15:51 by cmariot           #+#    #+#              #
#    Updated: 2021/11/08 17:16:01 by cmariot          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

if __name__ == "__main__":
    t = ( 0, 4, 132.42222, 10000, 12345.67)
    print("module_0%d" %t[0], end=', ') 
    print("ex_0%d" %t[1], end=', ') 
    print("%.2f" %t[2], end=', ') 
    print(format(t[3],'.2e'), end=', ')
    print(format(t[4],'.2e'))
