import configparser

config = configparser.RawConfigParser()
config.read(".\\Configuration\\config.ini")

class ReadConfig:
    @staticmethod
    def get_url():
        url = config.get("common info", 'url')
        return url

    @staticmethod
    def get_email():
        email= config.get("common info", 'email')
        return email

    @staticmethod
    def get_password():
        password = config.get("common info", "password")
        return password

    @staticmethod
    def get_page_title():
        title = config.get("common info", "page_title")
        return title

    @staticmethod
    def get_headline():
        headline= config.get("common info", "headline")
        return headline