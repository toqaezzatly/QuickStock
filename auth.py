from functools import wraps
from flask import session, redirect, url_for, request, flash
from database import db_create_user, db_get_user
from werkzeug.security import generate_password_hash, check_password_hash

def hash_password(password):
    return generate_password_hash(password)

def verify_password(password, hashed_password):
    return check_password_hash(hashed_password, password)

def create_user(username, password):
    hashed_password = hash_password(password)
    return db_create_user(username, hashed_password)

def authenticate_user(username, password):
    user = db_get_user(username)
    if user and verify_password(password, user['password']):
        return user
    return None

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            flash('Please log in to access this page.', 'warning')
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function
