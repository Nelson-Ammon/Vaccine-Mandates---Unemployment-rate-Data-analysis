#%%
# import all packages 
import pandas as pd
import altair as alt
from altair_saver import save
import numpy as np
#%% # read in the data 
m1= pd.read_csv("M1SL.csv")
m1=
# %%
m1_chart = alt.Chart(m1).mark_line()
m1_chart
# %%
