#!/usr/bin/env python3
# Created by: Carolyn Webster Pless
# Created on: 2022/10/03
# Takes user input for the subtotal and displays
# the tax and total back to the user with the GST
# being from Nunavut

# importing the GST constant in the constant.py file
import constant


def main():

    # title
    print("Cost and Tax in Nunavut")

    # input for the subtotal
    cost = int(input("Enter the subtotal of your item: "))

    # calculations
    tax = cost * constant.GST
    total = cost + tax

    # display the calculations back to the user
    print("The tax is {}!".format(tax))
    print("The total is {}!".format(total))


if __name__ == "__main__":
    main()
