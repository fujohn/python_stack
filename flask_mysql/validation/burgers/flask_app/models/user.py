from flask_bcrypt import Bcrypt        
bcrypt = Bcrypt(app)    # we are creating an object called bcrypt, 
                        # which is made by invoking the function Bcrypt with our app as an argument



from flask import flash
import re	# the regex module
# create a regular expression object that we'll use later   
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 
class User:
    @staticmethod
    def validate_user( user ):
        is_valid = True
        # test whether a field matches the pattern
        if not EMAIL_REGEX.match(user['email']): 
            flash("Invalid email address!")
            # flash("Email cannot be blank!", 'email')
            is_valid = False
        return is_valid

# bcrypt hashing insert (register)
    @classmethod
    def save(cls,data):
        query = "INSERT INTO users (username, password) VALUES (%(username)s, %(password)s);"
        return connectToMySQL("mydb").mysql.query_db(query, data)

# bcrypt hashing insert (login)
    @classmethod
    def get_by_email(cls,data):
        query = "SELECT * FROM users WHERE email = %(email)s;"
        result = connectToMySQL("mydb").query_db(query,data)
        # Didn't find a matching user
        if len(result) < 1:
            return False
        return cls(result[0])

##################################### associating users in classes

# tweet related
from twitter_app.models import tweet
# Other imports here...
class User:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.handle = data['handle']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        # [] can represent a currently empty place to store all of the tweets that a single User instance has created, as a User creates MANY Tweets
        self.tweets = [] 

from twitter_app.models import user
# Other imports here...
class Tweet:
    def __init__(self, data):
        self.id = data['id']
        self.content = data['content']
        self.location = data['location']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at'] 
        # None can represent a currently empty space for a single User dictionary to be placed here, as a Tweet is made by ONE User. We want a User instance and all their attributes to be placed here, so something like data['...'] will not work as we have to make the User instance ourselves.
        self.creator = None
    
    @classmethod
    def get_all_tweets_with_creator(cls):
        # Get all tweets, and their one associated User that created it
        query = "SELECT * FROM tweets JOIN users ON tweets.user_id = users.id;"
        results = connectToMySQL('real_twitter').query_db(query)
        all_tweets = []
        for row in results:
            # Create a Tweet class instance from the information from each db row
            one_tweet = cls(row)
            # Prepare to make a User class instance, looking at the class in models/user.py
            one_tweets_author_info = {
                # Any fields that are used in BOTH tables will have their name changed, which depends on the order you put them in the JOIN query, use a print statement in your classmethod to show this.
                "id": row['users.id'], 
                "name": row['name'],
                "handle": row['handle'],
                "email": row['email'],
                "password": row['password'],
                "created_at": row['users.created_at'],
                "updated_at": row['users.updated_at']
            }
            # Create the User class instance that's in the user.py model file
            author = user.User(one_tweets_author_info)
            # Associate the Tweet class instance with the User class instance by filling in the empty creator attribute in the Tweet class
            one_tweet.creator = author
            # Append the Tweet containing the associated User to your list of tweets
            all_tweets.append(one_tweet)
        return all_tweets



