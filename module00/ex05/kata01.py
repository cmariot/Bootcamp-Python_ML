# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    kata01.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: cmariot <cmariot@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/11/08 17:16:46 by cmariot           #+#    #+#              #
#    Updated: 2021/11/08 17:16:47 by cmariot          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

if __name__ == "__main__":
    languages = {
        'Python': 'Guido van Rossum',
        'Ruby': 'Yukihiro Matsumoto',
        'PHP': 'Rasmus Lerdorf',
        }
    for key, value in languages.items():
        print(key, "was created by", value)
