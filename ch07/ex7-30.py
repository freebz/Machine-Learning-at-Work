rmse_test = []

# 특징 조합별 성능을 측정한다.
for column in candidate_columns:
    # 누락값을 제거한다.
    filtered_lens = lens[column].dropna()
    # 입력 데이터를 더미 변수로 변환한다.
    v = DictVectorizer()
    X_more_feature = v.fit_transform(
        list(filtered_lens.drop('rating', axis=1).T.to_dict().values()))
    # 정답에 해당하는 실제 평점
    y_more_feature = filtered_lens['rating'].tolist()

    # 정답 데이터를 훈련 데이터와 테스트 데이터로 분할한다.
    X_mf_train, X_mf_test, y_mf_train, y_mf_test = train_test_split(
        X_more_feature, y_more_feature, test_size=0.1, random_state=42)

    # rating을 표준화한다.
    scaler = StandardScaler()
    y_mf_train_norm = scaler.fit_transform(np.array(y_mf_train)).ravel()

    # MCMC 알고리즘으로 모델을 학습힌다.
    fm = mcmc.FMRegression(n_iter=500, rank=8, random_state=123)
    fm.fit_predict(X_mf_train, y_mf_train_norm, X_mf_test)

    # 테스트 데이터의 예측 결과로부터 RMSE를 계산한다.
    y_pred = fm.fit_predict(X_mf_train, y_mf_train_norm, X_mf_test)
    rmse = np.sqrt(
        mean_squared_error(scaler.inverse_transform(y_pred), y_mf_test))
    rmse_test.append(rmse)

# RMSE를 그려본다.
ind = np.arange(len(rmse_test)
bar = plt.bar(ind, height=rmse_test)
plt.xticks(ind, ('A', 'B', 'C', 'D', 'E'))
plt.ylim((0.88, 0.90))
