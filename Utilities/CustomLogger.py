import logging

class Loggen:
    @staticmethod
    def loggen():
        logging.basicConfig(filename=".\\Logs\\automation.log",
                            format='%(asctime)s: %(levelname)s: %(message)s', datefmt='%m/%y/%d %I:%M:%S %p',
                            force=True)

        logger = logging.getLogger()
        logger.setLevel(logging.INFO)

