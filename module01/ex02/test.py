# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    test.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: cmariot <cmariot@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/11/09 23:56:10 by cmariot           #+#    #+#              #
#    Updated: 2021/11/11 02:28:38 by cmariot          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from vector import Vector

# Run with "python test.py"
if __name__ == "__main__":

    # INIT
    # Different types to init a vector
    v0 = Vector([[0.0], [1.0], [2.0], [3.0]])
    v1 = Vector([[10.0], [2.0], [3.0], [4.0]])
    v2 = Vector([0.0, 1.0, 2.0, 3.0, 4.0])
    v3 = Vector([10.0, 2.0, 3.0, 4.0])
    v4 = Vector(3)
    v5 = Vector(range(4, 9))
    v6 = Vector(range(2, 7))

    print("PRINT THE VECTORS AFTER THE INIT")
    print(v0)
    print(v1)
    print(v2)
    print(v3)
    print(v6)
    print(v4)
    print(v5)

    # A Vector have 2 attributes
    # Attribute value = x1, x2, x3 ... xn
    # Attribute shape = if type v0 or v1 (number of value , 1) for vector columns
    #                   else (1, number of value) for vector rows

    # [[0.0], [1.0], [2.0], [3.0]] (4, 1)
    # [[1.0], [2.0], [3.0], [4.0]] (4, 1)
    # [0.0, 1.0, 2.0, 3.0] (1, 4)
    # [10.0, 2.0, 3.0, 4.0] (1, 4)
    # [[0.0], [1.0], [2.0]] (3, 1)
    # [[10.0], [11.0], [12.0], [13.0], [14.0]] (5, 1)
    # [[15.0], [16.0], [17.0], [18.0], [19.0]] (5, 1)
    # [[0.0], [1.0], [2.0], [3.0]]


    print("\nPRINT ATTRIBUTES")
    print(v0.value)
    print(v0.shape)

    # METHODS
    # Like function on Vector 
    # Addition, substraction, division, multiplication, Transpose or dot product between two vectors of same shape
    print("Addition")
    print(v0.__str__())
    v0.__add__(v1);
    print(v0.__str__())
    v0.__str__()
    print()


    v2.__add__(v3);

    # Return addition
    #v0.__radd__(v1);
    #v2.__radd__(v3);

    # Substraction
    v1.__sub__(v0);
    v3.__sub__(v2);

    # Return addition
    #v0.__rsub__(v1);
    #v2.__rsub__(v3);

    # Division
    v0.__truediv__(5);
    v2.__truediv__(5);

    # Return addition
    #v0.__rtruediv__(5);
    #v2.__rtruediv__(5);

    # Multiplication
    v0.__mul__(5);
    v2.__mul__(5);

    # Return addition
    v0.__rmul__(5);
    v2.__rmul__(5);

    # Transpose
    v0.T()
    v2.T()

    # Dot product between two vectors of same shape
    #result = v1.dot(v2)
    result = v0.dot(v3)

    # Print Vector
    v0.__str__()

    # Return Vector
    v0.__repr__()

    print("END")

# Go to vector.py to see the Class !
