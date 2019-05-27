n_iter = 100
seed = 333

rmse_test = []
# rank가 4, 8, 16, 32, 64인 경우를 탐색한다.
ranks = [4, 8, 16, 32, 64]

# rank 값을 바꿔가며 학습 및 성능을 측정, dev test 데이터에 대한 RMSE를 구한다.
for rank in ranks:
    fm = mcmc.FMRegression(n_iter=n_iter, rank=rank, random_state=seed)
    y_pred = fm.fit_predict(X_train, y_train, X_dev_test)
    rmse = np.sqrt(mean_squared_error(y_pred, y_dev_test))
    rmse_test.append(rmse)
    print('rank:{}\trmse:{:.3f}'.format(rank, rmse))

# 각 rank 값에 대한 RMSE를 그려본다.
plt.plot(ranks, rmse_test, label='dev test rmse', color="r")
plt.legend()
