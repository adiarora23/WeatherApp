import pandas as pd   
import matplotlib.pyplot as plt 
import numpy as np
import time
from datetime import datetime

class Graph: 
    
    def __init__(self):
        self.labelx = ''
        self.labely = ''
    
    def chart_prediction(self):
        pass    
        
    def chart_temp_overview(self, df):
        plt.figure(figsize = (6,4))
        x = df['date'].values
        y1 = df['daily_avg'].values
        y2 = df['daily_fl'].values
        y3 = df['daily_max'].values
        y4 = df['daily_min'].values
        
        plt.plot(x, y1, color = 'yellow', label = 'Daily Averages', lw= 5, 
                 marker = '*', markersize = 10, markerfacecolor = 'blue', markeredgecolor = 'blue')
        plt.plot(x, y2, color = 'blue', label = 'Daily feels like', ls = '--')
        plt.plot(x, y3, color = 'green', label = 'Daily max')
        plt.plot(x, y4, color = 'red', label = 'Daily min')
        
        plt.tick_params(axis = 'x', rotation = 45) #for visiual neatness
        plt.grid()
        plt.spring() #might not even need it... delete it later
        
        plt.title('Temperature Overview For the Next 7 Days')
        plt.legend()
        
        plt.show

    def temp_overview(self, all_data): 
        temp_stats = ['day','min','max','night','eve','morn']#for the temp keys in dataset
        time_of_day = ['day','night','eve','morn'] #for feels like keys in dataset
        
        date = []
        temps_avg = ['daily_avg', 'daily_min','daily_max','night_avg','eve_avg','morn_avg'] #key names for overview_dict
        temps_fl = ['daily_fl','night_fl','eve_fl','morn_fl'] #key names for overview_dict
        
        overview_dict = {}
        
        for x in range(0,8): #for loop for the days
            date.append(time.ctime(all_data['daily'][x]['dt'])[:10])
        
        overview_dict['date'] = date
            
        for key_name in temps_avg:
            overview_dict[key_name] = []
            
        for x in range(0,8):#for loop for the temp_avg's
            for data_key,key_name in zip(temp_stats,temps_avg): #code help from https://www.oreilly.com/library/view/python-cookbook/0596001673/ch01s15.html
                value = (all_data['daily'][x]['temp'][data_key] - 273.15)
                overview_dict[key_name].append(round(value))
                
        for key_name in temps_fl:
            overview_dict[key_name] = []
            
        for x in range(0,8):#for loop for the temp_avg's
            for data_key,key_name in zip(time_of_day,temps_fl): #code help from https://www.oreilly.com/library/view/python-cookbook/0596001673/ch01s15.html
                value = (all_data['daily'][x]['temp'][data_key] - 273.15)
                overview_dict[key_name].append(round(value))
            
            
        df = pd.DataFrame.from_dict(overview_dict) 
        self.chart_temp_overview(df)
    
    def sunshine(self):
        pass
    
    def wind(self):
        pass

