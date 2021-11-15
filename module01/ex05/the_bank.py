# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    the_bank.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: cmariot <cmariot@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/11/14 18:15:18 by cmariot           #+#    #+#              #
#    Updated: 2021/11/15 15:44:10 by cmariot          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class Account(object):
    
    """The account"""
    
    ID_COUNT = 1

    def __init__(self, name, **kwargs):
        self.id = self.ID_COUNT
        self.name = name
        self.__dict__.update(kwargs)
        if hasattr(self, 'value'):
            self.value = 0
        Account.ID_COUNT += 1

    def transfer(self, amount):
        self.value += amount


class Bank(object):
    
    """The bank"""
    
    def __init__(self):
        self.account = []
    
    def add(self, account):
        self.account.append(account)
    
    def transfer(self, origin, dest, amount):
        """
        @origin:  int(id) or str(name) of the first account
        @dest:    int(id) or str(name) of the destination account
        @amount:  float(amount) amount to transfer
        @return         True if success, False if an error occured
        """
        print("SECURE TRANSFER PROTOTCOL")
        #Check the type of origin
        if (type(origin) != int and type(origin) != str):
            print("ERROR")
            return (False)
        #Check the type of dest
        if (type(dest) != int and type(dest) != str):
            print("ERROR")
            return (False)
        #Check the type of amount and if amount > 0
        if (type(amount) == int):
            amount = float(amount)
        if (type(amount) != float):
            print("ERROR")
            return (False)
        if (amount < 0):
            print("ERROR")
            return (False)
        #Check if the origin name / ID is avalable in the bank
        found = 0
        i = 0
        while i < len(self.account):
            if origin == self.account[i].name or origin == self.account[i].id:
                found = 1
                break ;
            i += 1
        if (found == 1):
            origin = self.account[i]
        else:
            print("ERROR")
            return (False)
        #Check if the dest name / ID is avalable in the bank
        found = 0
        i = 0
        while i < len(self.account):
            if dest == self.account[i].name or dest == self.account[i].id:
                found = 1
                break ;
            i += 1
        if (found == 1):
            dest = self.account[i]
        else:
            print("ERROR")
            return (False)
        #Check if the origin or the dest account aren't corrupted
        #Type of accounts must be Account
        if type(origin) != Account or type(dest) != Account:
            print("ERROR")
        #They must have an even number of attributes
        if len(origin.__dict__) % 2 == 0 or len(dest.__dict__) % 2 == 0:
            print("ERROR")
        #No attributes must begin by 'b', 'zip' or 'addr'
        #The accounts must have the attributes 'name', 'id' and 'value'
        correct_attribute = 0
        for items in origin.__dict__:
            if items[0] == 'b' or items[0:2] == 'zip' or items[0:3] == 'addr':
                print("ERROR")
                return (False)
            if items == 'value':
                correct_attribute += 1
            elif items == 'name':
                correct_attribute += 1
            elif items == 'id':
                correct_attribute += 1
        if correct_attribute != 3:
            print("ERROR")
            return (False)
        correct_attribute = 0
        for items in dest.__dict__:
            if items[0] == 'b' or items[0:2] == 'zip' or items[0:3] == 'addr':
                print("ERROR")
                return (False)
            if items == 'value':
                correct_attribute += 1
            elif items == 'name':
                correct_attribute += 1
            elif items == 'id':
                correct_attribute += 1
        if correct_attribute != 3:
            print("ERROR")
            return (False)
        #Make the transfer if enough money to do it
        if origin.value < amount:
            print("ERROR")
            return (False)
        else:
            origin.value -= amount
            dest.value += amount
            return(True)

    def fix_account(self, account):
        """
        fix the corrupted account
        @account: int(id) or str(name) of the account
        @return         True if success, False if an error occured
        """

if __name__ == "__main__":
    #Create a bank
    mybank = Bank()
    #Create an account
    myaccount = Account("Charles", value="")
    #Add the account to the bank
    mybank.add(myaccount)
    #Add money on the account
    myaccount.transfer(1000)
    #Create another account
    myclientaccount = Account("Ulysse", value="")
    #Add the account to the bank
    mybank.add(myclientaccount)
    #Add money on the account
    myclientaccount.transfer(1000)

    #Before tranfer
    print("MYACCOUNT = " + str(myaccount.value))
    print("MYCLIENTACCOUNT = " + str(myclientaccount.value))

    mybank.transfer("Ulysse", "Charles", 500)

    #After transfer
    print("MYACCOUNT = " + str(myaccount.value))
    print("MYCLIENTACCOUNT = " + str(myclientaccount.value))
