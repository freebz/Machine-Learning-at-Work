from sklearn.model_selection import train_test_split

train_is_cv_list, test_is_cv_list, train_is_treat_list, \
test_is_treat_list, train_feature_vector_df, \
test_feature_vector_df = \
   train_test_split(is_cv_list, is_treat_list,
                    feature_vector_df, test_size=0.5,
                    random_state=42)

# index 리셋
train_feature_vector_df = \
   train_feature_vector_df.reset_index(drop=True)
test_feature_vector_df = \
   test_feature_vector_df.reset_index(drop=True)
