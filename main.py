# Libs
from libs.storage import Storage
from modules.calendar.calendar import Calendar
from modules.calendar.filter import Filter
from modules.auth.auth import Auth
import json
from modules.user.user import User



credientials = Auth("1193096338", "1193096338").login()
User(credentials=credientials).get_info()
# #credientials = {'SSO_ID': 'v1.2~1~C349CBCF730F785B7D03BCDDF0DAFD67A50A9094C1A0668D9239A9788329DE2C9C127B24D9741B76E747894C4CFA5185C9A7BF7F1E50B14983875E8CC75631B085A6F9D1EB6B77D144CBF61FCC8C4B185A3481B0230229B39FF929E3363FAE03572F5824B6E65F4FA2E68078FD8D363963EDA213AC6CEFA0E572091249746B00A407B53FFAAAE05A5EBBE3060750E14FF873976E7457F648A70B8E2561653E460BECE9512DE43FC9EE5F47103E1710E0FD259245BFBA9DE247E61A84C69156A4447EB13B50F07A45F372138B875072334433CCA08A82748353C1404762F5B63A04DDF208C36531D36A34BEAF01B61531034A6DE3FE488F9F'}
# data = Calendar(credientials)
# filter_data = Filter(data=data.get_class(option="80%232022")).filter(
#     week_days=data.get_calendar_days(),
#     day="thursday"
# )
# print(filter_data)
# print(json.dumps(filter_data, indent=2))
