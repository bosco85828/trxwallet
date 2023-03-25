from tronpy.providers import HTTPProvider
from tronpy import Tron,Contract
from pprint import pprint

# 創建TRON對象
global tron
# tron = Tron(HTTPProvider(api_key="eaa4855b-5b24-45c2-b31c-ec9693a6d0c2"))
tron=Tron()
contract = "TR7NHqjeKQxGTCi8q8ZY4pL8otSzgjLj6t" # USDT 
cntr=tron.get_contract(contract)
global precision
precision = cntr.functions.decimals()
# print(precision)

def create_account():
    data=tron.generate_address()
    return data


def get_balance(address):
    symbol=cntr.functions.symbol()
    balance= cntr.functions.balanceOf(address) / 10 ** precision #換算 USDT 單位 (原單位為 wei )
    return symbol,balance

if __name__ == "__main__":
    print('=== 創建 trx 地址 ==')
    pprint(create_account())
    print('')

    print('=== 查詢 TJh5zGuMA4jLeAZNbAFFQ4t2EkacYZgxa1 此地址 USDT 餘額 ===')
    pprint(get_balance('TJh5zGuMA4jLeaZNceFFQqq2EkacYZgxa1'))
    print('')


    # print('Symbol:', cntr.functions.symbol())  # The symbol string of the contract
    # print('Balance:', cntr.functions.balanceOf(address) / 10 ** precision)

# data=tron.generate_address()
# pprint(tron.trc20_get_balance(contract=contract, address='TTdbpnTLYzHq11Pgpxh12eYjyS6SnD2sE9'))

# pprint(tron.get_account_balance("TTdbpnTLYzHq11Pgpxh12eYjyS6SnD2sE9"))
# pprint(tron.get_account_asset_balances("TTdbpnTLYzHq11Pgpxh12eYjyS6SnD2sE9"))