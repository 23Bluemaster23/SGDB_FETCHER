from configparser import ConfigParser

from configuration.constants import CONFIG_LOCATION

config = ConfigParser()
def get_config(section:str,option:str):
    config.read(CONFIG_LOCATION)
    return config[section][option]

# if __name__ == '__main__':
#     print(get_config('API','key'))
