
import pickle
import streamlit as st


# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="Movie Matcher",
    page_icon="🎬",
    layout="wide",
    initial_sidebar_state="collapsed"
)


# ============================================================
# CUSTOM CSS
# ============================================================

st.markdown(
    """
    <style>

    /* Main background */
    .stApp {
        background: linear-gradient(
            135deg,
            #0f0c29,
            #302b63,
            #24243e
        );
        color: white;
    }

    /* Page spacing */
    .block-container {
        padding-top: 2rem;
        padding-bottom: 3rem;
    }

    /* Main title */
    .main-title {
        text-align: center;
        font-size: 55px;
        font-weight: 900;
        margin-bottom: 5px;

        background: linear-gradient(
            90deg,
            #ff6a00,
            #ee0979,
            #8e2de2,
            #4facfe
        );

        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }

    /* Subtitle */
    .subtitle {
        text-align: center;
        color: #d7d7e8;
        font-size: 19px;
        margin-bottom: 40px;
    }

    /* Selection card */
    .selection-card {
        background: rgba(255, 255, 255, 0.08);
        border: 1px solid rgba(255, 255, 255, 0.15);
        border-radius: 20px;
        padding: 25px;
        margin-bottom: 20px;
        box-shadow: 0 10px 35px rgba(0, 0, 0, 0.30);
    }

    /* Select box */
    div[data-baseweb="select"] > div {
        background-color: rgba(255, 255, 255, 0.10);
        border: 1px solid rgba(255, 255, 255, 0.25);
        border-radius: 12px;
    }

    div[data-baseweb="select"] span {
        color: white !important;
    }

    /* Button */
    .stButton > button {
        width: 100%;
        border: none;
        border-radius: 14px;
        padding: 14px 20px;
        font-size: 18px;
        font-weight: 700;
        color: white;

        background: linear-gradient(
            90deg,
            #ff512f,
            #dd2476
        );

        box-shadow: 0 6px 20px rgba(221, 36, 118, 0.40);
    }

    .stButton > button:hover {
        transform: translateY(-3px);
        box-shadow: 0 10px 30px rgba(221, 36, 118, 0.60);
    }

    /* Recommendation heading */
    .recommend-title {
        text-align: center;
        font-size: 34px;
        font-weight: 800;
        margin-top: 40px;
        margin-bottom: 30px;
        color: white;
    }

    /* Movie card */
    .movie-card {
        background: rgba(255, 255, 255, 0.08);
        border: 1px solid rgba(255, 255, 255, 0.15);
        border-radius: 18px;
        padding: 25px 15px;
        min-height: 180px;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.30);
        backdrop-filter: blur(10px);
    }

    /* Movie title */
    .movie-title {
        font-size: 18px;
        font-weight: 700;
        text-align: center;
        color: white;
        margin-top: 15px;
        min-height: 50px;

        display: flex;
        align-items: center;
        justify-content: center;
    }

    /* Ranking */
    .rank {
        display: inline-block;

        background: linear-gradient(
            135deg,
            #ff6a00,
            #ee0979
        );

        border-radius: 50%;
        width: 45px;
        height: 45px;
        line-height: 45px;
        text-align: center;

        font-weight: 900;
        font-size: 18px;

        box-shadow: 0 5px 15px rgba(238, 9, 121, 0.4);
    }

    /* Footer */
    .footer {
        text-align: center;
        margin-top: 60px;
        padding-top: 20px;

        border-top: 1px solid rgba(255, 255, 255, 0.12);

        color: #aaaabd;
        font-size: 14px;
    }

    /* Labels */
    label {
        color: white !important;
        font-weight: 700 !important;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# ============================================================
# LOAD PICKLE FILES
# ============================================================

movies = pickle.load(
    open("movie_list.pkl", "rb")
)

similarity = pickle.load(
    open("similarity.pkl", "rb")
)


# ============================================================
# RECOMMENDATION FUNCTION
# ============================================================

def recommend(movie):
    index = movies[movies["title"] == movie].index[0]

    distances = sorted(
        list(enumerate(similarity[index])),
        reverse=True,
        key=lambda x: x[1]
    )

    recommended_movie_names = []

    for i in distances[1:6]:
        recommended_movie_names.append(
            movies.iloc[i[0]].title
        )

    return recommended_movie_names


# ============================================================
# HEADER
# ============================================================

st.markdown(
    '<div class="main-title">🎬 Movie Matcher</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    'Discover movies you might love based on your favorite films ✨'
    '</div>',
    unsafe_allow_html=True
)


# ============================================================
# MOVIE LIST
# ============================================================

movie_list = movies["title"].values


# ============================================================
# MOVIE SELECTION
# ============================================================

st.markdown(
    '<div class="selection-card">',
    unsafe_allow_html=True
)

selected_movie = st.selectbox(
    "🎥 Choose a movie",
    movie_list
)

st.markdown(
    "</div>",
    unsafe_allow_html=True
)




# ============================================================
# SHOW RECOMMENDATIONS
# ============================================================

if st.button("✨ Show Recommendations"):

    with st.spinner("🍿 Finding movies you may love..."):

        recommended_movie_names = recommend(selected_movie)

    st.markdown(
        '<div class="recommend-title">'
        '🍿 Recommended For You'
        '</div>',
        unsafe_allow_html=True
    )

    for movie_name in recommended_movie_names:

        st.markdown(
            f"""
            <div class="movie-card">
                <div class="movie-title">
                    {movie_name}
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )


# ============================================================
# FOOTER
# ============================================================

st.markdown(
    """
    <div class="footer">
        🎬 Movie Matcher
        &nbsp; • &nbsp;
        Powered by Machine Learning
    </div>
    """,
    unsafe_allow_html=True
)

