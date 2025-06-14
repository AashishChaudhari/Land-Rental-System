#read.py
def table_details():
      # Create an empty dictionary to store land information
    land_info = {}
    # Open the file "LandRentalSystem.txt" in read mode
    fileName = open("LandRentalSystem.txt", "r")
    
    # Read all lines from the file
    lines = fileName.readlines()
     # Iterate through each line in the file
    for each in lines:
        # Remove the newline character and split the line by comma to separate fields
        each = each.replace("\n", "").split(",")
         # The first element of the split line is used as the key
        key = each[0]
        
        # Create an empty list to store values corresponding to the key
        value = []
         # Iterate through the elements starting from the second element
        for i in range(1, len(each)):
            # Remove trailing spaces or tabs from each element
            while each[i].endswith(' ') or each[i].endswith('\t'):
                each[i] = each[i][:-1]
        # Add the cleaned element to the values list
            value.append(each[i])
            # Assign the list of values to the key in the dictionary
        land_info[key] = value
    fileName.close()# Close the file
    # Return the dictionary containing land information
    return land_info





            
