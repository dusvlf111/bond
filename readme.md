아래는 `my_bond_package`에 대한 `README.md` 파일의 예시입니다. 패키지의 설명, 설치 방법, 사용 방법 등을 포함하고 있습니다.

```markdown
# My Bond Package

`my_bond_package`는 채권의 가격, 만기수익률(Yield to Maturity, YTM), 듀레이션, 콘벡서티 등을 계산할 수 있는 파이썬 패키지입니다. 금융 분석에서 채권의 주요 지표들을 계산하는 데 유용합니다.

## 기능

- **채권 가격 계산**: 할인율에 따른 채권의 현재 가치를 계산합니다.
- **만기수익률(YTM) 계산**: 주어진 채권의 만기수익률을 계산합니다.
- **듀레이션 계산**: 맥컬레이 듀레이션과 수정 듀레이션을 제공합니다.
- **콘벡서티 계산**: 채권의 콘벡서티(Convexity)를 계산합니다.
- **현재 수익률 계산**: 채권의 현재 수익률(Current Yield)을 계산합니다.
- **스프레드 계산**: 채권 수익률과 벤치마크 금리 간의 스프레드를 계산합니다.

## 설치

```bash
pip install my_bond_package
```

## 사용법

```python
from my_bond_package.bond import Bond

# 채권 정보 입력
bond = Bond(face_value=1000, coupon_rate=0.05, years_to_maturity=10, price=950, payment_frequency=2)

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
bond_price = bond.price(discount_rate=0.04)
print(f"채권 가격: {bond_price:.2f}")

# 스프레드 계산 (벤치마크 금리 3%)
spread_value = bond.spread(benchmark_rate=0.03)
print(f"스프레드: {spread_value:.4f}")
```

## 예제

- **YTM 계산**: 위의 예제에서 채권의 YTM을 계산할 수 있습니다. 예시에서는 쿠폰 이자율 5%, 만기 10년, 현재 가격 950인 채권의 YTM을 계산합니다.
  
- **듀레이션 계산**: 채권의 맥컬레이 듀레이션과 수정 듀레이션을 구할 수 있습니다.
  
- **콘벡서티 계산**: 채권 가격 민감도를 측정하는 콘벡서티 값을 제공합니다.

## 기여

기여를 원하시는 분들은 PR(Pull Request)를 통해 코드를 제출해 주시거나, 이슈(issues)를 남겨주세요. 

## 라이선스

이 프로젝트는 MIT 라이선스를 따릅니다. 자세한 내용은 [LICENSE](./LICENSE)를 참조하세요.
```

