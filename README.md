# Learning Flask REST JWT Authentication

Learned following concepts:
1. Flask-JWT-Extended 

This app implements following routes
1. /signup
2. /signin
3. /users
4. /user/<string:username>
5. /refresh_token 

Following environment variables must be set before running this app:
```buildoutcfg
JWT_SECRET_KEY="<some-random-alpha-numeric-value>"
```

Database Tables:

User: (id, username, email, password)

