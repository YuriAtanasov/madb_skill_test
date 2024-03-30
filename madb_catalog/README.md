# Skillo Final Exam - Python Project

## Project title

Movie Database Application

## Project Description

In this project, you have to create a CLI Python application that serves as a movie database.
The application has to use SQLite as a database and provide features for listing, viewing,
searching, adding, and categorizing movies.

## Requirements

### I. Functionality ( **CLI** )

1) Movie Listing Page: **movlst**

    > - When executed this command should return a structured representation of all the movies in the database.

2) Movie Details Page: **movdt** **`<movie_id>`**

    > - Users should be able to get the details of a movie if it exists in the database.
    > - Details may include the movie's **title**, **description**, **release date**, **director**, **genre**, and **user ratings**.

3) Search Functionality: **movsrch** **`<query>`**

    > - Users should be able to search for movies based on their titles.
    > - Search results should be a structured representation of all the movies that match the search query.

4) Adding New Movies: **movadd** **`<title>, <desc>, <date>, <director>, <genre>`**

    > - Users can add new movies to the database.
    > - They should provide details such as the movie's **title**, **description**, **release date**, **director**, and **genre**.

5) Favorites: **movfv** **`<movie_id>`**

    > - Users should be able to mark movies as their favorites.

6) Movie Categories: **movcat** **`<category: [liked, newest, genre]>`**

    > - Movies will be categorized by genres.
    > - Sections like "**Most Liked**," "**Newest**," and "**Genres**" will feature the top 5 movies in each category.

#### **CLI** technical requirements

- Follow all the OOP principles and good practices.
- Implement SQLite as the database to store movie information.
- Have a good database structure including tables and relations.
- Have well-written project documentation.
- Have proper project and apps structure and separation.

### II. Functionality ( **Django** )

1) Movie Listing Page:
    > - The application will have a main page that lists all the movies in the database.
    > - Each movie will be displayed with its title and a brief description.

2) Movie Details Page:
    > - When a user clicks on a movie from the listing, it will open a new page with detailed information about that movie.
    > - Details may include the movie's **title**, **description**, **release date**, **director**, **genre**, and **user ratings**.

3) Search Functionality
    > - Users can search for movies based on their **titles**, **directors**, or **genres**.
    > - Search results will be displayed on a separate page.

4) Adding New Movies
    > - Users can add new movies to the database.
    > - They should provide details such as the movie's **title**, **description**, **release date**, **director**, **genre**, and **upload** a cover image.

5) Favorites
    > - Users can mark movies as their favorites.
    > - There will be a section where users can view and manage their favorite movies.

6) Movie Categories
    > - Movies will be categorized by genres.
    > - Sections like "**Most Liked**," "**Newest**," and "**Genres**" will feature the top 5 movies in each category.
    &#9888; **Important:** &#9888; The categories should be sorted as follows:
        **Most Liked** = **MOST_WATCHED**
        **Newest** = **TOP_RATED**
        **Genres** = **RECENTLY ADDED**

#### **Django** technical requirements

- Use Django for building the web application.
- Implement SQLite as the database to store movie information.
- Utilize Django models for defining the movie data structure.
- Create views and templates for displaying movie details and listing.
- Implement search functionality using Django's query capabilities.
- Allow user registration and login for managing favorites.
- Use Django's ORM for database operations.
- Have well-written project documentation.
- Have proper project and apps structure and separation.
