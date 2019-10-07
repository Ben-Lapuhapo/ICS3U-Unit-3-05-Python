#!/usr/bin/env python3

# Created by: Ben Lapuhapo
# Created on: September 30 2019
# This program checks the Month


def main():
    # Input
    month_num = input("Enter Number from 1-12: ")
    print("")

    # Process and Output
    if month_num == "1":
        print("It's January!")
    elif month_num == "2":
        print("It's February!")
    elif month_num == "3":
        print("It's March!")
    elif month_num == "4":
        print("It's April!")
    elif month_num == "5":
        print("It's May!")
    elif month_num == "6":
        print("It's June!")
    elif month_num == "7":
        print("It's July!")
    elif month_num == "8":
        print("It's August!")
    elif month_num == "9":
        print("It's September!")
    elif month_num == "10":
        print("It's October!")
    elif month_num == "11":
        print("It's November!")
    elif month_num == "12":
        print("It's December!")
    else:
        print("Not A Month.")


if __name__ == "__main__":
    main()
