import pandas as pd, numpy as np, sys, datetime, requests
import matplotlib.pyplot as plt, folium, json
from pandas_datareader import data

def trump_approval():
    # https://www.realclearpolling.com/polls/approval/donald-trump/approval-rating
    # LV = Likely Voters, RV = Registered Voters
    df = pd.read_csv('djt_approval.csv',index_col='Date')
    df.index = pd.to_datetime(df.index,format='%d-%m-%Y')
    df = df.reindex(pd.date_range(start=df.index.min(),
                                  end=df.index.max(),
                                  freq='1D')).interpolate()    
    df['net'] = df.Approve - df.Disprove
    df['net'].plot(grid=True,title='POTUS Net Approval - ' + datetime.datetime.now().strftime("%m/%d"))    
    print (df['net'].tail(6))
    plt.savefig('/tmp/approval.jpg')
    return df

def map_usnavy(infile,outfile):
    df = pd.read_csv(infile,sep=',')
    m = folium.Map(location=[0,0], zoom_start=3) 
    for idx, (ship,lat,lon) in df.iterrows():
        folium.Marker([lat + np.random.uniform(-0.5,0.5),
                       lon + np.random.uniform(-0.5,0.5)],
                      popup=folium.Popup(ship)).add_to(m)
    m.save(outfile)    

def elev_at(lat,lon):
    data = '[[%f,%f]]' % (lat,lon)
    response = requests.post('https://elevation.racemap.com/api',
                             headers={'Content-Type': 'application/json',},
                             data=data)
    res = response.text
    return int(json.loads(res)[0])

def get_fred(year, series):
    today = datetime.datetime.now()
    start=datetime.datetime(year, 1, 1)
    end=datetime.datetime(today.year, today.month, today.day)
    df = data.DataReader(series, 'fred', start, end)
    return df

def flip_c(arg):
    return [[x[1],x[0]] for x in arg]

def map_coords(center, coords, lines={}, zoom=5, colors={}, outfile="/tmp/out.html"):
    m = folium.Map(location=center, zoom_start=zoom)
    folium.TileLayer(tiles="https://{s}.basemaps.cartocdn.com/rastertiles/voyager/{z}/{x}/{y}.png",
            name='subdomains2',
            attr='attribution',
            subdomains='mytilesubdomain'
    ).add_to(m)
    for key,val in coords.items():
        folium.Marker(val, popup=folium.Popup(key, show=True)).add_to(m)
    for key,val in lines.items():
        c = colors[key] if key in colors else "blue"
        folium.PolyLine(val, color=c, popup=folium.Popup(key, show=True)).add_to(m)
    m.save(outfile)
    
if __name__ == "__main__": 
    
    if sys.argv[1] == "approv":
        trump_approval()
    if sys.argv[1] == "usnavy":
        plot_us_navy("usnavy-1212.csv","map17.html")
