# -----------------------------------------------------------------
# Project Name:         Employee Discount System
# Name:                 Ong Jai Sheng
# -----------------------------------------------------------------

# --------------------------------------------------
# --------------------------------
# Function Name:       Display Total For The Day
# Function Purpose:    Display Accumulated Totals for the Day
# ----------------------------------------------------------------------------------


def Display_Total_For_The_Day(dblDayTotalBeforeDiscount, dblDayTotalAfterDiscount):
    
    print("")

    print("Total before Discount for the day: ", "${:,.2f}".format(dblDayTotalBeforeDiscount))
    print("Total after Discount applied: ", "${:,.2f}".format(dblDayTotalAfterDiscount))


# ----------------------------------------------------------------------------------
# Function Name:       Display Outputs
# Function Purpose:    Display Calculated Outputs
# ----------------------------------------------------------------------------------


def Display_Outputs(dblEmployeePercentages, dblYTDAmountDiscount, dblTotalPurchaseToday, dblEmployeeDiscount, dblTotalWithDiscount):

    print("")
    
    dblEmployeePercentages = dblEmployeePercentages * 100
    dblEmployeePercentages = int(dblEmployeePercentages)

    print("Employee Discount Percentage is ", dblEmployeePercentages,"%")
    print("Year-To-Date Amount of Discount in Dollars are ", "${:,.2f}".format(dblYTDAmountDiscount))
    print("Total Purchase Today before Discount are ", "${:,.2f}".format(dblTotalPurchaseToday))
    print("Discount Allowed For This Purchase are ", "${:,.2f}".format(dblEmployeeDiscount))
    print("Total Amount With Discount are ", "${:,.2f}".format(dblTotalWithDiscount))

    
# -------------------------------------------------------------------
# Function Name:       Accumulate Total Include Discount
# Function Purpose:    Will Accumulate Totals that Include Discount
# -------------------------------------------------------------------

def Accumulate_Total_Include_Discount(dblTotalWithDiscount, dblDayTotalAfterDiscount):

    dblDayTotalAfterDiscount += dblTotalWithDiscount

    return dblDayTotalAfterDiscount


# -------------------------------------------------------------------
# Function Name:       Accumulate Total Before Discount
# Function Purpose:    Will Accumulate Totals Before Discount
# -------------------------------------------------------------------

def Accumulate_Total_Before_Discount(dblTotalPurchaseToday, dblDayTotalBeforeDiscount):

    dblDayTotalBeforeDiscount += dblTotalPurchaseToday

    return dblDayTotalBeforeDiscount


#--------------------------------------------------------------------------
# Function Name:       Validate Next Employee
# Function Purpose:    Check for Another Employee
#--------------------------------------------------------------------------

def Validate_Next_Employees(strAnotherEmployee):

    if strAnotherEmployee == 'yes' or strAnotherEmployee == 'no':
        global strValidated
        strValidated = True
    else:
        print("Please Enter 'Yes' or 'No'")

    return strAnotherEmployee

# ----------------------------------------------------------------------------------
# Function Name:      Calculate Employee Discount
# Function Purpose:   Calculate Employee Discount for this Purchase
# ----------------------------------------------------------------------------------

def Calculate_Employee_Discount(dblYTDAmountDiscount, dblCurrentDiscount, dblEmployeeDiscount):

    if dblYTDAmountDiscount > 200:
        dblEmployeeDiscount = 0

    elif (dblYTDAmountDiscount + dblCurrentDiscount) < 200:
        dblEmployeeDiscount = dblCurrentDiscount

    elif (dblYTDAmountDiscount + dblCurrentDiscount) > 200:
         dblEmployeeDiscount = (dblYTDAmountDiscount + dblCurrentDiscount) - 200


    return dblEmployeeDiscount

# ----------------------------------------------------------------------------------
# Function Name:       Determine Manager Discount Percentage
# Function Purpose:    Determine Discount Percentage for Manager Status
# ----------------------------------------------------------------------------------

