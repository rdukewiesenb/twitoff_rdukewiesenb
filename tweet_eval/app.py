from flask import Flask, render_template
from .model import DB, User, Tweet, example_users

def create_app():
    app = Flask(__name__)
    app.config['SQLAlchemy_DATABASE_URI'] = "sqlite3://db.sqlite3"
    app.config['SQLQLCHEMY_TRACK_MODIFICATIONS'] = False
    DB.init_app(app)

    @app.route('/')
    def root():
        DB.drop_all()
        DB.create_all()
        example_users()
        return render_template("base.html", title="Home", users=User.query.all())

    return app


"""
IN TERMINAL: 
    IN FLASK SHELL:
        from tweet_eval.model import *
        example_users()
        User.query.all()



        from tweet_eval.model import User, Tweet
        user = User(id=1, name='user')
        tweet = Tweet(id=1, text='test', user=user)
        user.tweets

       test = User.query.first()
       test.tweets
"""