import pandas as pd
import plotly.graph_objects as go
import sys

def main():
    df = pd.read_csv('data/NED_cities.csv')
    df['Apartments_per_person']=df['Number_of_apartments']/df['Population']

    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=df['Size_km'], y=df['Apartments_per_person'],
        mode='markers',
        text=df['City'],
    ))
    fig.update_traces(mode='markers',marker_size=12)
    font = {"size": 20,'color':'black'}
    fig.update_xaxes(
            title_text = "Size of the city in sq. km",title_font = font,)
    fig.update_yaxes(
            title_text = "Apartments per person",title_font = font,)

    fig.update_layout(
        title="Number of apartments per person in Dutch cities (2020)",
        title_font = font,
        width=700,
        height=500
    )
    return fig

if __name__=='__main__':
    figure = main()
    if (len(sys.argv)>=2):
        if int(sys.argv[1])==0:
            figure.show()
        elif int(sys.argv[1])==1:
            filename='plotly_1.html'
            figure.write_html(filename)
            print(f'Saved to {filename}')
    else: sys.exit('No argument given.')


