from flask_restful import Resource, reqparse
from models.date import DateModel


class Date(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument("year",
                        type=str,
                        required=True,
                        help="This field cannot be left blank!"
                        )
    parser.add_argument("month",
                        type=str,
                        required=True,
                        help="This field cannot be left blank!"
                        )
    parser.add_argument("day",
                        type=str
                        )
    parser.add_argument("member_no",
                        type=str
                        )
    parser.add_argument("member",
                        type=str)

    def get(self):
        data = Date.parser.parse_args()
        if data["day"]:
            date_info = DateModel.find_by_date(data["year"], data["month"], data["day"])
            return date_info.json(), 200
        return {"message": "You need to specify a day."}, 404

    def post(self):
        data = Date.parser.parse_args()
        if data["year"] and data["month"] and data["day"] and data["member_no"] and data["member"]:
            date_info = DateModel(data["year"], data["month"], data["day"], data["member_no"], data["member"])
            try:
                date_info.save_to_db()
            except:
                return {"message": "An error occurred while registering date info."}, 500
            return date_info.json(), 201


class DateInMonth(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument("year",
                        type=str,
                        required=True,
                        help="This field cannot be left blank!"
                        )
    parser.add_argument("month",
                        type=str,
                        required=True,
                        help="This field cannot be left blank!"
                        )

    def get(self):
        data = DateInMonth.parser.parse_args()
        return {"date_info_list": [day_info.json() for day_info in
                                   DateModel.query.filter_by(year=data["year"]).filter_by(month=data["month"]).all()]}
