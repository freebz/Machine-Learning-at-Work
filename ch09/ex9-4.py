from sklearn.linear_model import LogisticRegression

# 학습기 초기화
treat_model = LogisticRegression(C=0.01)
control_model = LogisticRegression(C=0.01)

# 학습
treat_model.fit(treat_feature_vector_list, treat_is_cv_list)
control_model.fit(control_feature_vector_list, control_is_cv_list)
