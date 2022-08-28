from brownie import accounts, config, code2, network
import os


def get_account():
    if network.show_active() == "development":
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])


def deploy_code2():
    account = get_account()
    # account = accounts.add(getenv("PRIVATE_KEY"))
    # account = accounts.add(config["wallets"]["from_key"])
    print("DEPLOYING CONTRACT")
    code_2 = code2.deploy({"from": account})
    intial_value = code_2.get_n1()
    print("Intial Value : " + str(intial_value))
    print("UPDATING 'n1'...")
    transaction = code_2.set_n1(36, {"from": account})
    transaction.wait(1)
    updated_value = code_2.get_n1()
    print("Updated Value : " + str(updated_value))
    p = code_2.person1()
    print(p)


def main():
    deploy_code2()
