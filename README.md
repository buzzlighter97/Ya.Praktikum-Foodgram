[![CI](https://github.com/buzzlighter97/foodgram-project/actions/workflows/main.yml/badge.svg)](https://github.com/buzzlighter97/foodgram-project/actions/workflows/main.yml)

# Foodgram.

  Foodgram is a service where you can create and discover new recipes to cook.

# Run
1. Install Docker and Docker Compose.
2. Clone repository https://github.com/buzzlighter97/foodgram-project.git
3. Rename ```.env-example``` to ```.env``` and fill it with secret values.
4. Change working directory to foodgram-project folder and run ```docker-compose up -d```
5. Open web container ```docker exec -it foodgram-project_web_1 bash```
6. Run commands:
   
   ```python manage.py collectstatic``` - collects static to static/.
   
   ```python manage.py migrate``` - executes all migrations
   
   ```python manage.py loadingredients``` - custom manage.py command to load ingridients
   
   ```python manage.py createsuperuser``` - fill credentials for new django superuser.
   
   ```python manage.py runserver```
4. Go to http://localhost:8080/ or http://localhost:8080/admin/ for an admin panel.

# Functionality
* Full user authentication.
* CRUD for recipe.
* Filter by breakfast/lunch/dinner.  
* Choose from a bunch of pre-installed ingredients.
* Gather favorite recipes.
* Follow another authors.
* Add ingredients to shopping list.
* Download shopping list.

# Stack used
* Python
* Django
* Django REST Framework
* PostgreSQL
* Docker
* Nginx
* Gunicorn