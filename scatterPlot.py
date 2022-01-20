import pandas as p
import plotly.express as pe

Plot = p.read_csv("covid.csv")

graph = pe.scatter(Plot,x="date",y="cases",color="country")

graph.show()