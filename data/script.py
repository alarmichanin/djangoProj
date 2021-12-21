import json
import random

citiesArr = ["./stations/kyivData.json", "./stations/dniproData.json", "./stations/kharkivData.json",
             "./stations/lvivData.json", "./stations/zaporizhzhiaData.json", "./stations/zhmerynkaData.json"]
stations = "./stations.json"
trains = "./trains.json"
routes = "./routes.json"
routeStations = "./routeStations.json"

stationsArr = []
stationsForEveryRoute = []
trainsStart = []
trainsEnd = []

objArr = []
index = 0
for city in citiesArr:
    with open(city, 'r', encoding='utf-8') as f:
        templates = json.load(f)
    # for appending start and end points
    for key, value in templates[0].items():
        obj = {}
        # value - arr of routes
        index += 1
        obj['id'] = index
        obj['route'] = value
        objArr.append(obj)

with open(routeStations, 'w', encoding='utf8') as rtSt:
    templatesRtSt = []
    pkStations = 1
    pkSchema = 0
    for o in objArr:
        pkSchema += 1
        templatesOfStations = []
        for every in o["route"]:
            objStation = {"pk": pkStations, "fields": {}, "model": "search_ticket.Station"}
            objStation["fields"]["name"] = every
            pkStations += 1
            templatesOfStations.append(objStation)
        schema = [
            *templatesOfStations,
            {
                "pk": pkSchema,
                "model": "search_ticket.Route",
                "fields": {
                    "start_point": [elem["pk"] for elem in templatesOfStations][0],
                    "end_point": [elem["pk"] for elem in templatesOfStations][len([elem["pk"] for elem in templatesOfStations])-1],
                    "slug": f'{[elem["pk"] for elem in templatesOfStations][0]}-{[elem["pk"] for elem in templatesOfStations][len([elem["pk"] for elem in templatesOfStations])-1]}'
                }
            },
            {
                "pk": pkSchema,
                "model": "search_ticket.RouteStation",
                "fields":
                    {
                        "route": pkSchema,
                        "stations": [elem["pk"] for elem in templatesOfStations],
                        "time": "17:41:28",
                        "price_from_start": random.randint(100, 300)
                    }
            },
            {
                "pk": pkSchema,
                "model": "search_ticket.RoutTrain",
                "fields":
                    {
                        "route": pkSchema,
                        "train": [pkSchema]
                    }
            },
            {
                "pk": pkSchema,
                "model": "search_ticket.Train",
                "fields":
                    {
                        "number_of_railcar": random.randint(15, 30),
                        "name": f'{o["route"][0]}-{o["route"][len(templatesOfStations) - 1]}',
                        "slug": f'{[elem["pk"] for elem in templatesOfStations][0]}-{[elem["pk"] for elem in templatesOfStations][len([elem["pk"] for elem in templatesOfStations])-1]}'
                    }
            }
        ]
        templatesRtSt += schema
    json.dump(templatesRtSt, rtSt, ensure_ascii=False)
