from matplotlib import pyplot as plt
plt.style.use('ggplot')

# user_id별 평가 횟수의 히스토그램
lens.groupby('user_id').size().sort_values(ascending=False).hist()

plt.xlabel('(영화별) 평점 개수')
plt.ylabel('(사용자별) 평가 횟수')
