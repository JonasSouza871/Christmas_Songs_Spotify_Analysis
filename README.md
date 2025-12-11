'''''''''''''''''111111 ''''''''# Christmas Songs Spotify Streaming Analysis (2017-2025)

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-11557c?style=for-the-badge&logo=python&logoColor=white)
![Seaborn](https://img.shields.io/badge/Seaborn-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Jupyter](https://img.shields.io/badge/Jupyter-F37626?style=for-the-badge&logo=jupyter&logoColor=white)
![BeautifulSoup](https://img.shields.io/badge/BeautifulSoup-59666C?style=for-the-badge&logo=python&logoColor=white)

## Overview

This project presents a comprehensive analysis of streaming patterns for 7 classic Christmas songs on Spotify between 2017 and 2025. Using data science and visualization techniques, we investigate temporal trends, seasonality, and the evolution of these songs' popularity during the holiday season.

## Analyzed Songs

1. All I Want for Christmas Is You - Mariah Carey
2. Last Christmas - Wham!
3. Rockin' Around the Christmas Tree - Brenda Lee
4. Jingle Bell Rock - Bobby Helms
5. Santa Tell Me - Ariana Grande
6. It's Beginning to Look a Lot Like Christmas - Michael Bublé
7. Feliz Navidad - José Feliciano

## Repository Structure

```
Christmas_Songs_Spotify_Analysis/
├── data/
│   └── raw/
│       └── spotify_christmas_streams_kworb_2017_2025.csv
├── notebooks/
│   ├── 01_data_collection.ipynb
│   ├── 02_exploratory_data_analysis.ipynb
│   ├── 03_temporal_analysis.ipynb
│   └── 04_prediction_models.ipynb
├── images/
│   ├── data_collection/
│   ├── exploratory_analysis/
│   ├── temporal_analysis/
│   └── prediction_models/
├── extract_images.py
├── README.md
├── LICENSE
└── .gitignore
```

## Analyses Performed

### 1. Data Collection
**Notebook:** `01_data_collection.ipynb`

- Web scraping from Kworb.net
- Historical streaming data extraction (2017-2025)
- Data processing and structuring
- Weekly granularity (Thursday updates)

![Collection Flowchart](images/data_collection/Data_Collection_Flowchart.png)

### 2. Exploratory Data Analysis
**Notebook:** `02_exploratory_data_analysis.ipynb`

Descriptive statistics per song:
- Mean, median, and standard deviation of weekly streams
- Coefficient of variation (CV%)
- Peak and outlier identification
- Frequency distribution

**Key Findings:**
- "All I Want for Christmas Is You" leads with 1.77 billion total streams
- All songs reached their peaks in Week 52 of 2024 (December 26)
- Average coefficient of variation of 64%, indicating high seasonality

![Average Weekly Streams](images/exploratory_analysis/average_weekly_streams_(in_top_200)_by_song_2017_-_nov_2025.png)

![Total Streams Distribution](images/exploratory_analysis/total_streams_distribution_by_song_(2017-2025).png)

### 3. Temporal Analysis
**Notebook:** `03_temporal_analysis.ipynb`

Time series analyses:
- Complete time series evolution (2017-2025)
- Seasonal patterns of the Christmas cycle (weeks 45-52 + week 1)
- Annual trend analysis with CAGR
- Year-over-year (YoY) growth
- Temporal heatmap (year × week)

**Key Findings:**
- CAGR of 23.34% (2017-2024)
- Exponential growth during weeks 48-52
- Sharp decline after week 1 (January)
- 2024 showed the highest historical peaks

![Individual Time Series](images/temporal_analysis/individual_time_series_weekly_streams_evolution_(2017-2025)_(only_shows_weeks_when_song_was_in_top_200_global).png)

![Temporal Heatmap](images/temporal_analysis/heatmap_total_streams_by_year_and_week_(all_7_christmas_songs_combined)_(weeks_45-52_+_week_1,_only_when_songs_were_in_top_200_global).png)

### 4. Predictive Models
**Notebook:** `04_prediction_models.ipynb`

Model selection and rationale:
- Data suitability analysis for seasonal patterns
- Dataset size considerations

**Selected Model:**
- **ARIMA**: Time series forecasting model for seasonal streaming patterns

## How to Run

### Prerequisites

```bash
pip install pandas numpy matplotlib seaborn jupyter beautifulsoup4 requests lxml tabulate
```

### Running the Notebooks

1. Clone the repository:
```bash
git clone https://github.com/your-username/Christmas_Songs_Spotify_Analysis.git
cd Christmas_Songs_Spotify_Analysis
```

2. Start Jupyter Notebook:
```bash
jupyter notebook
```

3. Run the notebooks in order:
   - `01_data_collection.ipynb` - Data collection
   - `02_exploratory_data_analysis.ipynb` - Exploratory analysis
   - `03_temporal_analysis.ipynb` - Temporal analysis
   - `04_prediction_models.ipynb` - Predictive models

## Key Results

### Popularity Ranking (Total Streams 2017-2025)

1. All I Want for Christmas Is You - 1.77 billion
2. Last Christmas - 1.50 billion
3. Rockin' Around the Christmas Tree - 1.16 billion
4. Jingle Bell Rock - 1.03 billion
5. Santa Tell Me - 1.01 billion
6. It's Beginning to Look a Lot Like Christmas - 927 million
7. Feliz Navidad - 633 million

### Seasonal Pattern

- **Start (Weeks 45-47)**: Gradual growth (8-11M streams/week)
- **Acceleration (Weeks 48-50)**: Exponential growth (15-24M streams/week)
- **Peak (Weeks 51-52)**: Maximum peak (27-39M streams/week)
- **Decline (Week 1)**: Sharp drop to 8-9M streams/week

### Annual Growth

- Compound Annual Growth Rate (CAGR): **23.34%**
- Consistent growth from 2017 to 2024
- 2024 established new historical records for all songs

## Dataset Limitations

- Data available only when songs are in Spotify's Global Top 200
- Gaps between February and October (off-season period)
- Weekly granularity (not daily)
- 2025 with partial data (until November 28)

## Technologies Used

- **Python 3.x**: Main language
- **Pandas**: Data manipulation and analysis
- **NumPy**: Numerical computing
- **Matplotlib**: Data visualization
- **Seaborn**: Statistical visualizations
- **Jupyter Notebook**: Development environment
- **BeautifulSoup**: Web scraping
- **Requests**: HTTP requests

## Data Source

**Kworb.net** - Spotify streaming tracking platform
- URL: https://kworb.net/spotify/
- Method: Web scraping
- Period: 01/01/2017 - 11/28/2025

## Author

**Jonas Souza**

Engenheiro Eletricista

## License

This project is under the MIT license. See the LICENSE file for more details.

---

**Note**: This is an educational analysis project and demonstration of data science skills. Data is collected from public sources for study purposes.
