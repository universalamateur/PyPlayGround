# Deploying Python on Deta

## Requirments

1. Install in CLI Deta tools

```=bash
curl -fsSL https://get.deta.dev/cli.sh | sh
```

```=psh
iwr https://get.deta.dev/cli.ps1 -useb | iex
```

2. Logging in to Deta via the CLI

```=bash
deta login
```

## A first test deploy

1. create a micro, navigate in your Terminal to a parent directory for micro and type:

```=bash
deta new --python MICRONAME
```

2. This will create a new Python Micro as well as a local copy inside a directory called MICRONAME which will contain a main.py file.
The CLI should respond:

```=json
{
    "name": "MICRONAME",
    "runtime": "python3.7",
    "endpoint": "https://<path>.deta.dev",
    "visor": "enabled",
    "http_auth": "enabled"
}
```

3. Opening Your Micro To the Public

```=bash
deta auth disable
```

4. Details about the deta endooint in this folder

```=bash
deta details
```

5. Prepare the Deploy

Enter the directory *MICRONAME*, and then create a file, *requirements.txt*, which tells Deta which dependencies to install.

6. Updating Code Locally

Manipulate the *MICRONAME/main.py* for the result

7. Deploying Local Changes

Use a deta deploy command in the folder *MICRONAME* to update your Micro.

```=bash
deta deploy
```

8. Visiting the Endpoint

under *`https://<path>.deta.dev`* out of the *`deta details`* command the app is visible

## Additional Info

We need to call our app instance *app* and it has to be in a file called *main.py*, which is the only required file for a Python Micro. Of course we can add more files and folders.

## Changes on Base Structure 

Inspiration from [Digital ocean without the docker part](https://www.digitalocean.com/community/tutorials/how-to-build-and-deploy-a-flask-application-using-docker-on-ubuntu-18-04)

HomeDir
|-app
|-app-tepmplates
|-app-tepmplates-home.html
|-app-__init.py__
|-app-views.py
|-main.py

- main.py just imports the module app `from app import app`
- *-app-__init.py__* imports flask and views.py
- *-app-views.py* has the trigger in it, which are shown in different http calls and imports templates to work with it