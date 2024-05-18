class User:
    def __init__(self, userId, username, password, role):
        self.__userId = userId
        self.__username = username
        self.__password = password
        self.__role = role

    def getUserId(self):
        return self.__userId

    def getUsername(self):
        return self.__username

    def getPassword(self):
        return self.__password

    def getRole(self):
        return self.__role

    def __str__(self):
        return f"User [userId={self.__userId}, username={self.__username}, role={self.__role}]"
