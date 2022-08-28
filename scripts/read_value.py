from brownie import accounts, config, code2, network


def read_contract():
    code_2 = code2[-1]
    print(code_2.get_n1())


def main():
    read_contract()
