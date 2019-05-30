train_sample_num = len(train_is_cv_list)

treat_is_cv_list = []
treat_feature_vector_list = []
control_is_cv_list = []
control_feature_vector_list = []

for i in range(train_sample_num):
    if train_is_treat_list[i]:
        treat_is_cv_list.append(train_is_cv_list[i])
        treat_feature_vector_list.append(
            train_feature_vector_df.loc(i))
    else:
        control_is_cv_list.append(train_is_cv_list[i])
        control_feature_vector_list.append(
            train_feature_vector_df.loc(i))

from sklearn.linear_model import LogisticRegression
treat_model = LogisticRegression(C=0.01)
control_model = LogisticRegression(C=0.01)

treat_model.fit(treat_feature_vector_list,
                treat_is_cv_list)
control_model.fit(control_feature_vector_list,
                  control_is_cv_list)
