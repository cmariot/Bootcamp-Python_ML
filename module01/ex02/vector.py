# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    vector.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: cmariot <cmariot@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/11/09 23:56:15 by cmariot           #+#    #+#              #
#    Updated: 2021/11/10 23:58:21 by cmariot          ###   ########.fr        #
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
            max = float(value[-1])
            if (min < max):
                range_size = max - min + 1
                while min <= max:
                    self.value.append([min])
                    min += 1.0
                self.shape = (int(range_size), 1)
            else:
                print("Error, check the range");

    def __add__(self, vector2):
        if (self.shape == vector2.shape):
            i = 0
            if (type(self.value[0]) == list):
                while (i < len(self.value)):
                    self.value[i][0] = self.value[i][0] + vector2.value[i][0]
                    i += 1
            elif (type(self.value[0]) == float):
                while (i < len(self.value)):
                    self.value[i] = self.value[i] + vector2.value[i]
                    i += 1

    def __radd__(self, vector2):
        if (self.shape == vector2.shape):
            self.__add__(vector2);
        else:
            i = 0
            if (type(self.value[0]) == list):
                while (i < len(self.value)):
                    self.value[i][0] = self.value[i][0] + vector2.value[i]
                    i += 1
            elif (type(self.value[0]) == float):
                while (i < len(self.value)):
                    self.value[i] = self.value[i] + vector2.value[i][0]
                    i += 1

    def __sub__(self, vector2):
        if (self.shape == vector2.shape):
            i = 0
            if (type(self.value[0]) == list):
                while (i < len(self.value)):
                    self.value[i][0] = self.value[i][0] - vector2.value[i][0]
                    i += 1
            elif (type(self.value[0]) == float):
                while (i < len(self.value)):
                    self.value[i] = self.value[i] - vector2.value[i]
                    i += 1

    def __rsub__(self, vector2):
        if (self.shape == vector2.shape):
            self.__sub__(vector2);
        else:
            i = 0
            if (type(self.value[0]) == list):
                while (i < len(self.value)):
                    self.value[i][0] = self.value[i][0] - vector2.value[i]
                    i += 1
            elif (type(self.value[0]) == float):
                while (i < len(self.value)):
                    self.value[i] = self.value[i] - vector2.value[i][0]
                    i += 1

    def __truediv__(self, scalar):
        if (scalar == 0):
            print("Error, division by 0 is impossible.")
            return ;
        i = 0
        if (type(self.value[0]) == list):
            while (i < len(self.value)):
                self.value[i][0] = self.value[i][0] / scalar
                i += 1
        elif (type(self.value[0]) == float):
            while (i < len(self.value)):
                self.value[i] = self.value[i] / scalar
                i += 1

    def __rtruediv__(self, scalar):
        i = 0
        new_value = []
        if (type(self.value[0]) == list):
            while (i < len(self.value)):
                if (self.value[i][0] != 0):
                    new_value.append(scalar / self.value[i][0])
                else:
                    print("Error, division by 0.")
                    return None
                i += 1
            return new_value
        elif (type(self.value[0]) == float):
            while (i < len(self.value)):
                if (self.value[i] != 0):
                    new_value.append(scalar / self.value[i])
                else:
                    print("Error, division by 0.")
                    return None
                i += 1
            return new_value
           

    def __mul__(self, scalar):
        i = 0
        if (type(self.value[0]) == list):
            while (i < len(self.value)):
                self.value[i][0] = self.value[i][0] * scalar
                i += 1
        elif (type(self.value[0]) == float):
            while (i < len(self.value)):
                self.value[i] = self.value[i] * scalar
                i += 1

    def __rmul__(self, scalar):
        i = 0
        if (type(self.value[0]) == list):
            while (i < len(self.value)):
                self.value[i][0] = scalar * self.value[i][0]
                i += 1
        elif (type(self.value[0]) == float):
            while (i < len(self.value)):
                self.value[i] = scalar * self.value[i]
                i += 1

    def __str__(self):
        return (str(self.value) + " " + str(self.shape))

    def __repr__(self):
        return (Vector(self.value))

    def T(self):
        if (type(self.value[0]) == list):
            new_values = []
            for values in self.value:
                new_values.append(values[0]);
            self.value = new_values;
            self.shape = (1, len(self.value))
        elif (type(self.value[0]) == float):
            new_values = []
            for values in self.value:
                new_values.append([values]);
            self.value = new_values;
            self.shape = (len(self.value), 1)

    def dot(self, vector2):
        if (self.shape == vector2.shape):
            if (type(self.value[0]) == list):
                result = 0
                i = 0
                while (i < len(self.value)):
                    result += self.value[i][0] * vector2.value[i][0]
                    i += 1
                return result
            elif (type(self.value[0]) == float):
                result = 0
                i = 0
                while (i < len(self.value)):
                    result += self.value[i] * vector2.value[i]
                    i += 1
                return result ;
        else:
            print("The dot method works with two vectors of the same type.")
