# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    kata02.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: cmariot <cmariot@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/11/08 17:16:49 by cmariot           #+#    #+#              #
#    Updated: 2021/11/08 17:16:51 by cmariot          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

if __name__ == "__main__":
    time = (3,30,2019,9,25)
    print("%d/" %time[3], end ='');
    print("%d/" %time[4], end ='');
    print("%d" %time[2], end ='');
    print(" %d:" %time[0], end ='');
    print("%d" %time[1]);