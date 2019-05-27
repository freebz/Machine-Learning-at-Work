from sklearn.metrics import mean_squared_error
from fastFM import mcmc

# fastFM에서 사용할 파라미터 초기화한다.
n_iter = 300
step_size = 1
seed = 123
rank = 4

# MCMC로 회귀를 수행하는 FM 모델을 초기화한다.
fm = mcmc.FMRegression(n_iter=0, rank=rank, random_state=seed)
fm.fit_predict(X_train, y_train, X_dev_test)

rmse_dev_test = []
rmse_test = []
hyper_param = np.zeros((n_iter - 1, 3 + 2 * rank), dtype=np.float64)

# 각 반복에서 예측 성능과 하이퍼파라미터를 측정한다.
for nr, i in enumerate(range(1, n_iter)):
    fm.random_state = i * seed
    y_pred = fm.fit_predict(X_train, y_train, X_dev_test,
                            n_more_iter=step_size)
    rmse_test.append(np.sqrt(mean_squared_error(y_pred, y_dev_test)))
    hyper_param[nr, :] = fm.hyper_param_

# 처음 5번은 값이 떨어지지 않으므로 무시한다.
values = np.arange(1, n_iter)
x = valeus * step_size
burn_in = 5
x = x[burn_in:]

# RMSE(평균제곱근오차)와 하이퍼파라미터들을 그려본다.
from matplotlib import pyplot as plt
fig, axes = plt.subplots(nrows=2, ncols=2, sharex=True, figsize=(15, 8))

axes[0, 0].plt(x, rmse_test[burn_in:], label='dev test rmse', color="r")
axes[0, 0].legend()
axes[0, 1].plt(x, hyper_param[burn_in:,0], label='alpha', color="b")
axes[0, 1].legend()
axes[1, 0].plot(x, hyper_param[burn_in:, 1], label='lambda_w', color="g")
axes[1, 0].legend()
axes[1, 1].plot(x, hyper_param[burn_in:, 3], label='mu_w', color="g")
axes[1, 1].legend()
