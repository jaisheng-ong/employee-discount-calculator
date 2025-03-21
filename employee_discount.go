package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

// DisplayTotalForTheDay displays accumulated totals for the day
func DisplayTotalForTheDay(dayTotalBeforeDiscount, dayTotalAfterDiscount float64) {
	fmt.Println()
	fmt.Printf("Total before Discount for the day: $%.2f\n", dayTotalBeforeDiscount)
	fmt.Printf("Total after Discount applied: $%.2f\n", dayTotalAfterDiscount)
}

// DisplayOutputs displays calculated outputs
func DisplayOutputs(employeePercentage, ytdAmountDiscount, totalPurchaseToday, employeeDiscount, totalWithDiscount float64) {
	fmt.Println()
	
	// Convert percentage to integer for display
	employeePercentageInt := int(employeePercentage * 100)
	
	fmt.Printf("Employee Discount Percentage is %d%%\n", employeePercentageInt)
	fmt.Printf("Year-To-Date Amount of Discount in Dollars are $%.2f\n", ytdAmountDiscount)
	fmt.Printf("Total Purchase Today before Discount are $%.2f\n", totalPurchaseToday)
	fmt.Printf("Discount Allowed For This Purchase are $%.2f\n", employeeDiscount)
	fmt.Printf("Total Amount With Discount are $%.2f\n", totalWithDiscount)
}

// AccumulateTotalIncludeDiscount accumulates totals that include discount
func AccumulateTotalIncludeDiscount(totalWithDiscount, dayTotalAfterDiscount float64) float64 {
	return dayTotalAfterDiscount + totalWithDiscount
}

// AccumulateTotalBeforeDiscount accumulates totals before discount
func AccumulateTotalBeforeDiscount(totalPurchaseToday, dayTotalBeforeDiscount float64) float64 {
	return dayTotalBeforeDiscount + totalPurchaseToday
}

// ValidateNextEmployees checks for another employee
func ValidateNextEmployees(anotherEmployee string) (string, bool) {
	anotherEmployee = strings.ToLower(anotherEmployee)
	if anotherEmployee == "yes" || anotherEmployee == "no" {
		return anotherEmployee, true
	}
	fmt.Println("Please Enter 'Yes' or 'No'")
	return anotherEmployee, false
}

// CalculateEmployeeDiscount calculates employee discount for this purchase
func CalculateEmployeeDiscount(ytdAmountDiscount, currentDiscount float64) float64 {
	if ytdAmountDiscount > 200 {
		return 0
	} else if (ytdAmountDiscount + currentDiscount) < 200 {
		return currentDiscount
	} else {
		return (ytdAmountDiscount + currentDiscount) - 200
	}
}

// DetermineManagerDiscountPercentage determines discount percentage for manager status
func DetermineManagerDiscountPercentage(yearsEmployed int) float64 {
	if yearsEmployed > 15 {
		return 0.4
	} else if yearsEmployed >= 11 && yearsEmployed <= 15 {
		return 0.35
	} else if yearsEmployed >= 7 && yearsEmployed <= 10 {
		return 0.3
	} else if yearsEmployed >= 4 && yearsEmployed <= 6 {
		return 0.24
	} else {
		return 0.2
	}
}

// DetermineEmployeeDiscountPercentage determines discount percentage for employee status
func DetermineEmployeeDiscountPercentage(yearsEmployed int) float64 {
	if yearsEmployed > 15 {
		return 0.3
	} else if yearsEmployed >= 11 && yearsEmployed <= 15 {
		return 0.25
	} else if yearsEmployed >= 7 && yearsEmployed <= 10 {
		return 0.2
	} else if yearsEmployed >= 4 && yearsEmployed <= 6 {
		return 0.14
	} else {
		return 0.1
	}
}

// ValidateTotalTodayPurchase validates the total of today's purchase
func ValidateTotalTodayPurchase(input string) (float64, bool) {
	totalPurchase, err := strconv.ParseFloat(input, 64)
	if err != nil {
		fmt.Println("Total of Today's Purchase Is Required and Must Be Numeric")
		return 0, false
	}
	
	if totalPurchase >= 0 {
		return totalPurchase, true
	}
	
	fmt.Println("Total of Today's Purchase Must Be Greater than Or Equal To 0")
	return 0, false
}

