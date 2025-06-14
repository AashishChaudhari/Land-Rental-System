#write.py
import read
import operations

# Function to display a welcome message
def welcome_message():
    print("########################################################################################################################################################")
    print("\t\t\t\t\t\t\tTechno Property Nepal\n")
    print("########################################################################################################################################################")
    print("\t\t\t\t\t\tLalitpur,Nepal || phone no: 9823467098\n")
    print("########################################################################################################################################################")
    print("\t\t\t\t\t\t\tHope you have a great day!!!\n")
    print("########################################################################################################################################################")
  # Function to display options to the user  
def show_options():
    print("1. Display all the available lands\n")
    print("2. Rent the available lands\n")
    print("3. Return your rented piece of land/lands\n")
    print("4. Exit")
    print("#######################################################################################################################################################")
    
# Function to handle renting land and generating bills
def rent_land_and_bill():
    rented_land_details = []
    land_info = read.table_details()
    land_numbers = list(land_info.keys())
      # Get client information
    name_of_client, address_of_client, number_of_client = operations.client_information()
    looping = True
    while looping:
        loop = True
        while loop:
            kitta_number = operations.kitta_number()
            while kitta_number not in land_numbers:
                print("Invalid!")
                kitta_number = input("Kitta number: ")
            availability = land_info[kitta_number][4]
            if availability == "Not Available":
                print("It is not available for rent.")
            else:
                loop = False
         # Input rent duration
        rent_duration = operations.input_rent_duration()
        total_rent = int(land_info[kitta_number][3]) * rent_duration

        renting_land = land_info[kitta_number]
        rented = [kitta_number, renting_land[0], renting_land[1], renting_land[2], renting_land[3], rent_duration, total_rent]
        rented_land_details.append(rented)
        renting_land[4] = "Not Available"
         # Update land availability in file
        with open("LandRentalSystem.txt", "w") as file:
            for key, value in land_info.items():
                file.write(key + "," + value[0] + "," + value[1] + "," + value[2] + "," + value[3] + "," + value[4])
                file.write("\n")
        ans = operations.rent_continuation()
        if ans == "no":
            looping = False
    
    grand = sum(sublist[-1] for sublist in rented_land_details)
    # Printing Bills
    import datetime
    year = datetime.datetime.now().year
    month = datetime.datetime.now().month
    day = datetime.datetime.now().day
    hour = datetime.datetime.now().hour
    minute = datetime.datetime.now().minute
    second = datetime.datetime.now().second
    day_time = str(year) + "-" + str(month) + "-" + str(day) + " " + str(hour) + ":" + str(minute) + ":" + str(second)
    unique = str(year) + str(month) + str(day) + str(hour) + str(minute) + str(second)
    txtfilename = name_of_client + "@" + unique + ".txt"
    # Printing the bill
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("\n")
    print("                                                    Techno property Nepal !!!!!" + "\n")
    print("\n")                                                 
    print("\n")
    print("        Location       :  Kamal Pokhari" +  "                           Contact number :  01-4445671" + "\n")
    print("\n")
    print("\n")
    print("                                                ************** "+ "\n")
    print("                                                 Bill details "     +"\n")
    print("                                                ************** " +"\n")
    print("\n")    
    print("Bill No. : " + unique + "\n")
    print("")
    print("Name of Client: " + name_of_client + "\n")
    print("Address: " + address_of_client + "\n")
    print("Phone Number: " + str(number_of_client) + "\n")
    print("*************************************************************************************************************************************************************")
    print("Kitta\t City       Direction   Anna   Price  Month\tTotal\n")
    print("************************************************************************************************************************************************************")
    # To print the bill
    for row in rented_land_details:
        # Iterate over each element in the row
        for element in row:
            print(str(element), end='\t')
        # Move to the next line after printing each row
        print()
    print("***********************************************************************************************************************************************************")
    print("Grand Total: Rs.", grand, "\n")

    # Creating a new .txt bill with unique bill number

    file = open(txtfilename, "w")
    file.write("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    file.write("\n")
    file.write("                                                    Techno property Nepal" + "\n")
    file.write("\n")                                                 
    file.write("\n")
    file.write("        Location       :  Kamal Pokhari" +  "                           Contact number :  01-4445671" + "\n")
    file.write("\n")
    file.write("\n")
    file.write("                                                ************** "+ "\n")
    file.write("                                                 Bill details "     +"\n")
    file.write("                                                ************** " +"\n")
    file.write("############################################################################################################################################################/n")
    file.write("Bill No.: " + unique + "\n")
    file.write("#############################################################################################################################################################\n")
    file.write("Name of Client: " + name_of_client + "\n")
    file.write("Address: " + address_of_client + "\n")
    file.write("Phone Number: " + str(number_of_client) + "\n")
    file.write("##############################################################################################################################################################\n")
    file.write("Details: ")
    file.write("##############################################################################################################################################################\n")
    file.write("Kitta \t City \t\t Direction\t    Anna  \tPrice    Month\t\tTotal\n")
    file.write("#################################################################################################################################################################\n")

    for rows in rented_land_details:
        for items in rows:
            file.write(str(items) + "\t\t")
        file.write("\n")

    file.write("################################################################################################################################################################\n")
    file.write("Grand Total: Rs." + str(grand) + "\n")
    file.close()
# Function to handle returning rented land and generating bills
def return_land_and_bill():
    returned_land_records = [] # List to store returned land details
    land_info = read.table_details()# Read land details from file
    land_numbers = list(land_info.keys())# Get list of land numbers
     # Get client information
    name_of_client, address_of_client, number_of_client = operations.client_information()
    looping = True
    while looping:
        loop = True
        while loop:
            kitta_number = operations.kitta_number() # Get kitta number
            while kitta_number not in land_numbers:
                print("Invalid!")
                kitta_number = input("Kitta number: ")
            availability = land_info[kitta_number][4]
            if availability == "Available":
                print("This land is already available for rent.")
            else:
                loop = False
        # Input rented months and returned months
        rent_months = operations.input_rented_months()
        return_months = operations.input_returned_months()
         # Calculate fine and total
        if return_months > rent_months:
            print("A fine will be charged since you are returning the land late.")
            fine_months = return_months - rent_months
            fine = 0.10 * fine_months * int(land_info[kitta_number][3]) * rent_months
            total = (int(land_info[kitta_number][3]) * rent_months) + fine
        else:
            fine = 0
            total = int(land_info[kitta_number][3]) * rent_months
        return_land_and_bill = land_info[kitta_number]
        record = [kitta_number, return_land_and_bill[0], return_land_and_bill[1], return_land_and_bill[2], return_land_and_bill[3], rent_months, fine, total]
        returned_land_records.append(record)
        return_land_and_bill[4] = "Available"
        file = open("LandRentalSystem.txt","w")
        for key,value in land_info.items():
            file.write(key+","+value[0]+","+value[1]+","+value[2]+","+value[3]+","+value[4])
            file.write("\n")
        file.close()
        ans = operations.rent_continuation()
        if ans == "no":
            looping = False
    
    grand = sum(sublist[-1] for sublist in returned_land_records)

    # Printing Bills
    import datetime
    year = datetime.datetime.now().year
    month = datetime.datetime.now().month
    day = datetime.datetime.now().day
    hour = datetime.datetime.now().hour
    minute = datetime.datetime.now().minute
    second = datetime.datetime.now().second
    day_time = str(year) + "-" + str(month) + "-" + str(day) + " " + str(hour) + ":" + str(minute) + ":" + str(second)
    unique = str(year) + str(month) + str(day) + str(hour) + str(minute) + str(second)
    txtfilename = name_of_client + "@" + unique + ".txt"
    # Printing the bill
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("\n")
    print("                                                    Techno property Nepal !!!!!" + "\n")
    print("\n")                                                 
    print("\n")
    print("        Location       :  Kamal Pokhari" +  "                           Contact number :  01-4445671" + "\n")
    print("\n")
    print("\n")
    print("                                                ************** "+ "\n")
    print("                                                 Bill details "     +"\n")
    print("                                                ************** " +"\n")
    print("\n")
    print("Bill No. : " + unique + "\n")
    print("####################################################################################################################################################################")
    print("Name of Client: " + name_of_client + "\n")
    print("Address: " + address_of_client + "\n")
    print("Phone Number: " + str(number_of_client) + "\n")
    print("####################################################################################################################################################################")
    print("Kitta\t City       Direction   Anna   Price  Month\tFine\tTotal\n")
    print("#######################################################################################################################################################################")
    # To print the bill
    for row in returned_land_records:
        # Iterate over each element in the row
        for element in row:
            print(str(element), end='\t')
        # Move to the next line after printing each row
        print()
    print("#######################################################################################################################################################################")
    print("Grand Total: Rs.",grand,"\n")    


    # Creating a new .txt bill with unique bill number

    file = open(txtfilename, "w")
    file.write("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    file.write("\n")
    file.write("                                                    Techno property Nepal !!!!!" + "\n")
    file.write("\n")                                                 
    file.write("\n")
    file.write("        Location       :  Kamal Pokhari" +  "                           Contact number :  01-4445671" + "\n")
    file.write("\n")
    file.write("\n")
    file.write("                                                ************** "+ "\n")
    file.write("                                                 Bill details "     +"\n")
    file.write("                                                ************** " +"\n")
    file.write("\n")
    file.write("Bill No.: " + unique + "\n")
    file.write("################################################################################################################################################################\n")
    file.write("Name of Client: " + name_of_client + "\n")
    file.write("Address: " + address_of_client + "\n")
    file.write("Phone Number: " + str(number_of_client) + "\n")
    file.write("################################################################################################################################################################\n")
    file.write("Details: ")
    file.write("#################################################################################################################################################################\n")
    file.write("Kitta \t City \t\t Direction\t    Anna  \tPrice    Month\t\tFine\tTotal\n")
    file.write("##################################################################################################################################################################\n")

    for rows in returned_land_records:
        for items in rows:
            file.write(str(items) + "\t\t")
        file.write("\n")

    file.write("#################################################################################################################################################################\n")
    file.write("Grand Total: Rs." + str(grand) + "\n")
    file.close()
