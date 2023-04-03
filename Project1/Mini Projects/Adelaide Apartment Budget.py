

f_fee = 13463
foreign_duty = 0.07
furniture_cost = 20000
conveyance = 1100


def stamp_duty(price):
    array = [500000, 300000, 250000, 200000, 100000, 50000, 12000, 0]
    base_duty = [21330, 11330, 8955, 6830, 2830, 1080, 480, 120, 0]
    rate = [0.055, 0.05, 0.0475, 0.0425, 0.04, 0.035, 0.03, 0.02, 0.01]
    total = 0
    for idx in range(len(array)):
        if price > array[idx]:
            total += base_duty[idx] + (price-array[idx])*rate[idx]
            break
    total = round(total,2)
    return total


def transfer_fee(price):
    trans_fee = 0.0087775
    total = price * trans_fee
    total = round(total,2)
    return total


def AUDtoUSD(i):
    usd = i / 1.4568
    return round(usd,2)


def AUDtoRMB(i):
    rmb = i * 4.6864
    return round(rmb,2)


if __name__ == '__main__':
    price = int(input('Enter the property price ($AUD) of the apartment: $'))
    stamp_duty_cost = stamp_duty(price)
    transfer_cost = transfer_fee(price)
    total_cost = price + f_fee + price*foreign_duty + furniture_cost + stamp_duty_cost + transfer_cost + conveyance
    print(f'Total Cost will be ${total_cost} AUD, or ${AUDtoUSD(total_cost)} USD or ￥{AUDtoRMB(total_cost)} RMB')
    print(f'Cost include:\n-Property Value: ${price}\n-Stamp Duty: ${stamp_duty(price)}\n'
          f'-Foreign Stamp Duty: ${round(price*foreign_duty,2)}\n-FIRB Application Fee: ${f_fee}\n-'
          f'Transfer Fee: ${transfer_fee(price)}\n-Furniture Cost: ${furniture_cost}\n-Conveyance Fee: ${conveyance}')