// ValidateTotalAmountPreviousPurchase validates the total amount of previous purchase
func ValidateTotalAmountPreviousPurchase(input string) (float64, bool) {
	totalPreviousPurchases, err := strconv.ParseFloat(input, 64)
	if err != nil {
		fmt.Println("Total Amount of Previous Purchase before Discount Is Required and Must Be Numeric")
		return 0, false
	}
	
	if totalPreviousPurchases >= 0 {
		return totalPreviousPurchases, true
	}
	
	fmt.Println("Total Amount of Previous Purchase before Discount Must Be Greater than Or Equal To 0")
	return 0, false
}

// ValidateNumberOfYearsEmployed validates the number of years employed
func ValidateNumberOfYearsEmployed(input string) (int, bool) {
	yearsEmployed, err := strconv.Atoi(input)
	if err != nil {
		fmt.Println("Number of Years Employed Is Required and Must Be Numeric")
		return 0, false
	}
	
	if yearsEmployed > 0 {
		return yearsEmployed, true
	}
	
	fmt.Println("Number of Years Employed Must Be Greater than 0")
	return 0, false
}

// DetermineEmployeesStatus validates and determines employee status
func DetermineEmployeesStatus(input string) (string, bool) {
	input = strings.ToLower(input)
	if input == "m" || input == "e" {
		return input, true
	}
	
	fmt.Println("Please Enter 'M' or 'E'")
	return "", false
}

// getInput reads a line from standard input
func getInput(prompt string) string {
	reader := bufio.NewReader(os.Stdin)
	fmt.Print(prompt)
	input, _ := reader.ReadString('\n')
	return strings.TrimSpace(input)
}

func main() {
	// Declare all input, output, and other needed variables
	var employeeStatus string
	var yearsEmployed int
	var totalPreviousPurchases float64
	var totalPurchase float64
	anotherEmployee := "yes"
	
	var employeePercentage float64
	var ytdAmountDiscount float64
	var totalPurchaseToday float64
	var employeeDiscount float64
	var currentDiscount float64
	var totalWithDiscount float64
	
	var dayTotalBeforeDiscount float64 = 0
	var dayTotalAfterDiscount float64 = 0
	
	for anotherEmployee == "yes" {
		fmt.Println()
		fmt.Println()
		
		// Determine employee role
		validated := false
		for !validated {
			input := getInput("Are You A Manager Or Employee (Type M or E): ")
			employeeStatus, validated = DetermineEmployeesStatus(input)
		}
		
		// Validate employee years employed
		validated = false
		for !validated {
			input := getInput("Enter The Number of Years Employed: ")
			yearsEmployed, validated = ValidateNumberOfYearsEmployed(input)
		}
		
		// Validate total amount of previous purchase
		validated = false
		for !validated {
			input := getInput("Enter the Total Amount of Previous Purchases before Discount: ")
			totalPreviousPurchases, validated = ValidateTotalAmountPreviousPurchase(input)
		}
		
		// Validate total of today's purchase
		validated = false
		for !validated {
			input := getInput("Enter the Total of Today's Purchase: ")
			totalPurchase, validated = ValidateTotalTodayPurchase(input)
		}
		
		// Determine employee discount percentage
		if employeeStatus == "m" {
			employeePercentage = DetermineManagerDiscountPercentage(yearsEmployed)
		} else {
			employeePercentage = DetermineEmployeeDiscountPercentage(yearsEmployed)
		}
		
		// Calculate year-to-date amount of discount in dollars
		ytdAmountDiscount = totalPreviousPurchases * employeePercentage
		
		// Calculate total purchase today before discount
		totalPurchaseToday = totalPurchase
		
		// Calculate employee discount for current purchase
		currentDiscount = totalPurchaseToday * employeePercentage
		employeeDiscount = CalculateEmployeeDiscount(ytdAmountDiscount, currentDiscount)
		
		// Calculate total with discount
		totalWithDiscount = totalPurchaseToday - employeeDiscount
		
		// Display outputs
		DisplayOutputs(employeePercentage, ytdAmountDiscount, totalPurchaseToday, employeeDiscount, totalWithDiscount)
		
		// Accumulate totals for the day
		dayTotalBeforeDiscount = AccumulateTotalBeforeDiscount(totalPurchaseToday, dayTotalBeforeDiscount)
		dayTotalAfterDiscount = AccumulateTotalIncludeDiscount(totalWithDiscount, dayTotalAfterDiscount)
		
		// Validate inputs for next employees
		validated = false
		for !validated {
			input := getInput("Is There Another Employee? (Yes or No): ")
			anotherEmployee, validated = ValidateNextEmployees(input)
		}
	}
	
	// Display total for the day
	DisplayTotalForTheDay(dayTotalBeforeDiscount, dayTotalAfterDiscount)
} 