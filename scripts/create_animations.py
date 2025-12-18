import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.animation import PillowWriter
from pathlib import Path
import warnings

warnings.filterwarnings('ignore')

CONFIG = {
    'input_file': Path(__file__).parent.parent / "data" / "raw" / "spotify_christmas_streams_kworb_2017_2025.csv", #csv data
    'output_dir': Path(__file__).parent.parent / "images" / "animations", #animations output
    'figsize': (16, 9),  #animation image size
    'dpi': 100,
    'colors': { #color for each song
        'All I Want for Christmas Is You': '#e74c3c', #Red
        'Last Christmas': '#3498db', #Blue
        "Rockin' Around the Christmas Tree": '#2ecc71',#Green
        'Jingle Bell Rock': '#f39c12', #Orange
        'Santa Tell Me': '#9b59b6', #Purple
        "It's Beginning to Look a Lot Like Christmas": '#1abc9c',#Teal
        'Feliz Navidad': '#e67e22' #Dark Orange
    }}
def load_data():
    df = pd.read_csv(CONFIG['input_file']) #reads the csv file with data for each song
    df['date'] = pd.to_datetime(df['date']) #adjusts the date column to datetime format to facilitate pandas analysis
    df['year'] = df['date'].dt.year  #new column with the year
    df['week'] = df['date'].dt.isocalendar().week # column with the week
    return df

def format_metric(num):
    if num >= 1e9: return f'{num/1e9:.2f}B' #transforms values to Billions to facilitate analysis
    if num >= 1e6: return f'{num/1e6:.1f}M' #transforms to millions
    return f'{num:,.0f}'

def animate_accumulated_race(df): #to create animation of accumulated views for each song
    df_pivot = df.pivot_table(index='date', columns='track', values='streams', fill_value=0).cumsum() #reorganizes data into table format
    #dates are in rows, columns are songs and values are streams for each song per date
    #cumsum calculates the number of viewers cumulatively
    dates = df_pivot.index #extracts dates to use in the animation
    fig, ax = plt.subplots(figsize=CONFIG['figsize'])  #creates figure and axis for the chart, size comes from dictionary defined above
    plt.subplots_adjust(left=0.30, right=0.95, top=0.90, bottom=0.10)  #subplot with margin adjustments, the 30% on the left is to place song names

    def update(frame): #function created to create each animation frame (several pictures together that will create the animation)
        ax.clear() #clears the previous chart to draw new frame (erases one and the next comes)
        current_date = dates[frame] #date of current frame
        data = df_pivot.loc[current_date].sort_values()#Data for specific date
        data = data[data > 0] # Filter zero (songs with 0 streams on some date)
        colors = [CONFIG['colors'].get(x, '#95a5a6') for x in data.index]  #colors (defined above) for each song
        ax.barh(data.index, data.values, color=colors, edgecolor='black', alpha=0.9) #Horizontal bar with colors for each song, with black border
        ax.set_yticks(range(len(data))) #Sets numeric positions for Y axis.
        ax.set_yticklabels(data.index, fontsize=12, fontweight='bold') ##y labels being the songs (in that 30% spacing defined above)

        for i, v in enumerate(data.values): #numeric value for each song and dates, will go through all dates to make the chart
            ax.text(v, i, f" {format_metric(v)}", va='center', fontweight='bold', fontsize=11) #formats values in millions and billions defined above 
        ax.set_title(f'TOTAL ACCUMULATED STREAMS (2017-2025)\n{current_date.strftime("%d %b %Y")}',  #title with the date
                     fontsize=18, fontweight='bold', pad=20)
        ax.grid(True, axis='x', linestyle='--', alpha=0.3)
        ax.text(0.95, 0.15, str(current_date.year), transform=ax.transAxes,  #to show the year as watermark in the lower corner, to facilitate year visualization
                fontsize=60, color='gray', alpha=0.15, ha='right', fontweight='bold')

    anim = animation.FuncAnimation(fig, update, frames=len(dates), interval=200) #Creates the animation object, the figure with the size where animation happens
    #update function to draw each frame one at a time, number of frames being the amount of dates -> Each date being a frame, and interval of 200ms between them
    out_path = CONFIG['output_dir'] / "race_accumulated_total.gif" #output name in gif format
    anim.save(out_path, writer=PillowWriter(fps=4), dpi=CONFIG['dpi']) #transforms the result into gif with 4 frames per second
    plt.close()
    print(f"   [Saved] {out_path.name}") #debug to know if it saved

