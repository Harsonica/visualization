import pandas as pd 
import csv 
import plotly.graph_objects as go 
df = pd.read_csv("data.csv")

#prints mean of each level

print(df.groupby("level")["attempt"].mean())


fig=go.Figure(go.Bar(x=df.groupby("level")["attempt"].mean(),
    y=["Level 1","Level 2", "Level3", "Level4"], 
    orientation="h"))
fig.show()