def Determine_Manager_Discount_Percentage(intYearsEmployed, dblEmployeePercentages):

    if intYearsEmployed > 15:
        dblEmployeePercentages = 0.4

    elif intYearsEmployed >= 11 and intYearsEmployed <= 15:
         dblEmployeePercentages = 0.35

    elif intYearsEmployed >= 7 and intYearsEmployed <= 10:
        dblEmployeePercentages = 0.3

    elif intYearsEmployed >= 4 and intYearsEmployed <= 6:
        dblEmployeePercentages = 0.24

    else:
        dblEmployeePercentages = 0.2

    return dblEmployeePercentages



# ----------------------------------------------------------------------------------
# Function Name:       Determine Employee Discount Percentage
# Function Purpose:    Determine Discount Percentage for Employee Status
# ----------------------------------------------------------------------------------

def Determine_Employee_Discount_Percentage( intYearsEmployed, dblEmployeePercentages):

    if intYearsEmployed > 15:
        dblEmployeePercentages = 0.3

    elif intYearsEmployed >= 11 and intYearsEmployed <= 15:
         dblEmployeePercentages = 0.25

    elif intYearsEmployed >= 7 and intYearsEmployed <= 10:
        dblEmployeePercentages = 0.2

    elif intYearsEmployed >= 4 and intYearsEmployed <= 6:
        dblEmployeePercentages = 0.14

    else:
        dblEmployeePercentages = 0.1

    return dblEmployeePercentages



# ----------------------------------------------------------------------------------
# Function Name:        Validate Total Today Purchase
# Function Purpose:     Validate the Total of Today's Purchase
# ----------------------------------------------------------------------------------

def Validate_Total_Today_Purchase(dblTotalPurchase):
    try:
        dblTotalPurchase = float(dblTotalPurchase)
        if (dblTotalPurchase >= 0):
            global strValidated
            strValidated = True
        else:
            print("Total of Today's Purchase Must Be Greater than Or Equal To 0")
    except ValueError:
        dblTotalPurchase = float(0)
        print("Total of Today's Purchase Is Required and Must Be Numeric")

    return dblTotalPurchase



# ----------------------------------------------------------------------------------
# Function Name:        Validate Total Amount Previous Purchase
# Function Purpose:     Validate the Total Amount Previous Purchase before Discount
# ----------------------------------------------------------------------------------

def Validate_Total_Amount_Previous_Purchase(dblTotalPreviousPurchases):
    try:
        dblTotalPreviousPurchases = float(dblTotalPreviousPurchases)
        if (dblTotalPreviousPurchases >= 0):
            global strValidated
            strValidated = True
        else:
            print("Total Amount of Previous Purchase before Discount Must Be Greater than Or Equal To 0")
    except ValueError:
        dblTotalPreviousPurchases = float(0)
        print("Total Amount of Previous Purchase before Discount Is Required and Must Be Numeric")

    return dblTotalPreviousPurchases



# -----------------------------------------------------------------
# Function Name:        Validate Number Of Years Employed
# Function Purpose:     Validate the Number of Years Employed
# -----------------------------------------------------------------

def Validate_Number_Of_Years_Employed(intYearsEmployed):
    try:
        intYearsEmployed = int(intYearsEmployed)
        if (intYearsEmployed > 0):
            global strValidated
            strValidated = True
        else:
            print("Number of Years Employed Must Be Greater than 0")
    except ValueError:
        intYearsEmployed = int(0)
        print("Number of Years Employed Is Required and Must Be Numeric")

    return intYearsEmployed



# -----------------------------------------------------------------
# Function Name:        Determine Employees Status 
# Function Purpose:     Validate and Determine Employee Status
# -----------------------------------------------------------------

def Determine_Employees_Status(strEmployeeStatus):

    if strEmployeeStatus == 'm' or strEmployeeStatus == 'e':
        global strValidated
        strValidated = True
    else:
        print("Please Enter 'M' or 'E'")

    return strEmployeeStatus



# -----------------------------------------------------------------
# Project 1: Main Processing Area   
# -----------------------------------------------------------------

