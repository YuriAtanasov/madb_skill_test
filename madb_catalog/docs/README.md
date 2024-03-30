# Implementation steps

## Django frontend

- Created authentication user
    **Action >>>**  username: django-admin / pass: admin / mail: <django-admin@localhost.com>

    ```bash
        python3 manage.py createsuperuser
    ```

    e.g:**test** user: user1 / pass: user@user1 / mail: <user.one@gmail.com>
        **access level:** favorites + upload movies + Admin panel movies catalog view

> *.py scripts located @ `madb_catalog`

- settings.py
    **Action >>>** Added `movies` to the INSTALLED_APPS list. Added comment to distinguish frame from code.
    **Action >>>** Added STATIC_URL and STATICFILES_DIRS to the settings file.
    **Action >>>** Added MEDIA_URL and MEDIA_ROOT to the settings file.
    **Action >>>** Added LOGIN_URL to the settings file.
    **Action >>>** Added paths with os.path for DB and MEDIA files.

- migrations ${repo_home}/madb_catalog/manage.py
    **Action >>>** Executed migrations to create app database.
    **Action >>>** Created superuser for the app.
    **Action >>>** Added favorite movies to the DB.

- urls.py
    **Action >>>** Added url patterns for the app. E.g. base, catalog, admin, etc.
    **Action >>>** extend urlpatterns with include() functions STATIC and MEDIA files.

## Python backend

> *.py scripts located @ `madb_backend`

- `models.py`
    **Action >>>** define movie structure.

- `admin.py`
    **Action >>>** import model.
    **Action >>>** register the movie model.

- `forms.py`
    **Action >>>** Created form for movie model for adding movies to DB.

- `views.py`
    **Action >>>** Created view Classes for movie model.
    **Action >>>** Added `get` and `post` methods for upload form.

- `templates/`

  - `clients/`
    **Action >>>** Created .html files for Add_Movie_form.

  - `movie_catalog/images/movies`
    **Action >>>** Created images folders for backend.

  - `movie_catalog/pages`
    **Action >>>** Created application *.html files for the madb app

    ```bash
        mkdir -p ../madb_backend/templates/movie_catalog/pages && \
        cd ../madb_backend/templates/movie_catalog/pages && \
        touch movie_list.html && \
        touch movie_detail.html && \
        touch about_me.html && \
        touch base.html
        cd -
    ```

  - `static/`
    **Action >>>** Created *.html files for top-rated, most-watched, recently-added

    ```bash
        mkdir -p ../madb_backend/templates/stats && \
        cd ../madb_backend/templates/stats && \
        touch top_rated.html && \
        touch most_watched.html && \
        touch recently_added.html
        cd -
    ```

- `urls.py`
    **Action >>>** Added url patterns for the app. Used `Class` and `views` (related to `views.py`)
    **Action >>>** extend path with pages for movie_upload_form, search, favorites
    **Action >>>** Added paths for top-rated, most-watched and recently added movies functionality

## Functionalities

- Serve on load  `http://127.0.0.1:8000`

  - / - file located in `{BASE_DIR}/templates/movie_catalog/pages/base.html`
  - /catalog/ - file located in `{BASE_DIR}/templates/movie_catalog/pages/movie_list.html`
  - /catalog/<movie_db_id>/ - file located in `{BASE_DIR}/templates/movie_catalog/pages/movies_detail.html`
  - images for movies - file located in `{BASE_DIR}/templates/movie_catalog/images/movies`
  - /catalog/favorites/ - file located in `{BASE_DIR}/templates/clients/favorite_movies.html`
  - /catalog/form_base - file located in `{BASE_DIR}/templates/clients/form_base.html`
  - /catalog/upload/ - file located in `{BASE_DIR}/templates/clients/add_movies.html`
  - /about - file located in `{BASE_DIR}/templates/movie_catalog/pages/about_me.html`
  - /admin/login/ - menu "Login" redirects to `http://127.0.0.1:8000/admin/login/?next=/admin`
  - ..search..bar - file located in `{BASE_DIR}/templates/movie_catalog/pages/search.html`
  - top-rated/ - file located in `{BASE_DIR}/templates/stats/top_rated_.html`
  - most-watched/ - file located in `{BASE_DIR}/templates/stats/most_watched.html`
  - recently-added/ - file located in `{BASE_DIR}/templates/stats/recently_added.html`

- Functional menu

  - HOME -> redirects to `http://127.0.0.1:8000`
  - Movies Catalog -> opens movie catalog `http://127.0.0.1:8000/catalog`
  - Favorites -> opens user's favorites (requires login) `http://127.0.0.1:8000/catalog/favorites`
  - Upload movie -> opens upload form page `http://127.0.0.1:8000/catalog/form_base`
    - Button at the bottom redirects to `http://127.0.0.1:8000/catalog/upload` - form for adding movies
  - Login - opens Django admin `http://127.0.0.1:8000/admin/login`
  - Search bar - performs a search by "title" and "genre" in the movie catalog
  - Top rated movies - opens `http://127.0.0.1:8000/catalog/top-rated`
  - Most watched movies - opens `http://127.0.0.1:8000/catalog/most-watched`
  - Recently added movies - opens `http://127.0.0.1:8000/catalog/recently-added`
