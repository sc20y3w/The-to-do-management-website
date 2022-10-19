# It was written because without it, the application would jump again and again
# between form and models.py and app.py.
from exts import db


class Module(db.Model):
    __tablename__ = "module"
    id = db.Column(db.String(200), primary_key=True, nullable=False)
    module_name = db.Column(db.String(200), nullable=False)


# Define ORM model(total assessments)
class Total(db.Model):
    __tablename__ = "total"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.String(200), nullable=False)
    ddl = db.Column(db.Date, nullable=False)
    finish = db.Column(db.String(200), nullable=False)
    module_id = db.Column(db.String(200), db.ForeignKey("module.id"))
    module = db.relationship("Module", backref="assessments")
