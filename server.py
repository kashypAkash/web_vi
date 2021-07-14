"""A simple number and datetime addition JSON API.
Run the app:
    $ python examples/flaskrestful_example.py
Try the following with httpie (a cURL-like utility, http://httpie.org):
    $ pip install httpie
    $ http GET :5001/
    $ http GET :5001/ name==Ada
    $ http POST :5001/add x=40 y=2
    $ http POST :5001/dateadd value=1973-04-10 addend=63
    $ http POST :5001/dateadd value=2014-10-23 addend=525600 unit=minutes
"""

from flask import Flask
from flask_restful import Api
from webargs.flaskparser import parser, abort
from resources.endpoints.logs import logs_api
from config import DEBUG, HOST, PORT

app = Flask(__name__)
api = Api(app)
app.register_blueprint(logs_api)



# # This error handler is necessary for usage with Flask-RESTful
# @parser.error_handler
# def handle_request_parsing_error(err, req, schema, *, error_status_code, error_headers):
#     """webargs error handler that uses Flask-RESTful's abort function to return
#     a JSON error response to the client.
#     """
#     abort(error_status_code, errors=err.messages)


if __name__ == "__main__":
    app.run(port=PORT, debug=DEBUG, host=HOST)