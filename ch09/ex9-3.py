# 훈련 데이터 생성
sample_num = 100000
train_is_cv_list, train_is_treat_list, train_feature_vector_list = \
   generate_sample_data(sample_num, seed=1)

# 데이터를 실험군(treatment)과 대조군(control)으로 나눔
treat_is_cv_list = []
treat_feature_vector_list = []
control_is_cv_list = []
control_feature_vector_list = []

for i in range(sample_num):
    if train_is_treat_list[i]:
        treat_is_cv_list.append(train_is_cv_list[i])
        treat_feature_vector_list.append(
            train_feature_vector_list[i])
    else:
        control_is_cv_list.append(train_is_cv_list[i])
        control_feature_vector_list.append(
            train_feature_vector_list[i])

# 전환율 출력
print("treatment_cvr",
      treat_is_cv_list.count(True) / len(treat_is_cv_list))
print("control_cvr",
      control_is_cv_list.count(True) / len(control_is_cv_list))

# treatment_cvr 0.031220247540463344
# control_cvr 0.031905453372055505
