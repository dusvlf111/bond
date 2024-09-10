# 듀레이션(Duration)

def calculate_bond_duration(face_value, coupon_rate, years_to_maturity, ytm, payment_frequency=1):
    """
    채권의 듀레이션을 계산하는 함수.
    """
    coupon_payment = (coupon_rate / payment_frequency) * face_value
    total_periods = years_to_maturity * payment_frequency

    bond_duration = 0
    bond_value = 0

    for period in range(1, total_periods + 1):
        cash_flow_pv = coupon_payment / (1 + ytm / payment_frequency) ** period
        bond_value += cash_flow_pv
        bond_duration += period * cash_flow_pv

    face_value_pv = face_value / (1 + ytm / payment_frequency) ** total_periods
    bond_value += face_value_pv
    bond_duration += total_periods * face_value_pv

    mac_duration = bond_duration / bond_value
    mod_duration = mac_duration / (1 + ytm / payment_frequency)

    return mac_duration, mod_duration