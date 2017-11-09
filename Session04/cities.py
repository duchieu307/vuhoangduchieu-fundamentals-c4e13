from haversine import haversine


cities = [
    {
        'name' : "Ha Noi",
        'lat' : 21.0277644,
        'long' : 105.83415979999995,
    },

    {
        'name': 'Hue',
        'lat' : 16.4498,
        'long' : 107.5623501,
    },
    {
        'name': 'Danang',
        'lat' : 16.0544068,
        'long' : 108.20216670000002
    },
    {
        'name': 'HoChiMinh',
        'lat' : 10.8230989,
        'long' : 106.6296638,
    }
]

for i in range(len(cities) - 1):
    for j in range(i + 1 , len(cities)):


        city1 = cities[i]
        city2 = cities[j]

        cord1 = [city1['lat'], city1['long']]
        cord2 = [city2['lat'], city2['long']]

        distance = haversine(cord1, cord2)

        print("Khoang cach tu {0} den {1} la {2}".format(city1["name"], city2['name'], distance))
        print()
