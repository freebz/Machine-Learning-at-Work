# 점수순으로 집계
treat_uu = 0
control_uu = 0
treat_cv = 0
control_cv = 0
treat_cvr = 0.0
control_cvr = 0.0
lift = 0.0

stat_data = []

for is_cv, is_treat, score in result:
    if is_treat:
        treat_uu += 1
        if is_cv:
            treat_cv += 1
        treat_cvr = treat_cv / treat_uu
    else:
        control_uu += 1
        if is_cv:
            control_cv += 1
        control_cvr = control_cv / control_uu

    # 두 그룹의 전환율 차이에서 실험군의 사람 수를 곱하는 방법으로 lift를 계산한다.
    # 비율(CVR)의 차이이므로 실험군과 대조군의 크기가 달라도 무방하다.
    lift = (treat_cvr - control_cvr) * treat_uu

    stat_data.append(
        [is_cv, is_treat, score, treat_uu, control_uu,
         treat_cv, control_cv, treat_cvr, control_cvr, lift])

# 통계 데이터를 DataFrame 객체로 변환
df = pd.DataFrame(stat_data)
df.columns = \
   ["is_cv", "is_treat", "score", "treat_uu",
    "control_uu", "treat_cv", "control_cv",
    "treat_cvr", "control_cvr", "lift"]

# 베이스라인 정보 추가
df["base_line"] = \
   df.index * df["lift"][len(df.index) - 1] / len(df.index)

# 시각화
df.plot(y=["treat_cv", "control_cv"])
plt.xlabel("업리프트 점수 순위")
plt.ylabel("전환 건수")

df.plot(y=["treat_cvr", "control_cvr"])
plt.xlabel("업리프트 점수 순위")
plt.ylabel("전환율")

df.plot(y=["lift", "base_line"])
plt.xlabel("업리프트 점수 순위")
plt.ylabel("전환 리프트")
