import gmaps
import pandas as pd

gmaps.configure(api_key='AIzaSyDAQtZoSJcyMCoLMBIutENA3WrMLf3YF3w') # Fill in with your API key

df = pd.read_csv("bonarea_gasolineras.csv")
normalized_price=(df['GASOIL A']-df['GASOIL A'].min())/(df['GASOIL A'].max()-df['GASOIL A'].min())

spain_coordinates = (41.8, -0.041509)
fig = gmaps.figure(center=spain_coordinates, zoom_level=7)
heatmap_layer = gmaps.heatmap_layer(df[['latitude', 'longitude']], weights=normalized_price,
    max_intensity=0, point_radius=20.0)


fig.add_layer(heatmap_layer)
fig