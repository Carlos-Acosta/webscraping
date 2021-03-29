import gmaps
import pandas as pd



def heatmap(api, csv_file, product_list):
    gmaps.configure(api_key=api) 
    df = pd.read_csv('bonarea_gasolineras_prices.csv')
    normalized_price=(df[product_list]-df[product_list].min())/(df[product_list].max()-df[product_list].min())
    spain_coordinates = (41.8, -0.041509)
    fig = gmaps.figure(center=spain_coordinates, zoom_level=7)
    heatmap_layer = gmaps.heatmap_layer(df[['latitude', 'longitude']], weights=normalized_price,
    max_intensity=0, point_radius=20.0)
    fig.add_layer(heatmap_layer)
    return fig


#heatmap("AIzaSyDAQtZoSJcyMCoLMBIutENA3WrMLf3YF3w",'bonarea_gasolineras_prices.csv',"GASOIL A")