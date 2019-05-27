from fastFM import als
import numpy as np

# 앞서 만든 더미 데이터의 사용자 중 19세인 사용자는 5점, 33세인 사용자는 1점,
# 55세 사용자는 2점, 20세 사용자는 4점을 부여했다고 하자.

y = np.array([5.0, 1.0, 2.0, 4.0])
# ALS로 FM 회귀 모델을 초기화한 뒤, 학습을 수행한다.
fm = als.FMRegression(n_iter=1000, init_stdev=0.1, rank=2,
                      l2_reg_w=0.1, l2_reg_V=0.5)
fm_fit(X, y)
# 나이가 24세인 사용자 ID 5가 아이템 10에 대해 내렸을 평점 rate를 예측한다.
fm.predict(v.transform({"user": "5", "item": "10", "age": 24}))
# array([ 3.60775939])
