from configparser import ConfigParser


def readConfig(section, key):
    config = ConfigParser()
    config.read('C://Users//admin//PycharmProjects//Inlynk_Appium//ConfigurationData//conf.ini')
    return config.get(section, key)
