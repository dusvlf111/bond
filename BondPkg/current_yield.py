# 현재 수익률(Current Yield)
# price.py

def calculate_bond_price(face_value:float, coupon_rate:float, years_to_maturity:int, discount_rate:float, payment_frequency=1):
    """
    채권의 현재가치를 계산하는 함수.
    """
    coupon_payment = (coupon_rate / payment_frequency) * face_value
    total_periods = years_to_maturity * payment_frequency
    bond_value = 0

    for period in range(1, total_periods + 1):
        bond_value += coupon_payment / (1 + discount_rate / payment_frequency) ** period

    bond_value += face_value / (1 + discount_rate / payment_frequency) ** total_periods

    return bond_value