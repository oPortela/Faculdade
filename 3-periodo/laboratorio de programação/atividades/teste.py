import ipeadatapy as ip
import matplotlib.pyplot as plt
from scipy.signal import savgol_filter

x = ip.list_series()
x = ip.timeseries('INPC', yearGreaterThan = 2022)
serie = x["VALUE (-)"]
serie_hat = savgol_filter(serie, 51, 3) 
#print(x["VALUE (-)"][0])
plt.plot(serie_hat)#[20:-20]
plt.show()
'''for i in range(9640):
    print(x['CODE'][i])'''
    
#print(x.keys)