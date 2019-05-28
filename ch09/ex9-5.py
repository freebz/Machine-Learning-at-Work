# seed 값을 바꿔 테스트 데이터를 생성한다.
test_is_cv_list, test_is_treat_list, test_feature_vector_list = \
   generate_sample_data(sample_num, seed=42)

# 두 모델로 전환율을 예측한다.
treat_score = treat_model.predict_proba(test_feature_vector_list)
control_score = control_model.predict_proba(test_feature_vector_list)

# 점수를 계산한다. (실험군 전환율 / 대조군 전환율)
# predict_proba는 각 클래스에 속할 확률의 리스트를 반환하므로 첫 번째 값만 확인한다.
# 반환값이 numpy.ndarray 타입이므로 그대로 나눠도 요소 단위 나눗셈이 된다.
score_list = treat_score[:,1] / control_score[:,1]
