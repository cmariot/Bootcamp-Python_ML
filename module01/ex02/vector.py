# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    vector.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: cmariot <cmariot@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/11/09 23:56:15 by cmariot           #+#    #+#              #
#    Updated: 2021/11/10 15:36:17 by cmariot          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class Vector:
    
    def __init__(self, value):
        
        type_list = False;
        type_list_of_list = False;
        type_list_of_list_of_floats = False;
        type_list_of_floats = False;
        type_int = False;
        type_range = False;
        column_vector = False
        row_vector = False

        # Check the input value type for the init, it could be a list of list of floats, a list of floats, an int or a range.
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
        elif (type(value) == int):
            type_int = True;
        elif (type(value) == range):
            type_range = True;
        else:
            print("The vector must be initialized as a list of list of floats or a list of floats.")
            return ;

       # print("type_list = " + str(type_list));
       # print("type_list_of_list = " + str(type_list_of_list));
       # print("type_list_of_list_of_floats = " + str(type_list_of_list_of_floats));
       # print("type_list_of_floats = " + str(type_list_of_floats));

        self.value = []
        
        if (type_list_of_list_of_floats == True or type_list_of_floats == True):
            for elements in value:
                self.value.append(elements)
            if (type_list_of_list_of_floats == True):
                column_vector = True;
                self.shape = (len(self.value), 1)
            elif (type_list_of_floats == True):
                row_vector = True;
                self.shape = (1, len(self.value))

        elif (type_int == True):
            i = 0.0
            while (i < float(value)):
                self.value.append([i])
                i += 1.0
            self.shape = (int(i), 1);

        elif (type_range == True):
            min = float(value[0])
            print(min)
            max = float(value[-1])
            print(max)
            range_size = max - min
            while min <= max:
                self.value.append([min])
                min += 1.0
            self.shape = (int(range_size) + 1, 1)


if __name__ == "__main__":
    
    v1 = Vector([[0.0], [1.0], [2.0], [3.0]])
    print(v1.value)
    print(v1.shape)
    
    v2 = Vector([0.0, 1.0, 2.0, 3.0])
    print(v2.value)
    print(v2.shape)

    v3 = Vector(3)
    print(v3.value)
    print(v3.shape)

    v4 = Vector(range(10, 15))
    print(v4.value)
    print(v4.shape)

