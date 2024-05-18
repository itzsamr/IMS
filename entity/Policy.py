class Policy:
    def __init__(self, policyId, policyName, startDate, endDate):
        self.__policyId = policyId
        self.__policyName = policyName
        self.__startDate = startDate
        self.__endDate = endDate

    def getPolicyId(self):
        return self.__policyId

    def getPolicyName(self):
        return self.__policyName

    def getStartDate(self):
        return self.__startDate

    def getEndDate(self):
        return self.__endDate

    def setPolicyId(self, policyId):
        self.__policyId = policyId

    def setPolicyName(self, policyName):
        self.__policyName = policyName

    def setStartDate(self, startDate):
        self.__startDate = startDate

    def setEndDate(self, endDate):
        self.__endDate = endDate

    def __str__(self):
        return f"Policy [policyId={self.__policyId}, policyName={self.__policyName}, startDate={self.__startDate}, endDate={self.__endDate}]"
