# -*- coding: utf-8 -*-

import datetime
from pytz import timezone

# 현재시간 가져오기
now = datetime.datetime.now()
# +timezone 반영
now_seoul = datetime.datetime.now(timezone("Asia/Seoul"))

# 주어진 string datetime object로 변환
exdate = "Mar 26 12:00:00 2022"
dateobj = datetime.datetime.strptime(exdate, "%b %d %H:%M:%S %Y")
dateobj = dateobj.replace(tzinfo=timezone("GMT"))

# dateobj의 timezone 변환
dateobj_kst = dateobj.astimezone(timezone("Asia/Seoul"))
dateobj_kst2 = dateobj_kst.strftime("%Y-%m-%d %H:%M:%S %Z")

# 시간계산
leftdaystime = dateobj_kst - now_seoul
