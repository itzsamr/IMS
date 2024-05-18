import pyodbc
from dao.IPolicyService import IPolicyService
from entity.Policy import Policy
from exception.PolicyNotFoundException import PolicyNotFoundException
from util.DBConnection import DBConnUtil


class InsuranceServiceImpl(IPolicyService):
    def createPolicy(self, policy: Policy) -> bool:
        try:
            connection = DBConnUtil.getConnection()
            cursor = connection.cursor()
            insert_query = "INSERT INTO Policies (policyId, policyName, startDate, endDate) VALUES (?, ?, ?, ?)"
            cursor.execute(
                insert_query,
                (
                    policy.getPolicyId(),
                    policy.getPolicyName(),
                    policy.getStartDate(),
                    policy.getEndDate(),
                ),
            )
            connection.commit()
            return True
        except Exception as e:
            print("Error creating policy:", e)
            return False
        finally:
            if connection:
                connection.close()

    def getPolicy(self, policyId: int) -> Policy:
        try:
            connection = DBConnUtil.getConnection()
            cursor = connection.cursor()
            select_query = "SELECT * FROM Policies WHERE policyId = ?"
            cursor.execute(select_query, (policyId,))
            row = cursor.fetchone()
            if row:
                policy = Policy(row[0], row[1], row[2], row[3])
                return policy
            else:
                raise PolicyNotFoundException("Policy not found")
        except Exception as e:
            raise PolicyNotFoundException("Policy not found") from e
        finally:
            if connection:
                connection.close()

    def getAllPolicies(self) -> list:
        try:
            connection = DBConnUtil.getConnection()
            cursor = connection.cursor()
            select_query = "SELECT * FROM Policies"
            cursor.execute(select_query)
            rows = cursor.fetchall()
            policies = []
            for row in rows:
                policy = Policy(row[0], row[1], row[2], row[3])
                policies.append(policy)
            return policies
        except Exception as e:
            print("Error retrieving policies:", e)
            return []
        finally:
            if connection:
                connection.close()

    def updatePolicy(self, policy: Policy) -> bool:
        try:
            connection = DBConnUtil.getConnection()
            cursor = connection.cursor()
            update_query = "UPDATE Policies SET policyName = ?, startDate = ?, endDate = ? WHERE policyId = ?"
            cursor.execute(
                update_query,
                (
                    policy.getPolicyName(),
                    policy.getStartDate(),
                    policy.getEndDate(),
                    policy.getPolicyId(),
                ),
            )
            connection.commit()
            return True
        except Exception as e:
            print("Error updating policy:", e)
            return False
        finally:
            if connection:
                connection.close()

    def deletePolicy(self, policyId: int) -> bool:
        try:
            connection = DBConnUtil.getConnection()
            cursor = connection.cursor()
            delete_clients_query = "DELETE FROM Clients WHERE policyId = ?"
            cursor.execute(delete_clients_query, (policyId,))
            connection.commit()
            delete_claims_query = "DELETE FROM Claims WHERE policyId = ?"
            cursor.execute(delete_claims_query, (policyId,))
            connection.commit()
            delete_payments_query = "DELETE FROM Payments WHERE clientId IN (SELECT clientId FROM Clients WHERE policyId = ?)"
            cursor.execute(delete_payments_query, (policyId,))
            connection.commit()
            delete_policy_query = "DELETE FROM Policies WHERE policyId = ?"
            cursor.execute(delete_policy_query, (policyId,))
            connection.commit()
            return True
        except Exception as e:
            print("Error deleting policy:", e)
            return False
        finally:
            if connection:
                connection.close()
