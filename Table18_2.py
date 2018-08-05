# The following code copies Table 18.2 in Options, Futures and Other Derivatives (8th)
# We can combine the below two functions into one function. 

import numpy as np
import pandas as pd

stock_prices = [49., 48.12, 47.37, 50.25, 51.75, 53.12, 53., 51.87, 51.38,
                53., 49.88, 48.5, 49.88, 50.37, 52.13, 51.88, 52.87, 54.87,
                54.62, 55.87, 57.25]

delta = [0.522, 0.458, 0.400, 0.596, 0.693, 0.774, 0.771, 0.706, 0.674, 0.787,
         0.550, 0.413, 0.542, 0.591, 0.768, 0.759, 0.865, 0.978, 0.990, 1., 1.]

rate = 0.05

frequence = 52  # week.


def shares_purchased(stock_prices, delta, nums=100000):
    # stock_prices, delta: list
    # nums: int

    # return: np.array

    shares_in_hands = [x * nums for x in delta]

    tmp = [0]
    tmp.extend(shares_in_hands[:-1])

    return1 = np.array(shares_in_hands) - np.array(tmp)

    return2 = np.array([x * y for x, y in zip(stock_prices, return1)])

    return return1, return2


shares_purchased, cost_shares_purchased = shares_purchased(stock_prices, delta)


def cul_cost_Interest(cost_shares_purchased, rate, frequence):
    # cost_share_purchased: np.array
    # rate: float

    # return: np.array

    return1 = []
    return2 = []

    for i in range(len(cost_shares_purchased)):

        if i == 0:
            return1.append(cost_shares_purchased[i])
        else:
            return1.append(sum(cost_shares_purchased[:i]) + cost_shares_purchased[i] + sum(return2[:i]))

        return2.append(return1[i] * rate / frequence)

    return return1, return2


cul_cost, interest_cost = cul_cost_Interest(cost_shares_purchased, rate, frequence)

Table18_2 = np.vstack(
    (np.array(stock_prices), np.array(delta), shares_purchased, cost_shares_purchased, cul_cost, interest_cost))

Table18_2 = pd.DataFrame(np.transpose(Table18_2))

Table18_2.columns = ['Stock price', 'Delta', 'Shares purchased', 'Cost of shares purchased',
                     'Culumlative cost including interest', 'Interest cost']

Table18_2.iloc[-1, -1] = np.nan


print Table18_2