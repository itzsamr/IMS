class Client:
    def __init__(self, clientId, clientName, contactInfo, policy):
        self.__clientId = clientId
        self.__clientName = clientName
        self.__contactInfo = contactInfo
        self.__policy = policy

    def getClientId(self):
        return self.__clientId

    def getClientName(self):
        return self.__clientName

    def getContactInfo(self):
        return self.__contactInfo

    def getPolicy(self):
        return self.__policy

    def __str__(self):
        return f"Client [clientId={self.__clientId}, clientName={self.__clientName}, contactInfo={self.__contactInfo}, policy={self.__policy}]"
