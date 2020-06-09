# import package needed for the code
import pyfiglet
import pandas as pd
import matplotlib.pyplot as plt

# import function written in different python files
import func_read
import func_plot

def front_face():
    image = pyfiglet.Figlet(font="big")
    print(image.renderText('Avocado'))

front_face()

# open data CFG method
year, averagePrice, volume, region, date = func_read.extract_data()
func_plot.histplot(averagePrice, 5)

# print maximum volume
maxvol = int(max(volume))
print("Maximum volume {}" .format(maxvol))



# open data panda.dataframe
df = pd.read_csv('./data/avocado.csv')
df = df.sort_values(by=['date']) # sort data by date



import datetime as dt
df['real_date'] = pd.TimedeltaIndex(df['date'], unit='d') + dt.datetime(1900,1,1)

print(df)


plt.plot(df.real_date,df.volume)

# Add title and axis names
plt.title('Total volume of avocado sold over the last couple years')
plt.xlabel('years')
plt.ylabel('volume')
plt.savefig('./plots/plot5.png', bbox_inches='tight', dpi=300)
plt.show()