'''
{
"lat":43.5953,
"lon":-79.6406,
"timezone":"America/Toronto",
"timezone_offset":-14400,

"current":{
"dt":1617049449,
"sunrise":1617015898,
"sunset":1617061273,
"temp":279.57,
"feels_like":275.78,
"pressure":1022,
"humidity":52,
"dew_point":270.75,
"uvi":2.54,
"clouds":40,
"visibility":10000,
"wind_speed":2.06,
"wind_deg":0,
"weather":[{"id":802,"main":"Clouds","description":"scattered clouds","icon":"03d"}]
},



"daily":[

{"dt":1617037200,
"sunrise":1617015898,
"sunset":1617061273,
"temp":{"day":277.01,"min":272.38,"max":279.58,"night":275.84,"eve":279.08,"morn":272.38},
"feels_like":{"day":271.05,"night":270.8,"eve":274.46,"morn":265.88},
"pressure":1023,
"humidity":42,
"dew_point":265.22,
"wind_speed":4.4,
"wind_deg":287,
"weather":[{"id":801,"main":"Clouds","description":"few clouds","icon":"02d"}],
"clouds":16,
"pop":0.3,
"uvi":4.37},


{"dt":1617123600,
"sunrise":1617102190,
"sunset":1617147744,
"temp":{"day":285.33,"min":275.67,"max":287.81,"night":284.66,"eve":286.98,"morn":277.02},
"feels_like":{"day":278.13,"night":279.77,"eve":280.85,"morn":271.53},
"pressure":1015,
"humidity":48,
"dew_point":274.46,
"wind_speed":7.78,
"wind_deg":202,
"weather":[{"id":804,"main":"Clouds","description":"overcast clouds","icon":"04d"}],
"clouds":90,
"pop":0,
"uvi":4.46},

{"dt":1617210000,
"sunrise":1617188482,
"sunset":1617234215,
"temp":{"day":278.82,"min":275.65,"max":284.41,"night":275.65,"eve":278.79,"morn":279.7},
"feels_like":{"day":273.9,"night":270.25,"eve":273.49,"morn":275.02},
"pressure":1016,
"humidity":63,
"dew_point":272.41,
"wind_speed":4.02,
"wind_deg":296,
"weather":[{"id":616,"main":"Snow","description":"rain and snow","icon":"13d"}],
"clouds":100,
"pop":0.99,
"rain":3.22,
"snow":0.18,
"uvi":3.59},

{"dt":1617296400,
"sunrise":1617274774,
"sunset":1617320686,
"temp":{"day":273.56,"min":271.14,"max":275.03,"night":271.5,"eve":272.95,"morn":271.14},
"feels_like":{"day":264.41,"night":263,"eve":263.96,"morn":263.51},
"pressure":1020,
"humidity":38,
"dew_point":260.83,
"wind_speed":8.48,
"wind_deg":336,
"weather":[{"id":804,"main":"Clouds","description":"overcast clouds","icon":"04d"}],
"clouds":99,
"pop":0.36,
"uvi":3.26},

{"dt":1617382800,
"sunrise":1617361066,
"sunset":1617407157,
"temp":{"day":277.31,"min":269.8,"max":278.89,"night":273.65,"eve":275.62,"morn":269.8},
"feels_like":{"day":269.81,"night":268.32,"eve":269.95,"morn":261.96},
"pressure":1027,
"humidity":21,
"dew_point":256.64,
"wind_speed":5.82,
"wind_deg":337,
"weather":[{"id":800,"main":"Clear","description":"clear sky","icon":"01d"}],
"clouds":0,
"pop":0,
"uvi":0.22},

{"dt":1617469200,
"sunrise":1617447359,
"sunset":1617493628,
"temp":{"day":281.43,"min":273.41,"max":283.33,"night":280.82,"eve":282.15,"morn":275.01},
"feels_like":{"day":275.8,"night":276.51,"eve":278.14,"morn":269.06},
"pressure":1022,
"humidity":59,
"dew_point":273.93,
"wind_speed":5.37,
"wind_deg":240,
"weather":[{"id":804,"main":"Clouds","description":"overcast clouds","icon":"04d"}],
"clouds":86,
"pop":0,
"uvi":1},

{"dt":1617555600,
"sunrise":1617533653,
"sunset":1617580099,
"temp":{"day":283.95,"min":280.13,"max":285.78,"night":281.92,"eve":283.69,"morn":280.56},
"feels_like":{"day":279.96,"night":279.1,"eve":280.13,"morn":276.97},
"pressure":1022,
"humidity":73,
"dew_point":279.3,
"wind_speed":4.44,
"wind_deg":229,
"weather":[{"id":804,"main":"Clouds","description":"overcast clouds","icon":"04d"}],
"clouds":100,
"pop":0,
"uvi":1},

{"dt":1617642000,
"sunrise":1617619946,
"sunset":1617666570,
"temp":{"day":288.49,"min":280.79,"max":288.49,"night":286.66,"eve":286.71,"morn":281.14},
"feels_like":{"day":283.06,"night":282.34,"eve":282.81,"morn":277.64},
"pressure":1018,
"humidity":61,
"dew_point":280.78,
"wind_speed":7.05,
"wind_deg":213,
"weather":[{"id":500,"main":"Rain","description":"light rain","icon":"10d"}],
"clouds":50,
"pop":0.77,
"rain":1.11,
"uvi":1}

]
}
'''









