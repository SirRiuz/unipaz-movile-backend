
PAYLOAD_DIR = 'payload'
SITE_TOKEN = r"v1.2%7E59076E25%7E59815768CE303485ECD932FED1CC60D61EDD780197402B33150F687D41867309684A13E181D638355A9E738BBBE4685588BAAE3A8269307A6E960776ED8B6E013A6692B9AE2FF9FAC3866AF3215558FB5EFDF5A20F45F48B5FEF8AC2E83FE53F7EC055FA6790B045867CBE9B4DAC5C45F2688805A504FB81C82CD2B888AF3EE36E954974CED4F50F293B75FFCF144A777F26914E1D215718A41EFE5D78A7C0E9C6B1EB011896457BBA81ABDDC1208734855C156E6F150DFFBEF7522BC4C4B3EE54078AC97378A67F3105AE2CF4CFF6A8E90750A3D0BE38344678ABDD5B19DAA9D4165EF2DFEA34D3"


PAYLOAD_REQUEST = f"site2pstoretoken={SITE_TOKEN}&password=PASSWORD&ssousername=USER_NAME"
PAYLOAD_CHANGE_REQUEST = f"oldpassword=USER&newpassword=PAYLOAD_PASSWORD&confpassword=PAYLOAD_PASSWORD&event=updatePassword"



# The global password
GLOBAL_PASSWORD = 'ThisIsAgootTroll121'


# Payloas
CHANGE_PAYLOAD = 'payloads/change'


URLS = {
    'CALENDAR': 'http://unipaz.uxxi.com/portal/page/portal/uxxiportal/academico/horario',
    'CHANGE_PASSWORD': 'http://unipazsso.uxxi.com/oiddas/ui/oracle/ldap/das/mypage/AppChgPwdMyPage?doneURL=http://unipaz.uxxi.com/portal/page/portal/uxxiportal/inicio',
    'GET_CHANGE_TOKEN': 'http://unipazsso.uxxi.com/oiddas/ui/oracle/ldap/das/mypage/AppChgPwdMyPage?doneURL=http://unipaz.uxxi.com/portal/page/portal/uxxiportal/inicio',
    'STUDENT_INFO': 'http://unipaz.uxxi.com/portal/page/portal/uxxiportal/academico/datos',
    'AUTH': 'http://unipazsso.uxxi.com/pls/orasso/orasso.wwsso_app_admin.ls_login'
}

# Data
VULNERABLE_DIR = 'data/vulnerable'
#VULNERABLE_DIR = 'payloads/list'
PAYLOADS_DIR = 'data/payloads'
DATASET_DIR = 'data/dataset'



# STORAGE
REDIS_HOST = 'localhost'
REDIS_PORT = 6379


JWT_SECRET_KEY = "ss"