import urllib.request
import json
import os
import time

os.makedirs('result', exist_ok=True)

search_term = ""
sort_key = 'newest'
category_list = [16, 331, 332, 333, 334, 335, 336,
                 337, 52, 362, 338, 51, 339, 340,
                 341, 342]  # 기술(technology) 분야
query_base = "https://www.kickstarter.com/projects/search.json?term=%s&category_id=%d&page=%d&sort=%s"

for category_id in category_list:
    for page_id in range(1, 201):
        try:
            query = query_base % (
                search_term, category_id, page_id, sort_key)
            print(query)
            data = urllib.request.urlopen(query).read().decode("utf-8")
            response_json = json.loads(data)
        except:
            break

    # 1페이지당 20건인 검색 결과를 하나씩 저장한다.
    for project in response_json["projects"]:
        filepath = "result/%d.json" % project["id"]
        fp = open(filepath, "w")
        fp.write(json.dumps(project, sort_keys=True, indent=2))
        fp.close()

    # API 접근에 1초 간격을 두어 서비스에 부담을 주지 않도록 한다.
    time.sleep(1)
