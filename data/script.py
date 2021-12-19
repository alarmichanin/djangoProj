import json
import random

citiesArr = ["./stations/kyivData.json", "./stations/dniproData.json", "./stations/kharkivData.json",
             "./stations/lvivData.json", "./stations/zaporizhzhiaData.json", "./stations/zhmerynkaData.json"]
stations = "./stations.json"
trains = "./trains.json"
routes = "./routes.json"

stationsArr = []
trainsStart = []
trainsEnd = []
for city in citiesArr:
    with open(city, 'r', encoding='utf-8') as f:
        templates = json.load(f)
    # for appending start and end points
    for key, value in templates[0].items():
        trainsStart.append(value[0])
        trainsEnd.append(value[len(value) - 1])
    # for appending stations
    for i in range(0, len(templates)):
        for key, value in templates[i].items():
            for elem in value:
                if not (elem in stationsArr):
                    stationsArr.append(elem)

with open(trains, 'w', encoding='utf8') as tr:
    templatesTr = []
    for index, item in enumerate(trainsStart, start=1):
        schema = {
            "model": "search_ticket.Train",
            "pk": index,
            "fields": {
                "name": f'{item}-{trainsEnd[index - 1]}',
                "number_of_railcar": random.randint(15, 30)
            }
        }
        templatesTr.append(schema)
    json.dump(templatesTr, tr, ensure_ascii=False)

with open(routes, 'w', encoding='utf8') as rt:
    templatesRt = []
    for index, item in enumerate(trainsStart, start=1):
        schema = {
            "model": "search_ticket.Route",
            "pk": index,
            "fields": {
                "start_point": item,
                "end_point": trainsEnd[index - 1],
                "rout_train": 1,
                "rout_station": 1
            }
        }
        templatesRt.append(schema)
    json.dump(templatesRt, rt, ensure_ascii=False)

with open(stations, 'w', encoding='utf8') as st:
    templatesSt = []
    for index, item in enumerate(stationsArr, start=1):
        schema = {
            "model": "search_ticket.Station",
            "pk": index,
            "fields": {
                "name": item
            }
        }
        templatesSt.append(schema)
    json.dump(templatesSt, st, ensure_ascii=False)
