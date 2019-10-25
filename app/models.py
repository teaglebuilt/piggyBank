from sqlalchemy_utils import URLType
from . import db


class Resource(db.Model):
    id          = db.Column(db.Integer, primary_key=True)
    name        = db.Column(db.String, nullable=False)
    url         = db.Column(URLType, nullable=True, unique=True)
    data        = db.Column(db.String(300))
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=False)
    category    = db.relationship('Category')
    tag_id      = db.Column(db.Integer, db.ForeignKey('tag.id'))
    tags        = db.relationship('Tag')

    def __repr__(self):
        return f"<Resource \n\tName: {self.name}\n\tTags: {self.tags}\n\tCategory: {self.category}\n\tURL: {self.url}\n>"



class Category(db.Model):
    id      = db.Column(db.Integer, primary_key=True)
    name    = db.Column(db.String, nullable=False)

    def __repr__(self):
        return f"<Category {self.name}>"


class Tag(db.Model):
    id      = db.Column(db.Integer, primary_key=True)
    name    = db.Column(db.String, nullable=False)

    def __repr__(self):
        return f"<Tag {self.name}>"


