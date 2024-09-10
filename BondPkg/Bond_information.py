# bond.py
from BondPkg.current_yield import calculate_bond_price
from BondPkg.ytm import calculate_ytm
from BondPkg.yield_calculator import calculate_current_yield
from BondPkg.duration import calculate_bond_duration
from BondPkg.convexity import calculate_convexity
from BondPkg.spread import calculate_yield_spread

class Bond:
    def __init__(self, face_value:float, coupon_rate:float, years_to_maturity:int, price:int, payment_frequency=1):
        """
        채권 정보 클래스
        """
        self.face_value = face_value
        self.coupon_rate = coupon_rate
        self.years_to_maturity = years_to_maturity
        self.price = price
        self.payment_frequency = payment_frequency

    def ytm(self):
        return calculate_ytm(
            self.face_value,
            self.coupon_rate,
            self.years_to_maturity,
            self.price,
            self.payment_frequency
            )

    def duration(self):
        return calculate_bond_duration(
            self.face_value,
            self.coupon_rate,
            self.years_to_maturity,
            self.price,
            self.payment_frequency
            )

    def convexity(self):
        ytm_value = self.ytm()
        return calculate_convexity(
            self.face_value,
            self.coupon_rate,
            self.years_to_maturity,
            ytm_value,
            self.payment_frequency
            )
    

    def current_price(self, discount_rate:float):
        return calculate_bond_price(
            self.face_value,
            self.coupon_rate,
            self.years_to_maturity,
            discount_rate,
            self.payment_frequency
        )

    def current_yield(self):
        return calculate_current_yield(
            self.coupon_rate,
            self.price
        )


    def spread(self, benchmark_rate:float):
        ytm_value = self.ytm()
        return calculate_yield_spread(ytm_value, benchmark_rate)
