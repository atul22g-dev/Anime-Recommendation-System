# Import necessary libraries
import dill
import gzip
import pandas as pd

class AnimeRecommender:
    def __init__(self):
        # Load the model
        with gzip.open('model/anime_recommender.pkl.gz', 'rb') as f:
            self.model = dill.load(f)
        # Extract the recommender from the model
        self.recommender = self.model.named_steps['AnimeRecommender']
    def get_recommendations(self, anime_name, n=10):
        """Get anime recommendations similar to the given anime name"""
        try:
            return self.recommender.get_recommendations(anime_name, n)
        except Exception as e:
            print(f"Error in get_recommendations: {e}")
            # Fallback implementation if the original method fails
            try:
                # Get the anime dataframe
                anime_df = self.recommender.anime_df

                # Check if the anime exists
                if anime_name not in anime_df['english_name'].values:
                    print(f"Anime '{anime_name}' not found in database")
                    return pd.DataFrame()

                # Get the anime's genres
                anime_idx = anime_df[anime_df['english_name'] == anime_name].index[0]
                anime_genres = anime_df.iloc[anime_idx]['genres']

                print(f"Finding anime similar to '{anime_name}' with genres: {anime_genres}")

                # Find anime with similar genres
                similar_anime = []
                for idx, row in anime_df.iterrows():
                    if idx != anime_idx and isinstance(row['genres'], str) and isinstance(anime_genres, str):
                        # Calculate simple genre similarity
                        anime_genre_set = set([g.strip() for g in anime_genres.split(',')])
                        row_genre_set = set([g.strip() for g in row['genres'].split(',')])

                        # If there's any genre overlap, consider it similar
                        if len(anime_genre_set.intersection(row_genre_set)) > 0:
                            similar_anime.append(idx)

                # Limit to n recommendations
                if len(similar_anime) > n:
                    similar_anime = similar_anime[:n]

                print(f"Found {len(similar_anime)} similar anime")
                return anime_df.iloc[similar_anime].copy()
            except Exception as fallback_error:
                print(f"Fallback implementation also failed: {fallback_error}")
                return pd.DataFrame()

    def get_recommendations_by_genre(self, genre, n=10):
        """Get anime recommendations by genre"""
        try:
            return self.recommender.get_recommendations_by_genre(genre, n)
        except Exception as e:
            print(f"Error in get_recommendations_by_genre: {e}")
            # Fallback implementation
            try:
                # Get the anime dataframe
                anime_df = self.recommender.anime_df

                # Find anime with the specified genre
                genre_anime = []
                for idx, row in anime_df.iterrows():
                    if isinstance(row['genres'], str) and genre.lower() in row['genres'].lower():
                        genre_anime.append(idx)

                # Limit to n recommendations
                if len(genre_anime) > n:
                    genre_anime = genre_anime[:n]

                print(f"Found {len(genre_anime)} anime with genre '{genre}'")
                return anime_df.iloc[genre_anime].copy()
            except Exception as fallback_error:
                print(f"Fallback implementation also failed: {fallback_error}")
                return pd.DataFrame()

    def get_top_rated_anime(self, n=10):
        """Get top rated anime"""
        try:
            return self.recommender.get_top_rated_anime(n)
        except Exception as e:
            print(f"Error in get_top_rated_anime: {e}")
            # Fallback implementation
            try:
                # Get the anime dataframe
                anime_df = self.recommender.anime_df

                # Sort by score (higher is better) and return top n
                top_anime = anime_df.sort_values('score', ascending=False).head(n)
                print(f"Found {len(top_anime)} top rated anime")
                return top_anime.copy()
            except Exception as fallback_error:
                print(f"Fallback implementation also failed: {fallback_error}")
                return pd.DataFrame()

    def get_popular_anime(self, n=10):
        """Get most popular anime"""
        try:
            return self.recommender.get_popular_anime(n)
        except Exception as e:
            print(f"Error in get_popular_anime: {e}")
            # Fallback implementation
            try:
                # Get the anime dataframe
                anime_df = self.recommender.anime_df

                # Check if 'rank' column exists, otherwise use 'score'
                if 'rank' in anime_df.columns:
                    # Sort by rank (lower is better) and return top n
                    popular_anime = anime_df.sort_values('rank').head(n)
                else:
                    # Sort by score (higher is better) and return top n
                    popular_anime = anime_df.sort_values('score', ascending=False).head(n)

                print(f"Found {len(popular_anime)} popular anime")
                return popular_anime.copy()
            except Exception as fallback_error:
                print(f"Fallback implementation also failed: {fallback_error}")
                return pd.DataFrame()

    def search_anime(self, query):
        """Search for anime by name"""
        try:
            return self.recommender.search_anime(query)
        except Exception as e:
            print(f"Error in search_anime: {e}")
            # Fallback implementation
            try:
                # Get the anime dataframe
                anime_df = self.recommender.anime_df

                # Simple case-insensitive search
                query = query.lower()
                results = anime_df[anime_df['english_name'].str.lower().str.contains(query)]

                print(f"Found {len(results)} anime matching '{query}'")
                return results.copy()
            except Exception as fallback_error:
                print(f"Fallback implementation also failed: {fallback_error}")
                return pd.DataFrame()

    def get_anime_details(self, anime_name):
        """Get details for a specific anime"""
        anime_df = self.recommender.anime_df
        return anime_df[anime_df['english_name'] == anime_name].iloc[0].to_dict() if anime_name in anime_df['english_name'].values else None

    def get_all_genres(self):
        """Get a list of all available genres"""
        # Extract all genres from the anime dataframe
        all_genres = []
        for genres in self.recommender.anime_df['genres'].dropna():
            if isinstance(genres, str):
                all_genres.extend([g.strip() for g in genres.split(',')])
        # Return unique genres sorted alphabetically
        return sorted(list(set(all_genres)))

    def get_all_anime_names(self):
        """Get a list of all anime names"""
        return self.recommender.anime_df['english_name']
