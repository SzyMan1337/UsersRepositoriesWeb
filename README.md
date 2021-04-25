# UsersRepositoriesWeb

## Goal
The application is a solution for recruitment of internship at Allegro Summer eXperience 2021.

## Deployment
Application is avaible at [Heroku](https://user-repositories-allegro.herokuapp.com/).
It provides two functionalities:
* Listing all user's repositories with number of stars. Invocation: 
  * /repositories?username=name
* Returning sum of all user repositorie's star. Invocation:
  * /rating?username=name

For example [all repositories of user SzyMan1337](https://user-repositories-allegro.herokuapp.com/repositories?username=SzyMan1337). 
* https://user-repositories-allegro.herokuapp.com/repositories?username=SzyMan1337
Sum of user [SzyMan1337 repositorie's starSzyMan1337](https://user-repositories-allegro.herokuapp.com/rating?username=SzyMan1337). 
* https://user-repositories-allegro.herokuapp.com/rating?username=SzyMan1337

## Technologie
Całość kodu jest napisana w Pythonie 3.8.5. z użyciem bibliotek:
* FastAPI 0.63.0
* requests 2.25.1
* pydantic 1.8.1
