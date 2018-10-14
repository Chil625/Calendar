from flask_restful import Resource
from models.member import MemberModel


class Member(Resource):
    def get(self, name):
        member = MemberModel.find_by_name(name)
        if member:
            return member.json(), 200
        return {"message": "Member named {} was not found.".format(name)}, 404

    def post(self, name):
        if MemberModel.find_by_name(name):
            return {"message": "Member named {} is already exists.".format(name)}, 400
        member = MemberModel(name, 0)
        try:
            member.save_to_db()
        except:
            return {"message": "An error occurred while registering member."}, 500
        return member.json(), 201


class MemberList(Resource):
    def get(self):
        return {"members": [member.json() for member in MemberModel.query.filter(MemberModel.yuko_flg != 1).all()]}
