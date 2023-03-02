# Написать простой кошелек с возможностью пополнения и списания средств

class Purse:
    
    money_usd = 0
    money_euro = 0
    
    def __init__(self, money_usd, money_euro):
        self.money_usd = money_usd
        self.money_euro = money_euro
        
    def put_money(self, usd_put):
        self.money_usd = self.money_usd + usd_put
        return self.money_usd
    
    def take_money(self, usd_take):
        self.money_usd = self.money_usd - usd_take
        return self.money_usd
    
    def balance_usd(self):
        print(self.money_usd)
    
    
usd = Purse(0, 0)
usd.put_money(100)
usd.take_money(10)
usd.balance_usd()


        