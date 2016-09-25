from functools import wraps
from flask import redirect, request, session
import logging

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
                    datefmt='%m-%d %H:%M',
                    filename='myapp.log',
                    filemode='w')

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not session.get('logged_in'):
            logging.info('dec: you not logged_in!!');
            return redirect('/login')
        return f(*args, **kwargs)
    return decorated_function
