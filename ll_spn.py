import requests


def geocode(address):
    # Собираем запрос для геокодера.
    geocoder_request = f"http://geocode-maps.yandex.ru/1.x/"
    geocoder_params = {
        "apikey": "40d1649f-0493-4b70-98ba-98533de7710b",
        "geocode": address,
        "format": "json"}

    # Выполняем запрос.
    json_response = requests.get(geocoder_request, params=geocoder_params).json()

    # Получаем первый топоним из ответа геокодера.
    # Согласно описанию ответа он находится по следующему пути:
    features = json_response["response"]["GeoObjectCollection"]["featureMember"]
    return features[0]["GeoObject"] if features else None


def get_ll_span(address):
    toponym = geocode(address)
    if not toponym:
        return (None, None)

    # Координаты центра топонима:
    toponym_coodrinates = toponym["Point"]["pos"]
    # Долгота и Широта :
    toponym_longitude, toponym_lattitude = toponym_coodrinates.split(" ")

    # Собираем координаты в параметр ll
    ll = ",".join([toponym_longitude, toponym_lattitude])

    # Рамка вокруг объекта:
    envelope = toponym["boundedBy"]["Envelope"]

    # левая, нижняя, правая и верхняя границы из координат углов:
    l, b = envelope["lowerCorner"].split(" ")
    r, t = envelope["upperCorner"].split(" ")

    # Вычисляем полуразмеры по вертикали и горизонтали
    dx = abs(float(l) - float(r)) / 2.0
    dy = abs(float(t) - float(b)) / 2.0

    # Собираем размеры в параметр span
    span = f"{dx},{dy}"

    return ll, span


# def get_ll_span2(address1, ll2, ):
#     toponym1 = geocode(address1)
#     # toponym2 = geocode(address1)
#     if not toponym1:
#         return (None, None)
#
#     # Координаты центра топонима:
#     toponym_coodrinates1 = toponym1["Point"]["pos"]
#     # toponym_coodrinates2 = toponym2["Point"]["pos"]
#     # Долгота и Широта :
#     toponym_longitude1, toponym_lattitude1 = toponym_coodrinates1.split(" ")
#     toponym_longitude2, toponym_lattitude2 = toponym_coodrinates2.split(" ")
#
#
#     # Собираем координаты в параметр ll
#     ll1 = ",".join([toponym_longitude1, toponym_lattitude1])
#     # ll2 = ",".join([toponym_longitude2, toponym_lattitude2])
#
#     # Рамка вокруг объекта:
#     envelope1 = toponym1["boundedBy"]["Envelope"]
#     envelope2 = toponym2["boundedBy"]["Envelope"]
#
#     # левая, нижняя, правая и верхняя границы из координат углов:
#     l1, b1 = envelope1["lowerCorner"].split(" ")
#     r1, t1 = envelope1["upperCorner"].split(" ")
#     l2, b2 = envelope2["lowerCorner"].split(" ")
#     r2, t2 = envelope2["upperCorner"].split(" ")
#
#     print("l1", l1)
#     print("b1", b1)
#     print("r1", r1)
#     print("t1", t1)
#     print("l2", l2)
#     print("b2", b2)
#     print("r2", r2)
#     print("t2", t2)
#     # Вычисляем полуразмеры по вертикали и горизонтали
#     dx = abs(float(l1) - float(r1)) / 2.0
#     dy = abs(float(t1) - float(b1)) / 2.0
#
#     # Собираем размеры в параметр span
#     span = f"{dx},{dy}"
#
#     return ll, span
