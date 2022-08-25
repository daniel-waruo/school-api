# School API

## Setup

The first thing to do is to clone the repository:

```sh
$ git clone https://github.com/daniel-waruo/school-api.git
$ cd school-api
```

Create a virtual environment to install dependencies in and activate it:

```sh
$ virtualenv2 --no-site-packages env
$ source env/bin/activate
```

Then install the dependencies:

```sh
(env)$ pip install -r requirements.txt
```
Note the `(env)` in front of the prompt. This indicates that this terminal
session operates in a virtual environment set up by `virtualenv2`.

Once `pip` has finished downloading the dependencies:
```sh
(env)$ cd project
(env)$ python manage.py runserver
```
And navigate to `http://127.0.0.1:8000/api/v1/docs/`.

Inorder to view all thw endpoints in the system

## Documentation
I have created POSTMAN Documentation for the above application and the link can be found below.
`https://documenter.getpostman.com/view/8930707/VUqxKuXR`

## Tests

To run the tests, `cd` into the directory where `manage.py` is:
```sh
(env)$ python manage.py test 
```
