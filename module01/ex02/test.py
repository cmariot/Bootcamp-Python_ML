# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    test.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: cmariot <cmariot@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/11/09 23:56:10 by cmariot           #+#    #+#              #
#    Updated: 2021/11/10 23:57:49 by cmariot          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from vector import Vector

if __name__ == "__main__":

    # INIT
    v0 = Vector([[0.0], [1.0], [2.0], [3.0]])
    v1 = Vector([[10.0], [2.0], [3.0], [4.0]])
    v2 = Vector([0.0, 1.0, 2.0, 3.0])
    v3 = Vector([10.0, 2.0, 3.0, 4.0])
    v4 = Vector(3)
    v5 = Vector(range(10, 15))
    v6 = Vector(range(15, 20))

    #PRINT ATTRIBUTES
    print(v0.value)
    print(v0.shape)

    # METHODS
    v0.__add__(v1);
    v2.__add__(v3);

    v0.__radd__(v1);
    v2.__radd__(v3);

    v1.__sub__(v0);
    v3.__sub__(v2);

    v0.__rsub__(v1);
    v2.__rsub__(v3);

    v0.__truediv__(5);
    v2.__truediv__(5);

    v0.__rtruediv__(5);
    v2.__rtruediv__(5);

    v0.__mul__(5);
    v2.__mul__(5);

    v0.__rmul__(5);
    v2.__rmul__(5);

    v0.T()
    v2.T()

    result = v1.dot(v2)
    result = v0.dot(v3)

    v0.__str__()
    v0.__repr__()
