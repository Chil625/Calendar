from db import db


class DateModel(db.Model):
    __tablename__ = "DATE_INFO"

    year = db.Column(db.String(4), primary_key=True)
    month = db.Column(db.String(2), primary_key=True)
    day = db.Column(db.String(2), primary_key=True)
    # 1, 2で一日あたり二人にする
    member_no = db.Column(db.Integer, primary_key=True)
    member = db.Column(db.String(16), db.ForeignKey("MEMBERS.name"))

    def __init__(self, year, month, day, member_no, member):
        self.year = year
        self.month = month
        self.day = day
        self.member_no = member_no
        self.member = member

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def json(self):
        return {"year": self.year,
                "month": self.month,
                "day": self.day,
                "member_no": self.member_no,
                "member": self.member}

    @classmethod
    def find_by_date(cls, year, month, day):
        return cls.query.filter_by(year=year).filter_by(month=month).filter_by(day=day).first()

    @classmethod
    def find_by_member_in_this_month(cls, year, month, name):
        return cls.query.filter_by(year=year).filter_by(month=month).filter_by(member=name).all()
