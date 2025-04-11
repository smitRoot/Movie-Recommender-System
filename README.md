

# Movie Recommendation System using TMDB 5000 Movie Dataset

## Overview

This project is a **Movie Recommendation System** developed using the **TMDB 5000 Movie Dataset**, leveraging **collaborative filtering** and **content-based** algorithms to provide personalized movie suggestions based on user preferences.

The system allows users to interact with the recommendation engine via a simple and intuitive graphical user interface (GUI) built with **Streamlit**. The recommendations are fetched dynamically using the **TMDB API** to display movie details and posters in real time.

The entire application has been deployed on **Heroku**, providing seamless cloud access for real-time movie recommendations.

---

## Features

- **Personalized Movie Recommendations**: Uses collaborative filtering and content-based algorithms to recommend movies based on users' viewing history and preferences.
- **Dynamic Movie Posters & Details**: Fetches and displays movie posters and additional details (such as genres, ratings, and release year) dynamically from the TMDB API.
- **User-Friendly Interface**: Built using **Streamlit**, making it easy for users to interact with the system and explore recommended movies.
- **Cloud Deployment**: Hosted on **Heroku** for smooth, real-time access from anywhere.

---

## Technologies Used

- **Python**: The core programming language used for data processing and building recommendation algorithms.
- **Pandas**: For data manipulation and processing.
- **Scikit-learn**: For implementing collaborative filtering and content-based recommendation algorithms.
- **Streamlit**: For creating an interactive user interface (GUI).
- **TMDB API**: For fetching real-time movie details and posters.
- **Heroku**: For deploying the application on the cloud.

---

## Setup & Installation

Follow the instructions below to run the application locally or contribute to the project.

### 1. Clone the Repository

Clone the repository to your local machine using the following command:

```bash
git clone https://github.com/smitRoot/Movie-Recommender-System.git
cd Movie-Recommender-System
```

### 2. Install Required Libraries

It's recommended to use a virtual environment (e.g., `venv`, `conda`) to manage dependencies. You can install the required libraries by running:

```bash
pip install -r requirements.txt
```

### 3. Obtain TMDB API Key

To access movie details and posters, you need to obtain an API key from [TMDB](https://www.themoviedb.org/).

- Go to the [TMDB API page](https://www.themoviedb.org/settings/api).
- Sign up or log in to TMDB.
- Generate a new API key.
- Save your API key in a `.env` file or add it directly to the code where necessary.

### 4. Run the Application

Once you have installed the dependencies and configured the TMDB API key, run the Streamlit application with the following command:

```bash
streamlit run app.py
```

### 5. Access the Application

Open your browser and navigate to `http://localhost:8501` to interact with the movie recommendation system locally.

---

## How It Works

### 1. Data Preprocessing

The **TMDB 5000 Movie Dataset** is used to build the recommendation engine. The dataset is preprocessed to extract movie features such as:

- Movie titles
- Genres
- Popularity ratings
- User ratings (if available)

### 2. Recommendation Algorithms

Two types of recommendation algorithms are employed:

- **Collaborative Filtering**: Uses user ratings to recommend movies based on similar preferences from other users.
- **Content-Based Filtering**: Uses the movie's features (e.g., genre, keywords) to recommend similar movies to the ones the user likes.

### 3. TMDB API Integration

The application integrates with the TMDB API to fetch movie details such as:

- Movie poster images
- Plot summaries
- Release year
- Genres
- User ratings

### 4. Streamlit Interface

The application presents a clean and easy-to-navigate interface using Streamlit, where users can:

- Enter their movie preferences.
- View movie recommendations dynamically.
- Explore movie details and images.

---

---

## Future Improvements

Here are some potential improvements for the project:

- **User Profile**: Implement user authentication and personalized user profiles for saving preferences.
- **Improved Algorithms**: Enhance the recommendation system with hybrid algorithms or deep learning-based models for better accuracy.
- **Search Functionality**: Add a search feature to allow users to search for specific movies.
- **Mobile Responsiveness**: Optimize the Streamlit interface for mobile devices.

---



## Acknowledgements

- **TMDB**: For providing the TMDB 5000 Movie Dataset and the TMDB API for movie details.
- **Streamlit**: For creating a powerful and easy-to-use interface framework.
- **Heroku**: For providing a free and reliable platform to deploy the application.
- **Nitish-Singh-Campux**: For providing end to end guidance
---

