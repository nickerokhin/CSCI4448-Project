import abc

class Invoker:

    def __init__(self):
        self.__commands = []
    
    def store_command(self, command):
        self.__commands.append(command)

    def execute_commands(self):
        for command in self.__commands:
            command.execute()

class Command(metaclass = abc.ABCMeta):
    def __init__(self, receiver):
        self.__receiver = receiver
    
    @abc.abstractmethod
    def execute(self):
        pass

class Search(Command):

    def __init__(self, )
    def 