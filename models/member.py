from db import db


class MemberModel(db.Model):
    __tablename__ = "MEMBERS"

    name = db.Column(db.String(16), primary_key=True)
    # 0またはなし: 有効, 1: 無効
    # やめた場合や、長期で休業の場合などに使用
    yuko_flg = db.Column(db.Integer)

    def __init__(self, name, yuko_flg):
        self.name = name
        self.yuko_flg = yuko_flg

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def json(self):
        return {"name": self.name,
                "yuko_flg": self.yuko_flg}

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first()

    @classmethod
    def find_by_yuko_flg(cls, yuko_flg):
        return cls.query.filter_by(yuko_flg=yuko_flg).all()
