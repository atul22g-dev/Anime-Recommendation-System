# Anime Recommendation System

A content-based anime recommendation system that suggests anime based on similarity, genres, popularity, etc.

## Prerequisites

- Python 3.10
- git-lfs

## Features

- **Similar Anime Recommendations**: Find anime similar to ones you already enjoy
- **Genre-based Recommendations**: Discover anime in specific genres
- **Top Rated Anime**: Browse the highest-rated anime
- **Popular Anime**: See what's trending
- **Search Functionality**: Find anime by name

## Model

The system uses the `anime_recommender.pkl` model stored using the dill package, which includes information about anime Collection, such as:
- Anime ID and name
- Image URL
- Score and rating
- Genres
- Description
- Episodes
- Producers and studios
- Popularity and favorites

## How It Works

The recommendation engine uses content-based filtering with TF-IDF vectorization and cosine similarity to find anime with similar characteristics. The system analyzes features like genres, descriptions, studios, and producers to determine similarity.

## Installation

### Clone and Run Locally

1. Clone this repository
2. Create a virtual environment:
   ```
   python -m venv venv
   ```
3. Activate the virtual environment:
   ```
   venv\Scripts\activate
   ```
4. Install the required packages:
   ```
   pip install -r requirements.txt
   ```
5. Import Large File Storage:
   ```
   git lfs pull
   ```
6. Run the Streamlit app:
   ```
   streamlit run app.py
   ```

### Option 2: Using Docker

1. Make sure you have Docker installed on your system
2. Build the Docker image:
   ```
   docker build -t anime-recommender .
   or
   docker build -t ghcr.io/atul22g-dev/anime-recommendation-system .
   ```
3. Run the Docker container:
   ```
   docker run -p 8501:8501 anime-recommender
   or
   docker run -p 8501:8501 ghcr.io/atul22g-dev/anime-recommendation-system
   ```
4. Access the application in your browser at:
   ```
   http://localhost:8501
   ```

## Docker Details

The included Dockerfile sets up a containerized environment for the application with the following features:

- Based on Python 3.10 slim image
- Automatically installs all required dependencies
- Exposes port 8501 for the Streamlit interface
- Includes the recommendation model

**Note**: The Docker image will be relatively large (~500MB) due to the inclusion of the recommendation model file.