# declare all input, output, and other needed variables

strEmployeeStatus = str("")
intYearsEmployed = int(0)
dblTotalPreviousPurchases = float(0)
dblTotalPurchase = float(0)
strAnotherEmployee = str("yes")

dblEmployeePercentages = float(0)
dblYTDAmountDiscount = float(0)
dblTotalPurchaseToday = float(0)
dblEmployeeDiscount = float(0)
dblCurrentDiscount = float(0)
dblTotalWithDiscount = float(0)

dblDayTotalBeforeDiscount = float(0)
dblDayTotalAfterDiscount = float(0)


while strAnotherEmployee == "yes":

    print("")
    print("")

# call function to determine employees role

    strValidated = bool(False)

    while strValidated is False:
        strEmployeeStatus = input("Are You A Manager Or Employee (Type M or E): ")
        strEmployeeStatus = strEmployeeStatus.lower()
        strEmployeeStatus = Determine_Employees_Status(strEmployeeStatus)


# call function to validate Employee Years Employed

    strValidated = bool(False)

    while strValidated is False:
        intYearsEmployed = input("Enter The Number of Years Employed: ")
        intYearsEmployed = Validate_Number_Of_Years_Employed(intYearsEmployed)


# call function to validate Total Amount of Previous Purchase before Discount

    strValidated = bool(False)

    while strValidated is False:
        dblTotalPreviousPurchases = input("Enter the Total Amount of Previous Purchases before Discount: ")
        dblTotalPreviousPurchases = Validate_Total_Amount_Previous_Purchase(dblTotalPreviousPurchases)


# call function to validate Total of Today's Purchase

    strValidated = bool(False)

    while strValidated is False:
        dblTotalPurchase = input("Enter the Total of Today's Purchase: ")
        dblTotalPurchase = Validate_Total_Today_Purchase(dblTotalPurchase)


# Determine Employee Discount Percentage

    if strEmployeeStatus == 'm':
        dblEmployeePercentages = Determine_Manager_Discount_Percentage(intYearsEmployed, dblEmployeePercentages)
    else:      
        dblEmployeePercentages = Determine_Employee_Discount_Percentage(intYearsEmployed, dblEmployeePercentages)


# Calculate Year-To-Date Amount of Discount In Dollars

    dblYTDAmountDiscount = dblTotalPreviousPurchases * dblEmployeePercentages


# Calculate Total Purchase Today Before Discount

    dblTotalPurchaseToday = dblTotalPurchase


# Calculate Employee Discount For Current Purchase

    dblCurrentDiscount = dblTotalPurchaseToday * dblEmployeePercentages

    dblEmployeeDiscount = Calculate_Employee_Discount(dblYTDAmountDiscount, dblCurrentDiscount, dblEmployeeDiscount)


# Calculate Total With Discount

    dblTotalWithDiscount = dblTotalPurchaseToday - dblEmployeeDiscount

# call function that display Total Travel Costs, Total Amount Reimbursed and Total Employees Responsible Amount 
    
    Display_Outputs(dblEmployeePercentages, dblYTDAmountDiscount, dblTotalPurchaseToday, dblEmployeeDiscount, dblTotalWithDiscount)


# call function to accumulate Totals for the Day

    dblDayTotalBeforeDiscount = Accumulate_Total_Before_Discount(dblTotalPurchaseToday, dblDayTotalBeforeDiscount)
    dblDayTotalAfterDiscount = Accumulate_Total_Include_Discount(dblTotalWithDiscount, dblDayTotalAfterDiscount)

# call function to validate inputs for next employees

    strValidated = bool(False)

    while strValidated is False:
        strAnotherEmployee = input("Is There Another Employee? (Yes or No): ")
        strAnotherEmployee = strAnotherEmployee.lower()
        strAnotherEmployee = Validate_Next_Employees(strAnotherEmployee)


Display_Total_For_The_Day(dblDayTotalBeforeDiscount, dblDayTotalAfterDiscount)


