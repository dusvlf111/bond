from BondPkg.Bond_information import Bond 


# 채권 정보 입력
bond = Bond(
    face_value=1000,
    coupon_rate=0.05,
    years_to_maturity=10,
    price=950,
    payment_frequency=2
    )


# YTM 계산
ytm_value = bond.ytm()
print(f"YTM: {ytm_value:.4f}")

# 듀레이션 계산
mac_duration, mod_duration = bond.duration()
print(f"맥컬레이 듀레이션: {mac_duration:.4f}")
print(f"수정 듀레이션: {mod_duration:.4f}")

# 콘벡서티 계산
convexity_value = bond.convexity()
print(f"콘벡서티: {convexity_value:.4f}")

# 현재 수익률 계산
current_yield_value = bond.current_yield()
print(f"현재 수익률: {current_yield_value:.4f}")

# 채권 가격 계산 (할인율 4%)
bond_price = bond.current_price(discount_rate=0.04)
print(f"채권 가격: {bond_price:.2f}")

# 스프레드 계산 (벤치마크 금리 3%)
spread_value = bond.spread(benchmark_rate=0.03)
print(f"스프레드: {spread_value:.4f}")
