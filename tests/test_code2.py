from brownie import accounts, code2

# Arrange
# act
# assert


def test_deploy():
    account = accounts[0]
    code_2 = code2.deploy({"from": account})
    intial_value = code_2.get_n1()
    expected = 0
    assert intial_value == expected


def test_update():
    account = accounts[0]
    code_2 = code2.deploy({"from": account})
    expected = 89
    transaction = code_2.set_n1(expected, {"from": account})
    transaction.wait(1)
    assert code_2.get_n1() == expected
