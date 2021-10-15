import pandas as pd 
import csv 
import plotly.graph_objects as go 
df = pd.read_csv("data.csv")
student_df = df.loc[df["student_id"]=="TRL_987"]

#prints mean of each level

print(student_df.groupby("level")["attempt"].mean())


fig=go.Figure(go.Bar(x=student_df.groupby("level")["attempt"].mean(),
    y=["Level 1","Level 2", "Level3", "Level4"], 
    orientation="h"))
fig.show()