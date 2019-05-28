import glob
import json
import pandas
import pandas.io.json

project_list = []

# glob으로 result 디렉터리에 있는 파일을 읽는다.
for filename in glob.glob("result/*.json"):
    project = json.loads(open(filename).read())
    project_list.append(project)

# json_normalize 함수를 사용하여 DataFrame으로 변환한다.
df = pandas.io.json.json_normalize(project_list)

# 값이 "_at"으로 끝나는 unixtime 칼럼을 datetime으로 변환한다.
datetime_columns = filter(lambda a: a[-3:] == "_at", df.columns)
for column in datetime_columns:
    df[column] = pandas.to_datetime(df[column], unit='s')

# DataFrame을 CSV 포맷 문자열로 변환한다.
csv_data = df.to_csv()

# 엑셀에서 임포트하기 쉽도록 CP949로 변환한다.
csv_data = csv_data.encode("cp949", "ignore")

# 변환한 결과를 파일에 쓴다.
fp = open("kickstarter_result.csv", "wb")
fp.write(csv_data)
fp.close()
