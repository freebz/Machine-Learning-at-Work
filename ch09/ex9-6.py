import pandas as pd
import matplotlib.pyplot as plt
from operator import itemgetter
plt.style.use('ggplot')
%matplotlib inline

# 점수가 높은 순으로 정렬
result = list(
    zip(test_is_cv_list, test_is_treat_list, score_list))
result.sort(key=itemgetter(2), reverse=True)

qdf = pd.DataFrame(columns=('treat_cvr', 'control_cvr'))

for n in range(10):
    # 결과를 10% 단위로 나눈다.
    start = int(n * len(result) / 10)
    end = int((n + 1) * len(result) / 10) - 1
    quantiled_result = result[start:end]

    # 실험군과 대조군에서 결과 집계
    treat_uu = list(
        map(lambda item: item[1], quantiled_result)
    ).count(True)
    control_uu = list(
        map(lambda item: item[1], quantiled_result)
    ).count(False)

    # 실험군과 대조군에서 전환 건수 집계
    treat_cv = [item[0] for item in quantiled_result
                if item[1] is True].count(True)
    control_cv = [item[0] for item in quantiled_result
                  if item[1] is False].count(True)

    # 전환 건수로부터 전환율을 계산하여 DataFrame에 저장
    treat_cvr = treat_cv / treat_uu
    control_cvr = control_cv / control_uu

    label = "{}%-{}%".format(n % 10, (n + 1) * 10)
    qdf.loc[label] = [treat_cvr, control_cvr]

qdf.plot.bar()
plt.xlabel("업리프트 점수 백분위수")
plt.ylabel("전환율")
