from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

# Set variables for car chart
series = ['Lotus Elise SC 2007', 'Subaru WRX STI 2017', 'Honda S2000 2009']
labels = ['kW', 'l/100km', 'Fuel tank capacity']
data = [
    [162, 8.5, 43.5],
    [227, 10.5, 60],
    [177, 10, 50]
]


# Send chart data for cars as json
class CarsData(Resource):
    def get(self):
        return [series, labels, data]


# Set Api resource routing
api.add_resource(CarsData, '/api/cars')


# Send index.html as static file
@app.route('/')
def start():
    return app.send_static_file('index.html')


if __name__ == '__main__':
    app.run(debug=True)
