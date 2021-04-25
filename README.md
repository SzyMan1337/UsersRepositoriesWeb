# UsersRepositoriesWeb

## Goal
The application is a solution for recruitment of internship at Allegro Summer eXperience 2021.

## Deployment
Application is avaible at [Heroku](https://user-repositories-allegro.herokuapp.com/).
It provides two functionalities:
* Listing all user's repositories with number of stars. Invocation: 
  * /repositories?username=name
* Returning sum of all user repositorie's stars. Invocation:
  * /rating?username=name

For example all repositories of user SzyMan1337
* https://user-repositories-allegro.herokuapp.com/repositories?username=SzyMan1337

Sum of user SzyMan1337 repositorie's stars 
* https://user-repositories-allegro.herokuapp.com/rating?username=SzyMan1337

## Possible development
* Possibility to compare users repositories. 
* Getting more information about a repository.

## Technologies
Whole code is writen in Python 3.8.5. with the use of libraries:
* FastAPI 0.63.0
* requests 2.25.1
* pydantic 1.8.1
