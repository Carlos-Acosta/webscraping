# Import functions/libraries
from main_functions import get_id_by_entityType1
from plot_box import box_price_one_id
from plot_box import box_price_all_id
from plot_heatmap import heatmap
from plot_price_evolution_by_id import evolucion_precio_gasolinera


# Function parameters to obtain the reportsg
csv_file = 'bonarea_gasolineras_prices.csv'
product_list = ["GASOIL A", "GASOLINA S/P 95", "GASOLINA S/P 98", "ADBLUE"]
type_options = ["1","2","3","4"]

# Initialization id petrol station by default
petrol_station_id = "A"

# Print all the available reports
print("Following reports are currently available: ")
print()
print("Type of report = 1 -> Box Plot for one selected Id")
print("Type of report = 2 -> Box Plot for all Id")
print("Type of report = 3 -> Line Plot showing price evolution for one selected Id")
print("Type of report = 4 -> Geographical HeatMap with the prices by product of all petrol stations: ")
print()

# User report option
select_report = str(input("Enter type of report you want to create: 1, 2, 3 o 4"))

# Showing important info to user for his/her selection
if select_report == "4":
    pass
else:
    print()
    print()
    print("These are the available Petrol Station Id: ")
    print()
    print()
    print(get_id_by_entityType1()[0])
    # User petrol station option selection
    petrol_station_id = str(input("Enter the petrol station Id:")).upper()

print()
print()
print("Following petrol products are currently available: ")
print()
print("Product Types:")
print("  -> GASOIL A")
print("  -> GASOLINA S/P 95")
print("  -> GASOLINA S/P 98")
print("  -> ADBLUE")
print()

# User petrol product type option
petrol_product_type = str(input("Enter the petrol product(GASOIL A, GASOLINA S/P 95, GASOLINA S/P 98 o ADBLUE):")).upper()

# Function to orchestrate the obtaining of the selected reports

def report(type_report):
    """[summary]
        Get report according user selection
    Args:
        integer: [integer to be used to select chosen dataset: 1, 2, 3 or 4].

    Returns:
        [plot]: [plot with selected report]
    """
    # Condition to ensure user selects proper petrol station id
    if petrol_station_id not in get_id_by_entityType1()[0]:
        result = print("Please, introduce correct Petrol Station Id!")
    
    # Condition to ensure user selects proper petrol product
    elif petrol_product_type not in product_list:
        result = print("Please, introduce correct Petrol product!")

    # Condition to ensure user selects proper type of report
    elif select_report not in type_options:
        result = print("Please, introduce correct type of report!")    
    
    else:
        if (type_report == "1"):
            #Report 1: Box Plot for one selected Id
            result = box_price_one_id(csv_file,
                                      petrol_station_id,
                                      petrol_product_type)

        elif (type_report == "2"):
            # Report 2: Box Plot for all Id
            result = box_price_all_id(csv_file,
                                      petrol_product_type)

        elif (type_report == "3"):
            # Report 3: Line Plot showing price evolution for one selected Id
            result = evolucion_precio_gasolinera(csv_file ,
                                                 petrol_station_id,
                                                 petrol_product_type)

        elif (type_report == "4"):
            # Report 4: Geographical HeatMap with the prices by product of all petrol stations
            # Introduction of user's API 
            api = str(input("Enter your API for google maps: "))
            result = heatmap(api, csv_file, petrol_product_type)


    return result

# Initialization
report(select_report)