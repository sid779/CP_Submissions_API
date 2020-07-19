# CP Submissions Tracker API

A simple Rest API which fetches user submissions from Stopstalk and return a json object containing data.

    {
    "Username": "User",
    "CodeChef": 173,
    "CodeForces": 485,
    "HackerRank": 237,
    "Hackerearth": 33,
    "Spoj": 40,
    "AtCoder": 0,
    "UVa": 0,
     "Total": 968
        }
### Usage:
- The API is deployed on Heroku @ https://cp-flask-api.herokuapp.com

#### Getting Data
- Use = https://cp-flask-api.herokuapp.com/ <"username">

##### Behaviour
- If the username is correct the it returns a JSON like above example.
- If the username is correct but user doesn't have submissions then

    `{ "About": "No Submissions" }`
- If the username is incorrect/ not registered in Stopstalk then

    `{"About": "USER NOT FOUND"}`
