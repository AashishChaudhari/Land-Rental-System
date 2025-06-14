#main.py
#initialize validation flag 
validation = True
# Main loop for the program
while validation == True:
# Import necessary modules
    import write
    write.welcome_message()# Display welcome message
    import operations
    import read
    write.show_options()# Show options to the user
    option = operations.select_option()
     # Perform actions based on the selected option    
    if option == 1:
        operations.display_table() # Display table of available land
        
    elif option == 2:
        operations.display_table()# Display table of available land
        write.rent_land_and_bill()   # Rent land and generate bill      
        print("\n\n\n\n\n\nThank you for visiting!!")  # Display thank you message       
        
    elif option == 3:
        operations.display_table() # Display table of available land
        write.return_land_and_bill()    # Return rented land and generate bill      
        print("\n\n\n\n\n\nThank you for visiting!!") # Display thank you message
        
       
    elif option == 4: # Exit the program
        print("\n\n\n\n\n\nThank you for visiting!!")
        validation = False # Set validation flag to False to exit the loop
    else: # Handle incorrect option selection
        print("\n Please choose correct option from(1-4)!\n")
