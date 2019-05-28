max_sample = 3000000
# 표본 A의 평균 : 45.1%
a = scipy.stats.bernoulli.rvs(0.451, size=max_sample)
# 표본 B의 평균 : 45.2%
b = scipy.stats.bernoulli.rvs(0.452, size=max_sample)
p_values = []
# 표본 크기를 5,000씩 늘려가며 검정을 수행한다.
sample_sizes = np.arange(1000, max_sample, 5000)
for sample_size in sample_sizes:
    _, p_value = scipy.stats.ttest_ind(a[:sample_size], b[:sample_size], equal_var=False)
    p_values.append(p_value)

plt.figure(figsize=(10, 3))
plt.plot(sample_sizes, p_values)
plt.xlabel('표본 크기')
plt.ylabel('p-값')
