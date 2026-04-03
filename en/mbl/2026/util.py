import pandas as pd, numpy as np, sys, datetime, subprocess
import matplotlib.pyplot as plt, folium, json, re, codecs
import requests, urllib.request, os, fredapi

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

def get_pd(): return pd

def econ_stats():
    fig, axes = plt.subplots(3, 1)
    df1 = get_fred(2025,"GASREGW")
    df1.plot(ax=axes[0],legend=False,title="Gas $/Gallon - " + str(float(df1.GASREGW.tail(1))))
    df2 = get_fred(2025,"DCOILWTICO").interpolate()
    df2.plot(ax=axes[1],legend=False,title="Crude WTI $/Barrel - " + str(float(df2.DCOILWTICO.tail(1))))
    df3 = get_fred(2026,"SP500").interpolate()
    df3.plot(ax=axes[2],legend=False,title="S&P 500 - "  + str(float(df3.SP500.tail(1))) )
    plt.tight_layout()
    plt.savefig('/tmp/out.jpg')    

def llm1(prompt):
    command = ["ollama", "run", "qwen3.5:397b-cloud", prompt]    
    result = subprocess.run(command, capture_output=True, check=True)    
    raw_output = result.stdout.decode('utf-8')
    pattern = r"(?si)Thinking\.\.\..*?done thinking\.\n?"
    clean_text = re.sub(pattern, "", raw_output)
    print (clean_text.strip())

def llm2(prompt):
    command = ["ollama", "run", "gpt-oss:120b-cloud", prompt]    
    result = subprocess.run(command, capture_output=True, check=True)    
    raw_output = result.stdout.decode('utf-8')
    pattern = r"(?si)Thinking\.\.\..*?done thinking\.\n?"
    clean_text = re.sub(pattern, "", raw_output)
    clean_text = clean_text.replace("\[","$$")
    clean_text = clean_text.replace("\]","$$")
    clean_text = clean_text.replace("\(","$")
    clean_text = clean_text.replace("\)","$")
    
    print (clean_text.strip())

def plot_crises():
    plt.axvspan('1980-01-01', '1982-11-01', color='y', alpha=0.5, lw=0)
    plt.axvspan('1987-10-06', '1988-01-01', color='y', alpha=0.5, lw=0)
    plt.axvspan('1990-09-01', '1991-07-01', color='y', alpha=0.5, lw=0)
    plt.axvspan('2001-03-01', '2001-10-27', color='y', alpha=0.5, lw=0)
    plt.axvspan('2007-12-22', '2009-05-09', color='y', alpha=0.5, lw=0)
    plt.axvspan('2020-01-03', '2020-07-09', color='y', alpha=0.5, lw=0)    
    

def get_yahoo_ticker(year, ticker):
    d1 = datetime.datetime.strptime(str(year) + "-01-01", "%Y-%m-%d").timestamp()
    d2 = datetime.datetime.now().timestamp()    
    url = "https://query2.finance.yahoo.com/v8/finance/chart/%s?period1=%d&period2=%d&interval=1d&events=history&includeAdjustedClose=true" 
    url = url % (ticker,int(d1),int(d2))
    req = urllib.request.Request(
        url, 
        data=None, 
        headers={
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
        }
    )    
    r = urllib.request.urlopen(req).read()
    res = json.loads(r)
    ts = res['chart']['result'][0]['timestamp']
    adjclose = res['chart']['result'][0]['indicators']['adjclose'][0]['adjclose']
    ts = [datetime.datetime.fromtimestamp(x).strftime("%Y-%m-%d") for x in ts]
    df = pd.DataFrame(adjclose,index=pd.to_datetime(ts),columns=[ticker])
    return df

def data_synth_1():
   N = 200
   X = np.linspace(-2*np.pi,2*np.pi,N)
   y = np.sin(X) + np.random.standard_normal(size=N)*0.2
   df = pd.DataFrame(y,index=X)
   df.columns = ['ydata']
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

def get_fred(year,series):
    params = json.loads(open(os.environ['HOME'] + "/.twkeys.json").read())
    api_key = params["fred"]
    start_date = f"{year}-01-01"
    f = fredapi.Fred(api_key=api_key)
    data = f.get_series(series,observation_start=start_date)
    df = pd.DataFrame(data, columns=[series])    
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
        map_usnavy("usnavy-0302.csv","map03.html")
