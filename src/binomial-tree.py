import math
class BinomialTree():
    def __init__(self, initial_price : float, strike : float , risk_free_rate : float, time_period: float, up_prob : float , down_prob : float):
        self.strike = strike 
        self.rate = risk_free_rate
        self.up = up_prob
        self.down = down_prob
        self.time = time_period
        self.initial = initial_price  

        

    def calculate(self):
        risk_neutral_up = (math.e ** (self.rate * self.time) - self.down)/(self.up - self.down)
        risk_neutral_down = 1 - risk_neutral_up
        up_payoff = max(0,(self.initial * self.up) - self.strike)
        down_payoff = max(0, (self.initial * self.down) - self.strike)
        price = math.e ** (-self.rate * self.time) * (risk_neutral_up * up_payoff + risk_neutral_down * down_payoff)
        print(price)


tree = BinomialTree(114 , 114, 0,0,204/114,84/114)
tree.calculate()