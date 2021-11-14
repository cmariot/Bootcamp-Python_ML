# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    eval.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: cmariot <cmariot@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/11/13 15:25:03 by cmariot           #+#    #+#              #
#    Updated: 2021/11/14 18:13:02 by cmariot          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class Evaluator:
    def __init__(self, words, coeff):
        self.words = words
        self.coeff = coeff

    def zip_evaluate(coefs, words):
        if (len(coefs) != len(words)):
            print("-1")
            return ;
        else:
            result = zip(coefs, words)
            ret = 0
            for item in list(result):
                ret += len(item[0]) * item[1]
            print(ret)

    def enumerate_evaluate(coefs, words):
        if (len(coefs) != len(words)):
            print("-1")
            return ;
        else:
            ret = 0
            for index, word in enumerate(words):
                ret += len(word) * coefs[index]
            print(ret)

#if __name__ == "__main__":
#    words = ["Le", "Lorem", "Ipsum", "est", "simple"]
#    coefs = [1.0, 2.0, 1.0, 4.0, 0.5]
#    Evaluator.enumerate_evaluate(coefs, words)
