# -*- coding: utf-8 -*-
# 소수 판별 알고리즘
# 에라토스테네스의 체를 인용하여, 입력된 수의 루트값까지 판별하는 함수.

def sieve(int num):
	if num != 1:
		for i in range(2, num):
			if num % i == 0:
				False
	else:
		False
	return True