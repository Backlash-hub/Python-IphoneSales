import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

Order_Details = pd.read_csv('Order_details(masked).csv')

Order_Details['Time'] = pd.to_datetime(Order_Details['Transaction Date'])
Order_Details['Hour'] = (Order_Details['Time']).dt.hour

timeslot1 = Order_Details['Hour'].value_counts().index.tolist()[:24]
timeslot2 = Order_Details['Hour'].value_counts().values.tolist()[:24]

tmost = np.column_stack((timeslot1, timeslot2))

#print( "Hour Of Day" + "\t" + "Cumulative Number of Purchase \n")
#print('\n'.join('\t\t'.join(map(str, row)) for row in tmost))

timemost = Order_Details['Hour'].value_counts()
timemost1 = []

for i in range(0,23):
    timemost1.append(i)

timemost2 = timemost.sort_index()
timemost2.tolist()
timemost2 = pd.DataFrame(timemost2)

plt.figure(figsize=(20, 10))

plt.title('Sales Happening Per Hour (Spread Throughout The Week)',
          fontdict={'fontname': 'monospace', 'fontsize': 30}, y=1.05)

plt.ylabel("Number of Purchases Made", fontsize=18, labelpad=20)
plt.xlabel("Hour", fontsize=18, labelpad=20)
plt.plot(timemost1, timemost2, color='m')
plt.grid()
plt.tight_layout()
plt.savefig("plot.png", dpi=200)
print("Saved plot.png")