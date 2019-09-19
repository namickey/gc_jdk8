import pandas as pd
%matplotlib inline
import matplotlib.pyplot as plt
fig, (a1) = plt.subplots(ncols=1, figsize=(25,8), sharey=True)
fig.suptitle(u'平均レスポンス 1秒間隔')
def graph(a, path, title):
    df = pd.read_csv(path)
    df['a'] = (df['a']/1000).round().astype(int)
    gf = df[['a','b']]
    gfed = gf.groupby('a').mean()
    a.set_title(title)
    a.set_ylim([0, 10000])
    a.set_yticks(range(0,10000,1000))
    a.grid(True)
    a.plot(gfed.index, gfed['b'])
a1.set_ylabel(u'レスポンス ミリ秒')
graph(a1, 'log.csv', u'mean ave')
fig.savefig('mean.png')
