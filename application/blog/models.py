from datetime import datetime

from application import db, ma

class Post(db.Model):
    """
        Création de la table posts dans la 
        base de données
    """
    __tablename__ = "posts"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), nullable=False)
    author = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text(), nullable=False)
    date = db.Column(db.DateTime(), default=datetime.utcnow())

    def __str__(self):
        return self.title


class PostSchema(ma.Schema):
    """
        Création du schema qui nous permettra de sérialiser
        les champs (colonnes) de la base de données
    """
    class Meta:
        model = Post
        fields = ("id", "title", "author", "content", "date")




