from find_businesses import find_business
from ll_spn import get_ll_span
from show_map import show_map
from distance import ll_distance
import sys

ll_1 = " ".join(sys.argv[1:])
biz = find_business(ll_1, '0.005, 0.005', 'аптека')
print(biz)
ll = get_ll_span(biz['properties']['description'])[0]
spn = str(abs((tuple(map(float, ll_1.split(',')))[0] - tuple(map(float, ll.split(',')))[0]) * 2)) + ',' + \
      str(abs((tuple(map(float, ll_1.split(',')))[1] - tuple(map(float, ll.split(',')))[1]) * 2))
a = {
    'адрес': biz['properties']['description'],
    'название': biz['properties']['name'],
    'время работы': biz['properties']["CompanyMetaData"]["Hours"]['text'],
    'расстояние до неё' : ll_distance(map(float, ll_1.split(',')), map(float, ll.split(',')))
}

ll_spn = f'll={ll}&spn={spn}'
for k in a.keys():
    print(f'{k}: {a[k]}')
show_map(ll_spn, add_params=f'pt={ll_1},pmwtm1~{ll},pmwtm2')