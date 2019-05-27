from statsmodels.stats.proportion import proportion_confint

# Wilson score interval을 이용하여 95% 신뢰구간을 구한다.
a_lower, a_upper = proportion_confint(sum(a), len(a), alpha=0.05, method='wilson')
b_lower, b_upper = proportion_confint(sum(b), len(b), alpha=0.05, method='wilson')

plt.plot(1, np.mean(a), 'ro')
plt.plot(2, np.mean(b), 'bo')
plt.plot([1, 1], [a_lower, a_upper], 'r-')
plt.ylib(0.448, 0.454)
plt.xlim(0, 3)
plt.xticks([1, 2], ['A', 'B'], fontsize=20)
plt.xlabel('표본')
plt.ylabel('모평균')
