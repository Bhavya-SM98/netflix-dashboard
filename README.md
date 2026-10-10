Netflix Movies and TV Shows Dashboard
An interactive dashboard that explores the Netflix catalog: how much content is Movies vs TV Shows, what was added each year, and which genres and countries lead. 

Live app: 

https://netflix-dashboard-hkxenggmgzlklxsudu6p94.streamlit.app/

Features

Sidebar filters for type (Movie / TV Show) and release year
Metric cards: total titles, movies, TV shows, countries
Charts: Movies vs TV Shows, titles added per year, top 10 genres, top 10 countries
Searchable table of titles

Dataset
Kaggle: Netflix Movies and TV Shows (`netflix_titles.csv`)

Tools Used
Python, pandas, Plotly, Streamlit, Jupyter Notebook (VS Code)
Data Cleaning
Converted `date_added` to a date and extracted year and month
Filled missing `country`, `director` and `cast` with "Unknown"
Dropped rows with a missing `rating`
Split multi-value columns (`listed_in` and `country`) into one row per value
Handled movie duration (minutes) and TV show duration (seasons) separately


Key Findings
ADD: what share of the catalog is Movies vs TV Shows
ADD: which year had the most titles added
ADD: the top genre and the top country
ADD: any other pattern you noticed

Project Structure
```
netflix-dashboard/
  data/            netflix_titles.csv
  notebooks/       analysis.ipynb
  app.py           Streamlit dashboard
  requirements.txt
  README.md
```
Run Locally
```
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
streamlit run app.py
```
