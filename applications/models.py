from main import db

class users(db.Model):
    __tablename__ = "users"
    user_id = db.Column(db.Integer, primary_key = True, autoincrement = True, unique = True, nullable = False)
    username = db.Column(db.String, unique = True, nullable = False)
    password = db.Column(db.String, nullable = False)
    score = db.Column(db.Integer, nullable = False, default = 0)

class easy(db.Model):
    __tablename__ = "easy"
    word = db.Column(db.String, primary_key = True, nullable = False, unique = True)
    synonyms = db.Column(db.String, nullable = False)

class medium(db.Model):
    __tablename__ = "medium"
    word = db.Column(db.String, primary_key = True, nullable = False, unique = True)
    synonyms = db.Column(db.String, nullable = False)

class hard(db.Model):
    __tablename__ = "hard"
    word = db.Column(db.String, primary_key = True, nullable = False, unique = True)
    synonyms = db.Column(db.String, nullable = False)