def calculate_ytm(face_value, coupon_rate, years_to_maturity, price, payment_frequency=1, tolerance=1e-6, max_iterations=100):
    """
    채권의 만기수익률(YTM)을 계산하는 함수.
    :param face_value: 액면가
    :param coupon_rate: 쿠폰 이자율
    :param years_to_maturity: 만기까지 남은 기간 (년)
    :param price: 현재 채권 가격
    :param payment_frequency: 연간 이자 지급 횟수
    :param tolerance: 계산의 오차 허용 범위
    :param max_iterations: 최대 반복 횟수
    :return: YTM (만기 수익률)
    """
    coupon_payment = (coupon_rate / payment_frequency) * face_value
    total_periods = years_to_maturity * payment_frequency
    ytm_guess = coupon_rate  # 초기 추정값을 쿠폰 이자율로 설정
    iteration = 0

    while iteration < max_iterations:
        iteration += 1
        bond_value = 0
        bond_derivative = 0

        for period in range(1, total_periods + 1):
            bond_value += coupon_payment / (1 + ytm_guess / payment_frequency) ** period
            bond_derivative += (-period * coupon_payment) / (1 + ytm_guess / payment_frequency) ** (period + 1)

        bond_value += face_value / (1 + ytm_guess / payment_frequency) ** total_periods
        bond_derivative += (-total_periods * face_value) / (1 + ytm_guess / payment_frequency) ** (total_periods + 1)

        # 분모가 0에 가까워지면 예외 처리
        if abs(bond_derivative) < tolerance:
            raise ValueError("Derivative is too small; convergence issue likely.")

        ytm_new = ytm_guess - (bond_value - price) / bond_derivative

        # 수렴 확인
        if abs(ytm_new - ytm_guess) < tolerance:
            return ytm_new * payment_frequency

        ytm_guess = ytm_new

    # 최대 반복 횟수 초과 시 None 대신 오류 반환
    raise ValueError("Failed to converge after maximum iterations")
