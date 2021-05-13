from typing import List


class ActionType:
    READ   = 'read'
    WRITE  = 'write'
    DELETE = 'delete'
    UPDATE = 'update'

class Resources:
    def __init__(self, name) -> None:
        self.name = name




class Policy:
    def __init__(self, name, actions: List[ActionType], resources: List[Resources]) -> None:
        self.name = name
        self.actions = actions
        self.resources = resources



class Role:
    def __init__(self, type: str, policy: Policy) -> None:
        self.type = type
        self.policy = policy



class User:
    def __init__(self, name: str, role: Role = None) -> None:
        self.name = name
        self.role = role


if __name__ == "__main__":
    print("Follow the steps to craete a request based access control: 1. Create a resource 2. Create a policy 3. Create a role 4. Create a user")
    check = False
    resources = []
    while check==False:
        resource_input = input("Enter the resource name \n")
        r = Resources(resource_input)
        resources.append(r)
        
        check_input = input("Do u want add another resource press 1 for yes else enter anything else \n")
        if check_input != 1:
            check = True
    check_resources = [val.name for val in resources]
    
    check = False
    policies = {}
    while check==False:
        policy_input = input("Enter the policy name \n")
        actions = input("Enter the actions' access you want to give to this policy as space separated input <1 for READ, 2 for WRITE, 3 DELETE, 4 for UPDATE> \n")
        actions = actions.split(' ')
        all_actions = []
        for action in actions:
            if action=='READ':
                all_actions.append(ActionType.READ)
            elif action=='WRITE':
                all_actions.append(ActionType.WRITE)
            elif action=='UPDATE':
                all_actions.append(ActionType.UPDATE)
            elif action=='DELETE':
                all_actions.append(ActionType.DELETE)

        policy_resources = input("Enter the resources' you want to give access to this policy as space separated input from the available list given --> <e.g. if r1 and r2 is there and you want assign to the user then enter r1 r2> \n")
        policy_resources = policy_resources.split(' ')
        all_resources = []
        
        new_policy = Policy(
            name = policy_input,
            actions = all_actions,
            resources = policy_resources
        )
        policies[policy_input] = new_policy
        print(new_policy.__dict__)
        check_input = input("Do u want add another policy then press 1 for yes else enter anything else")
        if check_input != 1:
            check = True
        
        available_roles = {}
        role = input("Enter the role name you want to add \n")
        policy_choice = input("Enter the policy you want to add for this role \n")
        if policy_choice in policies and 'WRITE' in policies[policy_choice].actions:
            new_role = Role(role, policy=policies[policy_choice])
            available_roles[role] = new_role
        else:
            print("There is no access to add role for this user's policy")
        
        all_users = {}
        username = input("Enter the username you want to add \n")
        role_choice = input('Enter the role you want to give to this user \n')
        if role_choice in available_roles:
            new_user = User(username, role=role)
            all_users[username] = new_user
        import pdb; pdb.set_trace()
