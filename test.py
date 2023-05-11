from modules.auth.auth import Auth
import requests
from libs.burpeer import parse_request
from modules.califications.califications import Califications
import datetime


credientials = Auth("1193096338", "123amarillo").login()
print(credientials)
OPTIONS = Califications(credientials).options()
HEADERS = parse_request('/home/riuz/Escritorio/unipaz-movile-backend/request')[0]

print(OPTIONS)
for option in OPTIONS:
    response = requests.post(
            url="http://unipaz.uxxi.com/portal/page/portal/uxxiportal/academico/Mis%20actas%20parciales",
            # headers=self.config.get("headers"),
            data=f"_piref35_712116_35_710664_710664.strutsAction=MisNotasParciales%2FInicioMisNotasParcialesAction.do&asignatura={option}",
            headers=HEADERS,
            cookies=credientials,
            allow_redirects=False
    )
    print(option)
    print(response.status_code)
    open(f"{datetime.datetime.now().__hash__()}.html", "w").write(f"_piref35_712116_35_710664_710664.strutsAction=MisNotasParciales%2FInicioMisNotasParcialesAction.do&idPac=2023-A%232023&planEstudio=63D%23109&asignatura={option}"+ response.text)
