
import streamlit as st
import pandas as pd

# ==========================================
# PAGE CONFIGURATION
# ==========================================

st.set_page_config(
    page_title="Movie Data Explorer | Lihi Admoni",
    page_icon="🎬",
    layout="wide"
)

# ==========================================
# WEBSITE DESIGN
# ==========================================

st.markdown("""
<style>
.stApp {
    background: linear-gradient(
        135deg, #0B1020 0%, #141B35 100%
    );
    color: #F1F5F9;
}

.block-container {
    max-width: 1100px;
    padding-top: 3rem;
    padding-bottom: 4rem;
}

h1, h2, h3 {
    color: #F8FAFC !important;
    font-family: 'Arial', sans-serif;
}

h1 {
    font-size: 3rem !important;
    font-weight: 800 !important;
}

h2 {
    padding-top: 20px;
    color: #A5B4FC !important;
}

p, li {
    color: #CBD5E1;
    line-height: 1.8;
    font-size: 16px;
}

.hero {
    background: linear-gradient(
        120deg, #312E81, #1E3A8A
    );
    border: 1px solid #6366F1;
    border-radius: 24px;
    padding: 36px;
    margin-bottom: 30px;
}

.hero-title {
    color: white;
    font-size: 42px;
    font-weight: 800;
    margin-bottom: 12px;
}

.hero-subtitle {
    color: #E0E7FF;
    font-size: 18px;
}

.info-card {
    background: #1E293B;
    border: 1px solid #334155;
    border-radius: 18px;
    padding: 24px;
    margin: 12px 0;
    min-height: 140px;
}

.card-title {
    font-size: 17px;
    font-weight: bold;
    color: #A5B4FC;
    margin-bottom: 10px;
}

.card-text {
    font-size: 15px;
    color: #E2E8F0;
    line-height: 1.7;
}

.metric-card {
    background: #1E293B;
    border: 1px solid #4338CA;
    border-radius: 18px;
    padding: 26px;
    text-align: center;
    margin-bottom: 16px;
}

.metric-number {
    font-size: 42px;
    font-weight: 800;
    color: #A5B4FC;
}

.metric-label {
    font-size: 15px;
    color: #CBD5E1;
}

.section-label {
    color: #818CF8;
    font-weight: 700;
    letter-spacing: 2px;
    font-size: 13px;
    margin-top: 35px;
}

.feature-card {
    background: #1E293B;
    border-left: 4px solid #818CF8;
    border-radius: 12px;
    padding: 22px;
    margin: 12px 0;
}

.feature-name {
    color: #C4B5FD;
    font-size: 21px;
    font-weight: bold;
}

.target-card {
    background: linear-gradient(
        110deg, #312E81, #1E3A5F
    );
    border-radius: 18px;
    border: 1px solid #818CF8;
    padding: 30px;
    margin: 20px 0;
}

[data-testid="stDataFrame"] {
    border-radius: 12px;
    overflow: hidden;
}

hr {
    border-color: #334155;
    margin: 35px 0;
}
</style>
""", unsafe_allow_html=True)


# ==========================================
# HEADER
# ==========================================

st.markdown("""
<div class="hero">
    <div class="hero-title">
        🎬 Movie Data Explorer
    </div>
    <div class="hero-subtitle">
        Exploring movie data, discovering patterns,
        and preparing for future predictions.
    </div>
    <p style="color:#C7D2FE; margin-top:18px;">
        Software Engineering Project 1 |
        Lihi Admoni
    </p>
</div>
""", unsafe_allow_html=True)


# ==========================================
# SECTION 1 - ABOUT THE DATASET
# ==========================================

st.markdown(
    '<div class="section-label">SECTION 01</div>',
    unsafe_allow_html=True
)

st.header("About the Dataset")

st.markdown("""
<div class="info-card">
    <div class="card-title">
        TMDB 5000 Movie Dataset
    </div>
    <div class="card-text">
        This project explores the TMDB 5000 Movie Dataset,
        which contains information about 4,803 movies.
        <br><br>
        Each row represents one movie, while each column
        represents a different characteristic of that movie.
        <br><br>
        The dataset includes information such as production
        budget, revenue, movie runtime, popularity,
        and audience ratings.
        <br><br>
        The goal is to understand the data and explore
        which movie characteristics might help predict
        movie revenue in the future.
    </div>
</div>
""", unsafe_allow_html=True)


# ==========================================
# SECTION 2 - DATA OVERVIEW
# ==========================================

st.markdown(
    '<div class="section-label">SECTION 02</div>',
    unsafe_allow_html=True
)

