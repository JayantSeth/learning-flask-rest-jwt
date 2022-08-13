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

References:
```buildoutcfg
https://blog.teclado.com/jwt-authentication-and-token-refreshing-in-rest-apis/
https://flask-jwt-extended.readthedocs.io/en/stable/v4_upgrade_guide/
https://stackoverflow.com/questions/66279295/flask-app-doent-register-jwt-user-lookup-loader-flask-jwt-extended
https://flask-jwt-extended.readthedocs.io/en/stable/refreshing_tokens/
https://flask-jwt-extended.readthedocs.io/en/stable/api/
https://stackoverflow.com/questions/40165665/flask-restful-vs-flask-restplus
https://flask-jwt-extended.readthedocs.io/en/stable/automatic_user_loading/
```
