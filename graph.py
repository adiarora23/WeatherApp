import pandas as pd   
import matplotlib.pyplot as plt 
import numpy as np
import random
class Graph:
    
    def __init__(self):
        self.labelx = ''
        self.labely = ''
    '''
    def precip_overview(self, precip_data): #title, xlab, ylab, time_length ):
        trial = pd.DataFrame.from_dict(precip_data) #just for now
        t = trial['time'].values
        #plt.plot()
        t = pd.Timedelta(days=2) #specify time to see in hours, days, weeks (if time delta works)
        print(trial, '\n\n\n\n', t)
        #print('\n\n\n', precip_data)
        '''
    def precip_overview(self, precip_data): #title, xlab, ylab, time_length ):
        df = pd.DataFrame.from_dict(precip_data) #just for now
        plt.plot(df['time'].values, df['rain amount'].values)
        
        plt.show() 
    
    def overview(self, general_data, time_choice): #graph for overview of temp (or precip) data over a period of time (choice of hourly avg or daily avg of the week)
        df = pd.DataFrame.from_dict(general_data)
        hour = 'nothing so far'
        df['time'] = pd.to_datetime(df['time'])
        if time_choice == 'hourly':
            hour = df['time'].dt.hour
        elif time_choice == 'daily':
            hour = df.groupby('day')
            
        print('hour')
    
    def sunshine(self):
        pass
    
    def wind(self):
        pass
    
#Sample Data to work w until
    
s = []
for i in range (0,20):
    a = random.uniform(0,2)
    a = round(a, 2)
    s.append(a)

r = []
for i in range (0,20):
    a = random.randint(0, 20)
    r.append(a)

t = ['00:00:00', '01:00:00', '02:00:00', '03:00:00','04:00:00', '05:00:00','06:00:00', '07:00:00','08:00:00', '09:00:00','10:00:00', '11:00:00','12:00:00', '13:00:00','14:00:00', '15:00:00','16:00:00', '17:00:00','18:00:00', '19:00:00']

data = {'time': t, 'rain amount': r, 'sun index': s}
a = Graph()
a.overview(data, 'hourly')
