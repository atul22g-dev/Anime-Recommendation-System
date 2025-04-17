import streamlit as st
from helper.recommendation_engine import AnimeRecommender
from helper.func.Func import display_anime, display_anime_list

# Page Title
st.set_page_config(page_title="Anime Recommendation System", layout="wide")

# Hide Streamlit Header and Footer and add custom styling
st.markdown("""
    <style>
        header {visibility: hidden;}
        footer {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)

# Initialize the recommender
@st.cache_resource
def load_recommender():
    return AnimeRecommender()

recommender = load_recommender()

# Title and Description
st.title("🎬 Anime Recommendation System")
st.markdown("""
    <div style='background-color: #1E3A8A; padding: 15px; border-radius: 10px; color: white; margin-bottom: 20px;'>
        <h3 style='margin:0; color: white;'>Find your next favorite anime with our recommendation system!</h3>
        <p>Discover new anime based on your preferences, genres, ratings, and more.</p>
    </div>
""", unsafe_allow_html=True)

# Sidebar Options
recommendation_type = st.sidebar.radio(
    "Select Recommendation Type",
    ["Similar to an Anime", "By Genre", "Top Rated", "Most Popular", "Search"]
)

# Similar to an Anime
if recommendation_type == "Similar to an Anime":
    # Get a list of all anime names for the dropdown
    anime_names = recommender.get_all_anime_names()

    # Create a dropdown to select an anime
    selected_anime = st.selectbox("Select an anime you like:", anime_names)

    # Number of recommendations slider
    num_recommendations = st.slider("Number of recommendations", 1, 20, 6)

    if st.button("Get Recommendations"):
        with st.spinner("Finding similar anime..."):
            # Get anime details
            anime_details = recommender.get_anime_details(selected_anime)
            if anime_details:
                st.subheader("Selected Anime")
                display_anime(anime_details)

                # Get recommendations
                recommendations = recommender.get_recommendations(selected_anime, num_recommendations)
                display_anime_list(recommendations, "Recommended Anime")
            else:
                st.error("Anime not found in the database.")

# By Genre
elif recommendation_type == "By Genre":
    # Get all genres
    genres = recommender.get_all_genres()

    # Create a dropdown to select a genre
    selected_genre = st.selectbox("Select a genre:", genres)

    # Number of recommendations slider
    num_recommendations = st.slider("Number of recommendations", 1, 20, 6)

    if st.button("Get Recommendations"):
        with st.spinner(f"Finding {selected_genre} anime..."):
            # Get recommendations by genre
            recommendations = recommender.get_recommendations_by_genre(selected_genre, num_recommendations)
            display_anime_list(recommendations, f"Top {selected_genre} Anime")

# Top Rated
elif recommendation_type == "Top Rated":
    # Number of recommendations slider
    num_recommendations = st.slider("Number of top rated anime", 1, 50, 10)

    if st.button("Get Top Rated"):
        with st.spinner("Finding top rated anime..."):
            # Get top rated anime
            top_rated = recommender.get_top_rated_anime(num_recommendations)
            display_anime_list(top_rated, "Top Rated Anime")

# Most Popular
elif recommendation_type == "Most Popular":
    # Number of recommendations slider
    num_recommendations = st.slider("Number of popular anime", 1, 50, 10)

    if st.button("Get Most Popular"):
        with st.spinner("Finding most popular anime..."):
            # Get popular anime
            popular = recommender.get_popular_anime(num_recommendations)
            display_anime_list(popular, "Most Popular Anime")

# Search
elif recommendation_type == "Search":
    # Search box
    search_query = st.text_input("Search for anime:", "")

    if search_query:
        with st.spinner(f"Searching for '{search_query}'..."):
            # Search for anime
            search_results = recommender.search_anime(search_query)
            display_anime_list(search_results, "Search Results")
