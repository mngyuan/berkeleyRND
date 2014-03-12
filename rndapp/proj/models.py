from rndapp.data import CRUDMixin, db

class Project(CRUDMixin, db.Model):
    __tablename__ = 'project_list'

    user_id = db.Column(db.Integer, db.ForeignKey('users_user.id'))
    title = db.Column(db.String)
    description = db.Column(db.String)

    def __repr__(self):
        return '<Project: {:id} {} {}>'.format(self.id,self.title, self.description)

    def __str__(self):
        return self.title    