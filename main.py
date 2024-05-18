from dao.InsuranceServiceImpl import InsuranceServiceImpl
from entity.Policy import Policy


class MainModule:
    def __init__(self):
        self.insurance_service = InsuranceServiceImpl()

    def display_menu(self):
        print("\nInsurance Management System Menu:")
        print("1. Create Policy")
        print("2. Get Policy")
        print("3. Get All Policies")
        print("4. Update Policy")
        print("5. Delete Policy")
        print("6. Exit")

    def run(self):
        while True:
            self.display_menu()
            choice = input("Enter your choice: ")

            if choice == "1":
                self.create_policy()
            elif choice == "2":
                self.get_policy()
            elif choice == "3":
                self.get_all_policies()
            elif choice == "4":
                self.update_policy()
            elif choice == "5":
                self.delete_policy()
            elif choice == "6":
                print("Exiting the program.")
                break
            else:
                print("Invalid choice. Please enter a valid option.")

    def create_policy(self):
        policy_id = int(input("Enter policy ID: "))
        policy_name = input("Enter policy name: ")
        start_date = input("Enter start date (YYYY-MM-DD): ")
        end_date = input("Enter end date (YYYY-MM-DD): ")

        policy = Policy(policy_id, policy_name, start_date, end_date)
        success = self.insurance_service.createPolicy(policy)
        if success:
            print("Policy created successfully.")
        else:
            print("Failed to create policy.")

    def get_policy(self):
        policy_id = int(input("Enter policy ID to retrieve: "))
        try:
            policy = self.insurance_service.getPolicy(policy_id)
            print(
                f"Policy ID: {policy.getPolicyId()}, Policy Name: {policy.getPolicyName()}, Start Date: {policy.getStartDate()}, End Date: {policy.getEndDate()}"
            )
        except Exception as e:
            print(e)

    def get_all_policies(self):
        policies = self.insurance_service.getAllPolicies()
        print("All Policies:")
        for policy in policies:
            print(
                f"Policy ID: {policy.getPolicyId()}, Policy Name: {policy.getPolicyName()}, Start Date: {policy.getStartDate()}, End Date: {policy.getEndDate()}"
            )

    def update_policy(self):
        policy_id = int(input("Enter policy ID to update: "))
        policy_name = input("Enter updated policy name: ")
        start_date = input("Enter updated start date (YYYY-MM-DD): ")
        end_date = input("Enter updated end date (YYYY-MM-DD): ")

        policy = Policy(policy_id, policy_name, start_date, end_date)
        success = self.insurance_service.updatePolicy(policy)
        if success:
            print("Policy updated successfully.")
        else:
            print("Failed to update policy.")

    def delete_policy(self):
        policy_id = int(input("Enter policy ID to delete: "))
        success = self.insurance_service.deletePolicy(policy_id)
        if success:
            print("Policy deleted successfully.")
        else:
            print("Failed to delete policy.")


if __name__ == "__main__":
    main_module = MainModule()
    main_module.run()
