import argparse


class CliParser:
    parser = None
    defaultEnvironment = 'develop'

    def __init__(self):
        self.parser = argparse.ArgumentParser(description='Python REST Api')
        self.parser.add_argument('--env', type=str, help='Environment for which the app will run (develop/production', default=self.defaultEnvironment)

    def getArgs(self, argv=None):
        return self.parser.parse_args(argv)

    def getEnvironment(self):
        try:
            return self.getArgs().env
        except:
            return None


cliParser = CliParser()