st.header("Data Overview")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="metric-card">
        <div class="metric-number">4,803</div>
        <div class="metric-label">Movies / Rows</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="metric-card">
        <div class="metric-number">20</div>
        <div class="metric-label">Dataset Columns</div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="metric-card">
        <div class="metric-number">7</div>
        <div class="metric-label">Numeric Columns</div>
    </div>
    """, unsafe_allow_html=True)


# ==========================================
# MISSING VALUES
# ==========================================

st.subheader("Missing Values")

st.write(
    "Some columns contain missing information. "
    "The table below shows the columns with missing values."
)

missing_data = pd.DataFrame({
    "Column": [
        "homepage",
        "tagline",
        "overview",
        "runtime",
        "release_date"
    ],
    "Missing Values": [
        3091,
        844,
        3,
        2,
        1
    ],
    "Missing (%)": [
        64.36,
        17.57,
        0.06,
        0.04,
        0.02
    ]
})

st.dataframe(
    missing_data,
    hide_index=True,
    use_container_width=True
)

st.markdown("""
<div class="info-card">
    <div class="card-title">
        🔎 What can we learn?
    </div>
    <div class="card-text">
        The <b>homepage</b> column contains the most
        missing values. This may be because some movies
        do not have an official website.
        <br><br>
        The <b>tagline</b> column also contains many
        missing values, possibly because not every movie
        has a promotional slogan.
        <br><br>
        Missing values in <b>overview</b>, <b>runtime</b>,
        and <b>release_date</b> may result from information
        that was not recorded.
        <br><br>
        Missing data could affect future analysis and
        prediction models. At this stage, we identify
        the missing values without modifying them.
    </div>
</div>
""", unsafe_allow_html=True)


# ==========================================
# NUMERICAL AVERAGES
# ==========================================

st.subheader("Numerical Column Averages")

averages = pd.DataFrame({
    "Column": [
        "budget",
        "id",
        "popularity",
        "revenue",
        "runtime",
        "vote_average",
        "vote_count"
    ],
    "Average": [
        "29,045,040",
        "57,165.48",
        "21.49",
        "82,260,640",
        "106.88",
        "6.09",
        "690.22"
    ]
})

st.dataframe(
    averages,
    hide_index=True,
    use_container_width=True
)

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="info-card">
        <div class="card-title">
            ⏱ Average Movie Runtime
        </div>
        <div class="card-text">
            The average movie runtime is approximately
            <b>106.88 minutes</b>, or about
            1 hour and 47 minutes.
            <br><br>
            This is a reasonable length for a movie,
            suggesting that the average runtime is
            similar to that of a typical feature film.
        </div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="info-card">
        <div class="card-title">
            ⭐ Average Vote Count
        </div>
        <div class="card-text">
            The average number of votes per movie
            is approximately <b>690.22</b>.
            <br><br>
            However, some movies receive thousands
            of votes while others receive very few.
            Popular movies may have a strong influence
            on this average.
        </div>
    </div>
    """, unsafe_allow_html=True)


# ==========================================
# SECTION 3 - PREDICTION PLAN
# ==========================================

st.markdown(
    '<div class="section-label">SECTION 03</div>',
    unsafe_allow_html=True
)

st.header("Prediction Plan")

st.write(
    "The next stage of this project will involve "
    "building a regression model to predict movie revenue."
)

st.markdown("""
<div class="target-card">
    <div style="color:#C7D2FE; font-size:14px;">
        TARGET VARIABLE (y)
    </div>
    <div style="color:white; font-size:34px;
                font-weight:bold; margin:12px 0;">
        revenue
    </div>
    <div class="card-text">
        Revenue represents the money earned by a movie.
        <br><br>
        I selected this variable because it is numerical,
        making it suitable for a future regression model.
        The goal will be to estimate movie revenue
        using other movie characteristics.
    </div>
</div>
""", unsafe_allow_html=True)

st.subheader("Selected Prediction Features")

st.write(
    "I selected three columns that may help "
    "predict movie revenue:"
)

st.markdown("""
<div class="feature-card">
    <div class="feature-name">
        01 / budget
    </div>
    <div class="card-text">
        The production budget may influence a movie's
        financial success.
        <br><br>
        Movies with larger budgets can often invest
        more in advertising, visual effects, and
        well-known actors.
        <br><br>
        These factors may attract larger audiences
        and lead to higher revenue.
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="feature-card">
    <div class="feature-name">
        02 / popularity
    </div>
    <div class="card-text">
        A movie's popularity may be related
        to its financial performance.
        <br><br>
        More popular movies may attract
        larger audiences and sell more tickets,
        potentially generating higher revenue.
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="feature-card">
    <div class="feature-name">
        03 / vote_average
    </div>
    <div class="card-text">
        Audience ratings may influence movie revenue.
        <br><br>
        Movies with higher ratings may receive
        more positive recommendations,
        encouraging additional people to watch them.
        <br><br>
        This could contribute to increased revenue.
    </div>
</div>
""", unsafe_allow_html=True)


# ==========================================
# FOOTER
# ==========================================

st.divider()

st.markdown("""
<p style="text-align:center; color:#94A3B8;">
    🎬 Movie Data Explorer
    <br>
    Software Engineering Project 1 | Lihi Admoni
</p>
""", unsafe_allow_html=True)
