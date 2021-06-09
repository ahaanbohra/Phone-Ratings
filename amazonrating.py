import csv
import plotly.figure_factory as ff
import pandas as pd

df=pd.read_csv("amazonrating.csv")
fig=ff.create_distplot([df["Avg Rating"].tolist()],["ratings"])
fig.show()