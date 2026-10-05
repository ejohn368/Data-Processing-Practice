'''
/************************************************************/
/* Author: Enzo Johnson */
/* Major: Information Technology */
/* Due Date: September 21, 2026 */
/* Course: CPSC 223 020 */
/* Assignment: Project 1 */
/* Purpose: To open files, process data, and write the processed data to an output file. */
/* Function name: get_data() */
/* Description: This function opens the file, splits the values by whitespace, appends them as lists to "sales" list, and converts values to floats. */
/* Function name: process_data() */
/* Description: This function processes a list of lists. It returns a count for how many months each department performed above or below
/* the standard and whether or not they satisfied the performance requirements. It also returns an average and the number of the
/* corresponding department. All processed data is returned as a dictionary and appended to an empty list. */
/* Function name: write_to_file() */
/* Description: This function writes a header and the processed data into an output file. */
/* Function name: main() */
/* Description: runs all the functions in a main function */
/************************************************************/
'''
fileInput = input("Please input the file: ") # takes an input file 

standard = [23.0, 33.1, 21.0, 23.5, 54.0, 34.3, 35.0, 45.0, 56.3, 45.6, 34.0, 55.0] # sets the standard for each month's sales

def get_data(inp):
    """This function opens the file, splits the values by whitespace, appends them as lists to "sales" list, and converts values to floats."""
    sales = [] # init list that will hold value lists
    with open(fileInput, 'r') as f: # opens the file in read mode
        for line in f: # loops through each line in the file
            values = line.split() # splits the values by white space
            sales.append(values) # appends each list of values to empty list
            for i in range(len(sales)): # loops through each index in the full length of the sales list
                for val in range(len(sales[i])): # loops through each of the values within the index of the full length of sales list
                    sales[i][val] = float(sales[i][val]) # converts each of the values within each list (index) to float values
    return sales # returns the converted list of lists

def process_data(inp, std):
    """This function processes a list of lists. It returns a count for how many months each department performed above or below
    the standard and whether or not they satisfied the performance requirements. It also returns an average and the number of the
    corresponding department. All processed data is returned as a dictionary and appended to an empty list."""
    dictList = [] # init list to hold dictionaries
    for i in range(len(inp)): # loops through the list of lists inputted into function
        # init counters for months above/below standard and a total for avg calculation
        total = 0 
        aboveCount = 0
        belowCount = 0
        for val in range(len(inp[i])): # loops through each value in each index (list) of values in the list of lists
            total += inp[i][val] # adds each value in each list to the total 
            # conditional statement determines if each value in each list performed above or below the standard
            if inp[i][val] >= standard[val]: 
                aboveCount += 1
            else:
                belowCount += 1
        avg = round(total / 12, 1) # calculates the average of each department's monthly sales
        # conditional statement determines whether department satisfied performance or did not.
        if belowCount > 4:
            performance = "unsatisfied"
        else:
            performance = "satisfied"
        # init a template dictionary to hold processed data from each list in list of lists and append it to the previously
        # created empty list
        dptDict = {"Department": i + 1, "Average": avg, "Above": aboveCount, "Below": belowCount, "Performance": performance}
        dictList.append(dptDict)
    return dictList # returns the completed list of dictionaries

def write_to_file(dictL):
    """This function writes a header and the processed data into an output file."""
    with open("out.dat", 'w') as file: # creates/opens the file in write mode
        file.write("Department,Average,Above,Below,Performance\n") # writes the header at the top of the file
        for dict in dictL: # loops through each dictionary in the list of dictionaries and writes the values as strings into the output
            file.write(f"{dict["Department"]},{dict["Average"]},{dict["Above"]},{dict["Below"]},{dict["Performance"]} \n")
            
def main(): # runs all the functions in a main function
    write_to_file(process_data(get_data(fileInput), standard))

if __name__ == "__main__": # executes main function
    main()