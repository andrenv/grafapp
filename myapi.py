from flask_restplus import Api

api = Api(version='0.1', title='Auctioneer API', description='Auction Managing Enginge')

@api.errorhandler
def std_handler(e):
    return {'message': 'An unexpected error has occured. Please contact the support.', 'e': e}, 500
