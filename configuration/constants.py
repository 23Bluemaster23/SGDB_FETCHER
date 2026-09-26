CONFIG_LOCATION:str = "./setting.cfg"
DB_LOCATION:str = "./games.db"
API_HEADER:dict = {
    "Authorization": 'Bearer {token}'
}

class IMAGE_TYPE:
    COVERTART:int = 0
    BANNER:int = 1
    ICON:int = 2
