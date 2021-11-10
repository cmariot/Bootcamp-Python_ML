# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    vector.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: cmariot <cmariot@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/11/09 23:56:15 by cmariot           #+#    #+#              #
#    Updated: 2021/11/10 13:48:15 by cmariot          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class Vector:
    
    def __init__(self, value):
        
        type_list = False;
        type_list_of_list = False;
        type_list_of_list_of_floats = False;
        type_list_of_floats = False;

        # Check the input value type for the init, it could be a list of list of floats or a list of floats 
        if (type(value) == list):
            type_list = True;
            if (type(value[0]) == list):
                type_list_of_list = True;
                for elements in value:
                    if (type(elements[0]) != float):
                        print("The vector must be initialized as a list of list of floats or a list of floats.")
                        return ;
                type_list_of_list_of_floats = True;
            elif (type(value[0]) == float):
                for elements in value:
                    if (type(elements) != float):
                        print("The vector must be initialized as a list of list of floats or a list of floats.")
                        return ;
                type_list_of_floats = True;
            else:
                print("The vector must be initialized as a list of list of floats or a list of floats.")
                return ;
        else:
            print("The vector must be initialized as a list of list of floats or a list of floats.")
            return ;

       # print("type_list = " + str(type_list));
       # print("type_list_of_list = " + str(type_list_of_list));
       # print("type_list_of_list_of_floats = " + str(type_list_of_list_of_floats));
       # print("type_list_of_floats = " + str(type_list_of_floats));

        if (type_list_of_list_of_floats == True or type_list_of_floats == True):
            x1 = value[0]
            x2 = value[1]
            x3 = value[2]
            x4 = value[3]
            self.value = [x1, x2, x3, x4];

        column_vector = False
        row_vector = False
        if (type_list_of_list_of_floats == True):
            column_vector = True;
        elif (type_list_of_floats == True):
            row_vector = True;


if __name__ == "__main__":
    v1 = Vector([[0.0], [1.0], [2.0], [3.0]])
    print(v1.value)
    v2 = Vector([0.0, 1.0, 2.0, 3.0])
    print(v2.value)

