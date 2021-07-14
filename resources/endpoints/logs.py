import datetime as dt
import glob

from flask import Blueprint, jsonify
from flask_restful import Resource, Api
from webargs import fields, validate
from webargs.flaskparser import use_args, use_kwargs



class AddResource(Resource):
    """An addition endpoint."""

    add_args = {"x": fields.Float(required=True), "y": fields.Float(required=True)}

    @use_kwargs(add_args)
    def post(self, x, y):
        """An addition endpoint."""
        return {"result": x + y}


class DateAddResource(Resource):

    dateadd_args = {
        "value": fields.Date(required=False),
        "addend": fields.Int(required=True, validate=validate.Range(min=1)),
        "unit": fields.Str(
            missing="days", validate=validate.OneOf(["minutes", "days"])
        ),
    }

    @use_kwargs(dateadd_args)
    def post(self, value, addend, unit):
        """A date adder endpoint."""
        value = value or dt.datetime.utcnow()
        if unit == "minutes":
            delta = dt.timedelta(minutes=addend)
        else:
            delta = dt.timedelta(days=addend)
        result = value + delta
        return {"result": result.isoformat()}


logs_api = Blueprint('resources', __name__)
api = Api(logs_api)
api.add_resource(AddResource, "/add")
api.add_resource(DateAddResource, "/dateadd")