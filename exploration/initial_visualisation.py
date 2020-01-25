#%%
import pandas as pd
import numpy as np
import seaborn as sns
import pillow

#%%
import folium

m = folium.Map(
    location=[14.0583, 108.2772],
    zoom_start=5,
    tiles='Stamen Terrain'
    )
m