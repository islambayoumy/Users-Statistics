# Users-Statistics
Simple python statistical script using '[pandas](https://pandas.pydata.org/)' and '[matplotlib](https://matplotlib.org/)' within [Django](https://www.djangoproject.com) framework.
#### ~ It isn't a ready for production, yet it is just a proof of concept 

### Assumptions
* uploaded file formate must be CSV
* data columns [user_id, country, language, user_level, created_time]

## Getting start (deployment)
### Prerequisites
* python 3
* virtualenv

### 1. Clone project
`$ git clone https://github.com/islambayoumy/Users-Statistics`
~ change directory to project folder  

### 2. Create Virtualenv
`$ virtualenv env`

### 3. Activate Virtualenv
`$ source env/Scripts/activate`

### 4. Install required packages inside Virtualenv
`$(env) pip install -r requirements.txt`

### 5. Run server
`$(env) python manage.py runserver`

* browse the application through http://127.0.0.1:8000/stats/

 ## Further plans
 - integrate with tools like (django-rest-pandas)[https://github.com/wq/django-rest-pandas]
