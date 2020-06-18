import json


def main():
    airline = dict(
        type='record',
        name='Airline',
        fields=[
            dict(name='airline_id', type='int', default=-1),
            dict(name='name', type='string', default="NONE"),
            dict(name='alias', type='string', default="NONE"),
            dict(name='iata', type='string', default="NONE"),
            dict(name='icao', type='string', default="NONE"),
            dict(name='callsign', type='string', default="NONE"),
            dict(name='country', type='string', default="NONE"),
            dict(name='active', type='boolean', default=False),
        ]
    )

    airport = dict(
        type='record',
        name='Airport',
        fields=[
            dict(name='airport_id', type='int', default=-1),
            dict(name='name', type='string', default="NONE"),
            dict(name='city', type='string', default="NONE"),
            dict(name='iata', type='string', default="NONE"),
            dict(name='icao', type='string', default="NONE"),
            dict(name='latitude', type='double'),
            dict(name='longitude', type='double'),
            dict(name='timezone', type='double'),
            dict(name='dst', type='string', default="NONE"),
            dict(name='tz_id', type='string', default="NONE"),
            dict(name='type', type='string', default="NONE"),
            dict(name='source', type='string', default="NONE")
        ]
    )

    route = dict(
        type='record',
        name='Route',
        namespace='edu.bellevue.dsc650',
        fields=[
            dict(name="airline", type=airline, default={}),
            dict(name="src_airport", type=airport, default={}),
            dict(name="dst_airport", type="Airport", default={}),
            dict(name='codeshare', type='boolean', default=False),
            dict(name='stops', type='int', default=0),
            dict(name='equipment', type=dict(type='array', items='string'))
        ]
    )

    with open('schemas/routes.avsc', 'w') as f:
        json.dump(route, f, indent=2)


if __name__ == '__main__':
    main()