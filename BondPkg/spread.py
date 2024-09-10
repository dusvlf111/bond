# 수익률 스프레드(Yield Spread)
# spread.py


def calculate_yield_spread(risky_bond_yield, risk_free_bond_yield):
    """
    두 채권 간의 수익률 스프레드를 계산하는 함수.
    """
    return risky_bond_yield - risk_free_bond_yield
