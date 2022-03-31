# 손익분기점 : [상품 가격 * 상품판매량 > 고정비용 + 가변비용 * 상품판매량] -> 인 시점
import sys
# a: 고정비용, b: 가변비용, c: 상품 가격
a, b, c = map(int, sys.stdin.readline().split())
if b >= c:
  print(-1)
else:
  # 상품판매량
  print((a//(c-b))+1)