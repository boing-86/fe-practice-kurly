from app import db


class Recent(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    weight = db.Column(db.Float, nullable=False)
    create_time = db.Column(db.DateTime(), nullable=False)


class Expected(db.Model):
    e_id = db.Column(db.Integer, primary_key=True)
    id = db.Column(db.Integer, db.ForeignKey('recent.id', ondelete='CASCADE'))
    min = db.Column(db.Float, nullable=False)
    max = db.Column(db.Float, nullable=False)


recent = db.relationship('Recent', backref=db.backref('answer_set'))