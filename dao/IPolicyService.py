from abc import ABC, abstractmethod
from entity.Policy import Policy
from exception.PolicyNotFoundException import PolicyNotFoundException


class IPolicyService(ABC):
    @abstractmethod
    def createPolicy(self, policy: Policy) -> bool:
        pass

    @abstractmethod
    def getPolicy(self, policyId: int) -> Policy:
        pass

    @abstractmethod
    def getAllPolicies(self) -> list:
        pass

    @abstractmethod
    def updatePolicy(self, policy: Policy) -> bool:
        pass

    @abstractmethod
    def deletePolicy(self, policyId: int) -> bool:
        pass
