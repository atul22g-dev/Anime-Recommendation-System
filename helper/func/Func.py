import streamlit as st
import pandas as pd

# Function to display anime details
def display_anime(anime, use_columns=True):
    if use_columns:
        col1, col2 = st.columns([1, 3])

        with col1:
            if 'image_url' in anime and anime['image_url']:
                st.image(anime['image_url'], width=200)
            else:
                st.image("https://placehold.co/600x400?text=No+Image", width=200)

        with col2:
            st.markdown(f"### {anime['english_name']}")

            # Display basic info in a single line
            st.markdown(f"**Score:** {anime.get('score', 'N/A')} | **Episodes:** {anime.get('episodes', 'N/A')} | **Rank:** {anime.get('rank', 'N/A')}")

            # Display genres
            if 'genres' in anime and anime['genres']:
                st.markdown(f"**Genres:** {anime['genres']}")

            # Display studios
            if 'studios' in anime and anime['studios']:
                st.markdown(f"**Studios:** {anime['studios']}")

            # Display synopsis
            if 'describe' in anime and anime['describe']:
                with st.expander("Description"):
                    st.write(anime['describe'])
    else:
        # Non-column version for nested contexts
        st.markdown(f"### {anime['english_name']}")

        if 'image_url' in anime and anime['image_url']:
            st.image(anime['image_url'], width=150)
        else:
            st.image("https://placehold.co/600x400?text=No+Image", width=150)

        # Display basic info in a single line
        st.markdown(f"**Score:** {anime.get('score', 'N/A')} | **Episodes:** {anime.get('episodes', 'N/A')} | **Rank:** {anime.get('rank', 'N/A')}")

        # Display genres
        if 'genres' in anime and anime['genres']:
            st.markdown(f"**Genres:** {anime['genres']}")

        # Display studios
        if 'studios' in anime and anime['studios']:
            st.markdown(f"**Studios:** {anime['studios']}")

        # Display synopsis
        if 'describe' in anime and anime['describe']:
            with st.expander("Description"):
                st.write(anime['describe'])

# Function to display a list of anime
def display_anime_list(anime_list, title=None):
    if title:
        st.subheader(title)

    # Convert to DataFrame if it's not already
    if not isinstance(anime_list, pd.DataFrame):
        anime_list = pd.DataFrame(anime_list)

    # Check if DataFrame is empty
    if anime_list.empty:
        st.info("No anime found.")
        return

    # Display each anime in a card
    for i in range(len(anime_list)):
        with st.container():
            st.markdown("<div class='anime-card'>", unsafe_allow_html=True)
            anime = anime_list.iloc[i]
            display_anime(anime, use_columns=True)
            st.markdown("</div>", unsafe_allow_html=True)
            st.markdown("<hr style='margin: 15px 0;'>", unsafe_allow_html=True)