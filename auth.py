from functools import wraps
from flask import session, redirect, url_for, request
from database import db_create_user, db_get_user
import hashlib

def hash_password(password):
  return hashlib.sha256(password.encode()).hexdigest()

def create_user(username, password):
  hashed_password = hash_password(password)
  return db_create_user(username, hashed_password)

def authenticate_user(username, password):
  user = db_get_user(username)
  if user and hash_password(password) == user['password']:
    return user
  return None

def login_required(f):
  @wraps(f)
  def decorated_function(*args, **kwargs):
    if 'user_id' not in session:
      return redirect(url_for('login'))
    return f(*args, **kwargs)
  return decorated_function