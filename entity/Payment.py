class Payment:
    def __init__(self, paymentId, paymentDate, paymentAmount, client):
        self.__paymentId = paymentId
        self.__paymentDate = paymentDate
        self.__paymentAmount = paymentAmount
        self.__client = client

    def getPaymentId(self):
        return self.__paymentId

    def getPaymentDate(self):
        return self.__paymentDate

    def getPaymentAmount(self):
        return self.__paymentAmount

    def getClient(self):
        return self.__client

    def __str__(self):
        return f"Payment [paymentId={self.__paymentId}, paymentDate={self.__paymentDate}, paymentAmount={self.__paymentAmount}, client={self.__client}]"