def animate_weekly_growth(df): #Weekly growth animation
    df_seas = df[df['week'].between(45, 52)].copy() #filters weeks between 45 and 52 (end of year)
    grouped = df_seas.groupby(['year', 'week', 'track'])['streams'].sum().reset_index()#Groups data by year, week and song
    frames = sorted(list(set(zip(grouped['year'], grouped['week'])))) #Creates a list of unique tuples (year, week), sorted chronologically
    #[(2017, 45), (2017, 46), ..., (2024, 52)]
    fig, ax = plt.subplots(figsize=CONFIG['figsize']) #Setup Plot
    plt.subplots_adjust(bottom=0.25, top=0.90) #25% of space at the bottom to place song names (same logic used above) 
    def update(frame): #function to update frames
        ax.clear() #to clear the image between each frame
        year, week = frames[frame] #definition of year and week
        data = grouped[(grouped['year'] == year) & (grouped['week'] == week)].sort_values('streams', ascending=False)   # Filter data for specific week
        if data.empty: return
        colors = [CONFIG['colors'].get(x, '#95a5a6') for x in data['track']] #colors for each bar
        ax.bar(range(len(data)), data['streams'], color=colors, edgecolor='black', alpha=0.8)#uses Bar unlike Barh(horizontal), this command is for vertical
        ax.set_xticks(range(len(data))) #position on x axis being each song, position 0,1,2,3...
        ax.set_xticklabels([x[:35] for x in data['track']], rotation=30, ha='right', fontsize=11, fontweight='bold') #places song names on axis
        #also tilts 30° and aligns right to facilitate visualization
        for i, v in enumerate(data['streams']): #adds the streams value...
            ax.text(i, v, f"{format_metric(v)}", ha='center', va='bottom', fontsize=11, fontweight='bold') #at the top of each bar -> the value for each week
        ax.set_title(f'Christmas Season Weekly Growth\nYear: {year} | Week: {week}', fontsize=18, fontweight='bold', pad=20) #Title in two lines showing current year and week
        ax.grid(True, axis='y', alpha=0.3) 
        ax.text(0.98, 0.95, f'{year} - W{week}', transform=ax.transAxes, fontsize=14,  #shows the year and week of analysis in yellow color in upper right corner
                ha='right', bbox=dict(boxstyle='round', facecolor='yellow', alpha=0.7))
        
    anim = animation.FuncAnimation(fig, update, frames=len(frames), interval=800)#Creates the animation object, the figure with the size where animation happens
    #update function to draw each frame one at a time, number of frames being the amount of dates -> Each date being a frame, and interval of 800ms between them
    out_path = CONFIG['output_dir'] / "growth_weekly_season.gif" #name and path for output (defined above)
    anim.save(out_path, writer=PillowWriter(fps=1.5), dpi=CONFIG['dpi']) #gif with 1.5 frames per second (slower to see the changes)
    plt.close()
    print(f"   [Saved] {out_path.name}")

if __name__ == "__main__": #ensures it will only run when executed
    CONFIG['output_dir'].mkdir(parents=True, exist_ok=True) #creates output directory (defined above) if it doesn't exist
    df = load_data() #loads and processes CSV data
    print(df)
    animate_accumulated_race(df)  #function to create the accumulated number of viewers
    animate_weekly_growth(df)  #function to see the weekly values of each song
    print("\n>> Sucess")