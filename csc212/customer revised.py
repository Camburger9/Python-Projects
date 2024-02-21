class Customer:

    def __init__(self, name, aTime, tTime):
        self.__name = name
        self.__arivalTime = aTime
        self.__taskTime = tTime

    def __str__(self):
        return f'Next in line is: {self.__name}, Time of arival: {self.__arivalTime}, Time till task complete: {self.__taskTime}'
