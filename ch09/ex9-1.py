import random

def generate_sample_data(num, seed=1):
    # 반환할 리스트 초기화
    is_cv_list = []
    is_treat_list = []
    feature_vector_list = []

    # 난수 생성기 초기화
    random_instance = random.Random(seed)

    # 데이터의 설정값
    feature_num = 8
    base_weight = \
      [0.02, 0.03, 0.05, -0.04, 0.00, 0.00, 0.00, 0.00]
    lift_weight = \
      [0.00, 0.00, 0.00, 0.05, -.05, 0.00, 0.00, 0.00]

    for i in range(num):
        # 난수로 특징 벡터 생성
        feature_vector = \
           [random_instance.random()
              for n in range(feature_num)]
        # 실험군 여부를 무작위로 결정
        is_treat = random_instance.choice((True, False))
        # 전활율 계산
        cv_rate = \
           sum([feature_vector[n] * base_weight[n]
              for n in range(feature_num)])

        if is_treat:
            # 실험군에 속하면 lift_weight의 영향을 추가
            cv_rate += \
               sum([feature_vector[n] * lift_weight[n]
                  for n in range(feature_num)])

        # 실제 전환 여부 결정
        is_cv = cv_rate > random_instance.random()

        # 생성된 값 저장
        is_cv_list.append(is_cv)
        is_treat_list.append(is_treat)
        feature_vector_list.append(feature_vector)

    # 생성한 데이터 반환
    return is_cv_list, is_treat_list, feature_vector_list
