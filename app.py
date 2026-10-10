import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(page_title="Netflix Dashboard", layout="wide")
st.title("Netflix Movies and TV Shows Dashboard")


@st.cache_data
def load_data():
    df = pd.read_csv("data/netflix_titles.csv", encoding="latin-1")
    df["date_added"] = pd.to_datetime(df["date_added"].str.strip(), errors="coerce")
    df["year_added"] = df["date_added"].dt.year
    df["country"] = df["country"].fillna("Unknown")
    df = df.dropna(subset=["rating"])
    return df


df = load_data()

# sidebar filters
st.sidebar.header("Filters")
types = st.sidebar.multiselect("Type", df["type"].unique(), default=list(df["type"].unique()))
year_min = int(df["release_year"].min())
year_max = int(df["release_year"].max())
years = st.sidebar.slider("Release year", year_min, year_max, (2000, year_max))

filtered = df[(df["type"].isin(types)) & (df["release_year"].between(years[0], years[1]))]

genres = filtered.assign(genre=filtered["listed_in"].str.split(", ")).explode("genre")
countries = filtered.assign(country=filtered["country"].str.split(", ")).explode("country")
countries = countries[countries["country"] != "Unknown"]

# metric cards
c1, c2, c3, c4 = st.columns(4)
c1.metric("Total titles", len(filtered))
c2.metric("Movies", int((filtered["type"] == "Movie").sum()))
c3.metric("TV Shows", int((filtered["type"] == "TV Show").sum()))
c4.metric("Countries", countries["country"].nunique())

# charts
left, right = st.columns(2)

with left:
    tc = filtered["type"].value_counts().reset_index()
    tc.columns = ["type", "count"]
    st.plotly_chart(px.pie(tc, names="type", values="count", hole=0.5, title="Movies vs TV Shows"), use_container_width=True)

    tg = genres["genre"].value_counts().head(10).reset_index()
    tg.columns = ["genre", "count"]
    st.plotly_chart(px.bar(tg, x="count", y="genre", orientation="h", title="Top 10 Genres"), use_container_width=True)

with right:
    yr = filtered["year_added"].value_counts().sort_index().reset_index()
    yr.columns = ["year", "count"]
    st.plotly_chart(px.line(yr, x="year", y="count", title="Titles Added per Year"), use_container_width=True)

    tco = countries["country"].value_counts().head(10).reset_index()
    tco.columns = ["country", "count"]
    st.plotly_chart(px.bar(tco, x="count", y="country", orientation="h", title="Top 10 Countries"), use_container_width=True)

# searchable table
st.subheader("Search titles")
search = st.text_input("Type a title")
table = filtered[filtered["title"].str.contains(search, case=False, na=False)]
st.dataframe(table[["title", "type", "country", "release_year", "rating", "listed_in"]])