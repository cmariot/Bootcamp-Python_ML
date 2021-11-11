# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    test.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: cmariot <cmariot@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/11/09 23:56:10 by cmariot           #+#    #+#              #
#    Updated: 2021/11/11 17:31:40 by cmariot          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from vector import Vector

# Operation on Vector objects, using class, method 
# Run with "python test.py"
if __name__ == "__main__":

    # INIT
    # Different types to init a vector
    v0 = Vector([0.0, 1.0, 2.0, 3.0])
    v1 = Vector([0.0, 1.0, 2.0, 3.0])
    v2 = Vector([[0.0], [1.0], [2.0], [3.0]])
    v3 = Vector([[1.0], [2.0], [3.0], [4.0]])
    v4 = Vector(4) #[[0.0], [1.0], [2.0]] (3, 1)
    v5 = Vector(range(0, 4)) #[[4.0], [5.0], [6.0], [7.0], [8.0]] (5, 1)
    v6 = Vector(range(1, 5)) #[[2.0], [3.0], [4.0], [5.0], [6.0]] (5, 1)

    print("PRINT THE VECTORS AFTER THE INIT")
    print("v0 = ", v0)
    print("v1 = ", v1)
    print("v2 = ", v2)
    print("v3 = ", v3)
    print("v4 = ", v4)
    print("v5 = ", v5)
    print("v6 = ", v6)

    # A Vector have 2 attributes :
    # Attribute value = [[x1], [x2], [x3] ... [xn]]
    # and 
    # Attribute shape = if it's a vector column (number of value , 1) or
    #                   (1, number of value) for vector row

    # v0 =  [0.0, 1.0, 2.0, 3.0] (1, 4)
    # v1 =  [0.0, 1.0, 2.0, 3.0] (1, 4)
    # v2 =  [[0.0], [1.0], [2.0], [3.0]] (4, 1)
    # v3 =  [[1.0], [2.0], [3.0], [4.0]] (4, 1)
    # v4 =  [[0.0], [1.0], [2.0], [3.0]] (4, 1)
    # v5 =  [[0.0], [1.0], [2.0], [3.0]] (4, 1)
    # v6 =  [[1.0], [2.0], [3.0], [4.0]] (4, 1)[0.0], [1.0], [2.0], [3.0]] (4, 1)

    print("\nPRINT ATTRIBUTES")
    print(v0.value)
    print(v0.shape)
    print()

    # METHODS
    # Like function on Vecto, definitions in vector.py
    # Addition, substraction, division, multiplication, Transpose or dot product between two vectors of same shape
    print("OPERATIONS")
    print("Addition")
    print(v0.__str__(), " + ", v1.__str__(),  " = ", end="") 
    v0.__add__(v1);
    print(v0.__str__())
    v0.__str__()


    v2.__add__(v3);

    # Return addition
    v0.__radd__(v1);
    v2.__radd__(v3);

    # Substraction
    print("Substraction")
    v1.__sub__(v0);
    v3.__sub__(v2);
    print("v3 - v2 = " + v3.__str__())

    # Return substraction
    v0.__rsub__(v1);
    v2.__rsub__(v3);

    # Multiplication
    print("Multiplication")
    v1 = Vector([[0.0], [1.0], [2.0], [3.0]])
    v1.__mul__(5)
    print("v1 * 5 = " + v1.__str__())

    # Return multiplication
    v0.__rmul__(5);
    v2.__rmul__(5);

    # Division
    print("Division");
    v0.__truediv__(5);
    v2.__truediv__(5);
    print("v2 / 5 =" + v2.__str__())

    # Return division
    v2.__rtruediv__(3.14);
    #v2.__rtruediv__(5);

    # Transpose
    print("Transposition")
    
    print("v0 = ", v0)
    v0.T()
    print ("v0.t()")
    print("v0 = ", v0)
    v2.T()

    # Dot product between two vectors of same shape
    # x.y = x1.x1 + ... + xn.yn
    print("Dot product")
    print(v6.__str__() + " dot " + v3.__str__() + " = ", end="")
    result = v6.dot(v3)
    print(result.__str__())

    # Print Vector
    v0.__str__()

    # Return Vector
    v0.__repr__()

# Go to vector.py to see the Class !
