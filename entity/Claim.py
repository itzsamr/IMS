class Claim:
    def __init__(
        self, claimId, claimNumber, dateFiled, claimAmount, status, policy, client
    ):
        self.__claimId = claimId
        self.__claimNumber = claimNumber
        self.__dateFiled = dateFiled
        self.__claimAmount = claimAmount
        self.__status = status
        self.__policy = policy
        self.__client = client

    def getClaimId(self):
        return self.__claimId

    def getClaimNumber(self):
        return self.__claimNumber

    def getDateFiled(self):
        return self.__dateFiled

    def getClaimAmount(self):
        return self.__claimAmount

    def getStatus(self):
        return self.__status

    def getPolicy(self):
        return self.__policy

    def getClient(self):
        return self.__client

    def __str__(self):
        return f"Claim [claimId={self.__claimId}, claimNumber={self.__claimNumber}, dateFiled={self.__dateFiled}, claimAmount={self.__claimAmount}, status={self.__status}, policy={self.__policy}, client={self.__client}]"
