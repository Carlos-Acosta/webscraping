# Import functions/libraries
from main_functions import update_prices
from main_functions import update_data_and_prices
from main_functions import update_dataframe_global

# User engagement.
# Instructions to get dataset option from user
print("In order to optimize memory and storage, there are several options to get bonarea dataframe.")
print()
print()
print("  -> Option 1: One dataset with all Bonarea entities (super, botiga, benzinera, bufet, box, cash, diposit) identification and description data")
print("  -> Option 2: One dataset with only variable data related with petrol product prices")
print("  -> Option 3: One full dataset with all data for petrol station only (constant and variable data)")
print()
print()
print("Option 1 will get a static dataset of all Bonarea entities with constant data like address, city, associated services, etc.")
print("This option is useful if you wish description data about any of the Bonarea entities")
print()
print()
print("Option 2 will get a updated dataset of the petrol station prices by product every time the query is risen")
print()
print()
print("Option 3 will get the combination of option 1 and 2 for petrol station only (easier to handle, but it is not optimized for memory purposes)")

# User dataset option
type_of_dataset = str(input("Enter the selected option: "))

# Definition of option list according selected dataset (new or update)
type_options = ["1","2","3"]

# Function to orchestrate the obtaining of the selected dataset
 
def dataframe(type_of_dataset):
    """[summary]
        Get dataframe according user selection
    Args:
        integer: [integer to be used to select chosen dataset: 1, 2 or 3].

    Returns:
        [csv file]: [csv file with selected dataframe]
    """
    # Condition to ensure user selects proper type of dataset
    if type_of_dataset not in type_options:
        dataframe = print("Please, introduce correct type of dataset!")    
    
    else:
        if (type_of_dataset == "1"):
            # Dataframe 1: All Bonarea entities info
            dataframe = update_dataframe_global()
            
        elif (type_of_dataset == "2"):
            # Dataframe 2: Petrol Station variable data info
            dataframe = update_prices("benzinera")

        elif (type_of_dataset == "3"):
            # Dataframe 3: Petro Station constant and variable data info
            dataframe = update_data_and_prices("benzinera")
        
    return dataframe

# Initialization
dataframe(type_of_dataset)