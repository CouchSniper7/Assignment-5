# Functions

# CONSTANTS
minimumDrinkingAge = 18

## Displays my unique place of birth         ----
# no param                                      |
# @ return my place of birth                    #pg 21 of PP
#                                            ---
def yourPlaceOfBirth() :                    #--
    return "Lutz, Florida"                  # pg33 of PP


## This function takes a value j that you pass it then returns j 7 times 
# @param j 
# @return j after 7 times
#
def septapalooza(j, timesReturned = 7) : 
    if timesReturned == 0 :
        return 0
    return j + septapalooza(j, timesReturned -1)
    

## this function takes a value age that you pass it. If the age is greater than or equal to 18 the function returns True, otherwise it returns False. 
# @param age
# @ return true or fals based on user input
#
def oldEnoughToDrink(age) :
    return age >= minimumDrinkingAge 
     


def main():                                              #pg 67 of PP
    print("Function 1 - yourPlaceOfBirth()")
    print(yourPlaceOfBirth())

    print("\nFunction 2 - septapalooza(7)")
    print(septapalooza(7))

    print("\nFunction 3 - oldEnoughToDrink(age)")
    age = int(input("Please enter your age: "))
    print(oldEnoughToDrink(age))

main()



