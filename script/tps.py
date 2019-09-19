import pandas as pd
%matplotlib inline
import matplotlib.pyplot as plt
fig, (a1) = plt.subplots(ncols=1, figsize=(25,8), sharey=True)
fig.suptitle(u'TPS（100秒間隔、クライアント1台）')
def graph(a, path, title):
    df = pd.read_csv(path)
    df['a'] = (df['a']/100000).round().astype(int)
    gf = df[['a','b']]
    gfed = gf.groupby('a').count()
    a.set_ylim([0, 90])
    a.set_yticks(range(0,90,10))
    a.set_title(title)
    a.grid(True)
    a.plot(gfed.index, gfed['b']/100)
a1.set_ylabel(u'TPS')
graph(a1, 'log.csv', u'TPS')
fig.savefig('tps.png')
