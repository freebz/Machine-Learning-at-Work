mu = 0.5 # 앞면이 나올 확률 50%
init_sample = list(scipy.stats.bernoulli.rvs(mu, size=20))

sample = init_sample
p_value_history = []
for i in range(200):
    # 최근 20회 시행의 결과를 사용하여 검정
    _, p_value = scipy.stats.ttest_1samp(sample[-20:], 0.5)
    p_value_history.append(p_value)
    # 동전을 다시 던진 다음 결과 저장
    sample.append(scipy.stats.bernoulli.rvs(mu))

plt.figure(figsize=(10, 4))
plt.plot(p_value_history)
plt.xlabel('테스트 에포크')
plt.ylabel('p-값')
