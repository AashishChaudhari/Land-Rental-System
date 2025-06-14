#operation.py
import write
import read
# Function to prompt user to select an option
def select_option():
    while True:
        try:
            chosen_option = int(input("Please select your desired service option: "))
            return chosen_option
        except ValueError:
            print("Only integer is accepted.")
# Function to display the table of available land
def display_table():
    write.welcome_message()
     # Print table header
    print("Kitta \t City \t    Direction  Anna  \t Price \t Availability")
    print("#############################################################################################################################################################################################################################")
    land_data = read.table_details()
    # Get land data from file
    for key, value in land_data.items():# Print land data
        print(key, end="\t")
        for v in value:
            print(v, end="\t")
        print("\n")

# Function to collect client information        
def client_information():
    try:
        name_of_client = input("Please enter your name: ")
        address_of_client = input("Please enter your address: ")
        number_of_client = int(input("Please enter your phone number: "))
    except ValueError:
        print("Please provide correct data")
        number_of_client = int(input("Please enter your phone number: "))
    return name_of_client, address_of_client, number_of_client
# Function to prompt user for kitta number
def kitta_number():
    kitta_number = input("Please enter the desired land's kitta number: ")
    return kitta_number

# Function to input rental duration
def input_rent_duration():
    try:
        rent_duration = int(input("Enter the rental duration (in months):"))
        while rent_duration < 1:
            print("Valid number of months required")
            rent_duration = int(input("Enter the rental duration (in months):"))
    except ValueError:
        print("Only integers are accepted.")
        rent_duration = int(input("Enter the rental duration (in months):"))
    
    return rent_duration

# Function to input rented months
def input_rented_months():
    try:
        rented_months = int(input("Please enter the number of months you rented the land: "))
        while rented_months < 1:
            print("Valid number of months rerquired")
            rented_months = int(input("Please enter the number of months you rented the land: "))
    except ValueError:
        print("Only integer is accepted.")
        rented_months = int(input("Please enter the number of months you rented the land: "))
    
    return rented_months

# Function to prompt user if they want to continue renting
def rent_continuation():
    while True:
        try:
            continue_renting = input("Do you want to continue renting?(Yes/No): ")
            if continue_renting.lower() not in ['yes', 'no']:
                print("Invalid input. Please enter 'Yes' or 'No'")
            else:
                break
        except ValueError as error:
            print(error)
    return continue_renting

# Function to input returned months
def input_returned_months():
    try:
        returned_months = int(input("Please enter the number of months since it has been since you crossed the due date: "))
        while returned_months < 1:
            print("Valid number of months rerquired")
            returned_months = int(input("Please enter the number of months since it has been since you crossed the due date: "))
    except ValueError:
        print("Only integer is accepted.")
        returned_months = int(input("Please enter the number of months since it has been since you crossed the due date: "))
    
    return returned_months
# Function to prompt user if they want to continue returning
def return_continuation():
    while True:
        try:
            continue_renturning = input("Do you want to continue renturning?(Yes/No): ")
            if continue_renturning.lower() not in ['yes', 'no']:
                print("Invalid input. Please enter 'Yes' or 'No'")
            else:
                break
        except ValueError as error:
            print(error)
    return continue_renturning


