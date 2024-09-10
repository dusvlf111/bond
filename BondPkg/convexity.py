#콘벡서티(Convexity)

# convexity.py

def calculate_convexity(face_value, coupon_rate, years_to_maturity, ytm, payment_frequency=1):
    """
    채권의 콘벡서티를 계산하는 함수.
    """
    coupon_payment = (coupon_rate / payment_frequency) * face_value
    total_periods = years_to_maturity * payment_frequency

    convexity:float = 0
    bond_value = 0

    for period in range(1, total_periods + 1):
        cash_flow_pv = coupon_payment / (1 + ytm / payment_frequency) ** period
        bond_value += cash_flow_pv
        convexity += period * (period + 1) * cash_flow_pv

    face_value_pv = face_value / (1 + ytm / payment_frequency) ** total_periods
    bond_value += face_value_pv
    convexity += total_periods * (total_periods + 1) * face_value_pv

    convexity = convexity / (bond_value * (1 + ytm / payment_frequency) ** 2)

    return convexity
