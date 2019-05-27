from sklearn.feature_extraction import DictVectorizer

# 입력 데이터의 원시 데이터(레이블인 점수는 포함하지 않음)
# {사용자 ID, 이 사용자가 평가한 아이템 ID, 사용자의 나이}를 담은 딕셔너리
train = [
    {"user": "1", "item": "5", "age": 19},
    {"user": "2", "item": "43", "age": 33},
    {"user": "3", "item": "20", "age": 55},
    {"user": "4", "item": "10", "age": 20}
]

# DictVectorizer 객체를 사용하여 age를 제외한 필드를 더미 변수로 변환한다.
v = DictVectorizer()
X = v.fit_transform(train)

# user, item은 문자열이므로 더미 변수로 변환하였다.
# [[ 19. 0. 0. 0. 1. 1. 0. 0. 0.]
#  [ 35. 0. 0. 1. 0. 0. 1. 0. 0.]
#  [ 55. 0. 1. 0. 0. 0. 0. 1. 0.]
#  [ 20. 1. 0. 0. 0. 0. 0. 0. 1.]]
