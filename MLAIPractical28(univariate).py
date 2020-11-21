from matplotlib import pyplot as plt

import pandas

filename = 'indians-diabetes.data.csv'
hnames = ['preg', 'plas', 'pres', 'skin', 'test','mass', 'pedi','age', 'class']

df = pandas.read_csv(filename, names = hnames)

print( type(df))
df.hist()
plt.show()