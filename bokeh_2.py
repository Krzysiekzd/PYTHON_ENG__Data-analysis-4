from bokeh.plotting import figure, output_file, show, save
import pandas as pd
import sys

def main():
    df = pd.read_csv('data/Luxemburg_deaths.csv')
    p = figure(title="Female deaths in Luxemburg 2011-2020", x_axis_label='Year', y_axis_label='Deaths',
        max_width=700, height=500,y_range=(1800, 2400),x_range=(2010.5,2020.5))

    p.line(df['Year'], df['Deaths_females'], line_width=2,color='red')
    p.xaxis.axis_label_text_font_size = '15pt'
    p.yaxis.axis_label_text_font_size = '15pt'
    p.title.text_font_size = '20pt'
    return p


if __name__=='__main__':
    plot = main()
    if (len(sys.argv)>=2):
        if int(sys.argv[1])==0:
            show(plot)
        elif int(sys.argv[1])==1:
            filename="bokeh_2.html"
            output_file(filename=filename)
            save(plot)
            print(f'Saved to {filename}')
    else: sys.exit('No argument given.')