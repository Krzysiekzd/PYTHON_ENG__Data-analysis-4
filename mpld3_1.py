import pandas as pd
import matplotlib.pyplot as plt
import mpld3
import sys

def main():
    sizes = {'label':20,'title':25,'text':15}

    df = pd.read_csv('data/sport_events.csv')
    countries = df['Country'].tolist()
    pos = list(range(len(countries)))

    fig, ax = plt.subplots(figsize=(7.292,5.208))
    ax.bar(pos,df['Percent_of_people_attending_at_least_once'],edgecolor='black',zorder=2)
    ax.set_ylim([0,100])
    ax.set_xticks(pos, labels=countries)
    ax.set_xlabel('Country',size=sizes['label'])
    ax.set_ylabel('Percent of people',size=sizes['label'])
    ax.set_title('People that attended sport events at least once in 2011',size=sizes['title'])

    _=[ax.text(index, 2, countries[index], size=sizes['text'],
                horizontalalignment='center',color='white') for index in range(len(countries))]
    return fig


if __name__=='__main__':
    figure = main()
    if (len(sys.argv)>=2):
        if int(sys.argv[1])==0:
            mpld3.show()
        elif int(sys.argv[1])==1:
            filename='mpld3_1.html'
            file = open(filename,'w+')
            file.write(mpld3.fig_to_html(figure))
            file.close()
            print(f'Saved to {filename}')
    else: sys.exit('No argument given.')