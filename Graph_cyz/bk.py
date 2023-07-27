from bokeh.plotting import output_notebook, figure, output_notebook, show
from bokeh.models import ColumnDataSource
import pandas as pd
import csv

df = pd.read_csv("graph.csv")
x = df.iloc[0:, 0]
y = df.iloc[0:, 1]
z = df.iloc[0:, 2]

data = ColumnDataSource({'x':x,
                         'y':y,
                         'color':['red']
                       })

renk = 'g'

p = figure(title='VFS and EXT4 layer READ/WRITE graph',
           x_axis_label = 'time(milliseconds)',
           y_axis_label = 'Amount of Data(bytes)',
          )

p.circle(x='x', y='y', color='color', source=data, legend_label='data')

show(p)