''' #Current weather for thurs april 1, 2021
{
"lat":43.5789,
"lon":-79.6583,
"timezone":"America/Toronto",
"timezone_offset":-14400,

"current":{
"dt":1617291890,
"sunrise":1617274779,
"sunset":1617320690,
"temp":273.43,
"feels_like":266.56,
"pressure":1020,
"humidity":59,
"dew_point":267.13,
"uvi":2.44,
"clouds":75,
"visibility":10000,
"wind_speed":9.77,
"wind_deg":330,
"weather":[{"id":803,"main":"Clouds","description":"broken clouds","icon":"04d"}]
},

"daily":[
{
"dt":1617296400,
"sunrise":1617274779,
"sunset":1617320690,
"temp":{"day":272.79,"min":271.55,"max":275.06,"night":271.55,"eve":272.61,"morn":271.63},
"feels_like":{"day":266.4,"night":265.77,"eve":266.31,"morn":265.77},
"pressure":1022,
"humidity":48,
"dew_point":264.18,
"wind_speed":7.9,
"wind_deg":341,
"weather":[{"id":803,"main":"Clouds","description":"broken clouds","icon":"04d"}],
"clouds":80,
"pop":0.02,
"uvi":2.78
},

{
"dt":1617382800,
"sunrise":1617361071,
"sunset":1617407160,
"temp":{"day":274.88,"min":269.82,"max":276.19,"night":272.19,"eve":274.79,"morn":269.82},
"feels_like":{"day":269.73,"night":263.54,"eve":270.15,"morn":263.54},
"pressure":1028,
"humidity":24,
"dew_point":256.3,
"wind_speed":6.37,
"wind_deg":340,
"weather":[{"id":800,"main":"Clear","description":"clear sky","icon":"01d"}],
"clouds":0,
"pop":0,
"uvi":3.96
},

{
"dt":1617469200,
"sunrise":1617447364,
"sunset":1617493631,
"temp":{"day":278.55,"min":271.98,"max":280.55,"night":276.32,"eve":275.55,"morn":272.25},
"feels_like":{"day":274.95,"night":269.28,"eve":271.05,"morn":269.28},
"pressure":1025,
"humidity":46,
"dew_point":267.74,
"wind_speed":5.07,
"wind_deg":212,
"weather":[{"id":500,"main":"Rain","description":"light rain","icon":"10d"}],
"clouds":70,
"pop":0.98,
"rain":1.51,
"uvi":2.14
},

{
"dt":1617555600,
"sunrise":1617533658,
"sunset":1617580102,
"temp":{"day":282.24,"min":276.04,"max":283.84,"night":278.26,"eve":280.79,"morn":276.04},
"feels_like":{"day":281.4,"night":273.92,"eve":279.03,"morn":273.92},
"pressure":1023,
"humidity":59,
"dew_point":274.72,
"wind_speed":1.87,
"wind_deg":357,
"weather":[{"id":802,"main":"Clouds","description":"scattered clouds","icon":"03d"}],
"clouds":43,
"pop":0.36,
"uvi":3.98
},

{
"dt":1617642000,
"sunrise":1617619951,
"sunset":1617666573,
"temp":{"day":282.23,"min":275.64,"max":282.63,"night":278.71,"eve":281.18,"morn":275.64},
"feels_like":{"day":282.23,"night":272.76,"eve":281.18,"morn":272.76},
"pressure":1024,
"humidity":40,
"dew_point":268.8,
"wind_speed":1.13,
"wind_deg":41,
"weather":[{"id":802,"main":"Clouds","description":"scattered clouds","icon":"03d"}],
"clouds":33,
"pop":0,
"uvi":0.26
},

{
"dt":1617728400,
"sunrise":1617706246,
"sunset":1617753044,
"temp":{"day":282.04,"min":276.12,"max":282.76,"night":279.4,"eve":280.26,"morn":276.36},
"feels_like":{"day":280.44,"night":274.68,"eve":279.54,"morn":274.68},
"pressure":1017,
"humidity":33,
"dew_point":265.73,
"wind_speed":2.82,
"wind_deg":113,
"weather":[{"id":802,"main":"Clouds","description":"scattered clouds","icon":"03d"}],
"clouds":31,
"pop":0,
"uvi":1
},

{
"dt":1617814800,
"sunrise":1617792540,
"sunset":1617839515,
"temp":{"day":284.43,"min":277.49,"max":285.01,"night":280.46,"eve":281.7,"morn":277.71},
"feels_like":{"day":282.34,"night":276.38,"eve":280.51,"morn":276.38},
"pressure":1014,
"humidity":28,
"dew_point":265.36,
"wind_speed":2.82,
"wind_deg":110,
"weather":[{"id":800,"main":"Clear","description":"clear sky","icon":"01d"}],
"clouds":1,
"pop":0,
"uvi":1
},

{
"dt":1617901200,
"sunrise":1617878836,
"sunset":1617925986,
"temp":{"day":279.29,"min":278.32,"max":280.36,"night":280.36,"eve":280.03,"morn":278.91},
"feels_like":{"day":276.21,"night":275.64,"eve":278.46,"morn":275.64},
"pressure":1005,
"humidity":87,
"dew_point":277.37,
"wind_speed":4.38,
"wind_deg":85,
"weather":[{"id":500,"main":"Rain","description":"light rain","icon":"10d"}],
"clouds":100,
"pop":1,
"rain":5.07,
"uvi":1
}
]

}
'''