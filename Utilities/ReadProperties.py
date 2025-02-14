import configparser

config = configparser.RawConfigParser()
config.read(".\\Configuration\\config.ini")

class ReadConfig:

    @staticmethod
    def get_url():
        url = config.get('common info', 'base_url')
        return url
    @staticmethod
    def get_username():
        user_name  = config.get('common info', 'user_name')
        return user_name

    @staticmethod
    def get_password():
        password = config.get('common info', 'password')
        return password

    @staticmethod
    def get_home_page_title():
        home_page_title = config.get('common info', 'home_page_title')
        return home_page_title

    @staticmethod
    def get_login_page_title():
        login_page_title = config.get('common info', 'login_page_title')
        return login_page_title

    @staticmethod
    def get_full_name():
        full_name = config.get('common info', 'full_name')
        return full_name

