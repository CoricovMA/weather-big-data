import matplotlib.pyplot as plt
import mplleaflet
from Model import earthquake,tsunami,weather
import pandas as pd
from random import randint
from string import Template
class Threading(object):
    def __init__(self, interval=1):
        self.interval = interval
        thread = threading.Thread(target=self.plotPoints, args=("",))
        thread.daemon = True
        thread.start()
    def plotPoints(map_name,lat_long,cl):
        fig, ax = plt.subplots()
        x = [lat_long['lng']]
        y = [lat_long['lat']]
        ax.plot(x, y, cl)
        maps="templates/"+map_name+".html"
        f=open(maps,"w")
        f.write(mplleaflet.fig_to_html(fig=fig))
        f.close()
    def plotWeather(map_name,hail_la_ln,wind_la_ln,tornado_la_ln):
        fig, ax = plt.subplots()
        x = [hail_la_ln['lng']]
        y = [hail_la_ln['lat']]
        ax.plot(x, y, 'b*')
        x = [wind_la_ln['lng']]
        y = [wind_la_ln['lat']]
        ax.plot(x, y, 'b>')
        x = [tornado_la_ln['lng']]
        y = [tornado_la_ln['lat']]
        ax.plot(x, y, 'b^')
        maps="templates/"+map_name+".html"
        f=open(maps,"w")
        f.write(mplleaflet.fig_to_html(fig=fig))
        f.close()
# if __name__ == '__main__':
#     plotPoints("templates/default.html")