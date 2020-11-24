# 구구단 출력하기 - 1
# for 단 in range(2, 10):
#     for 수 in range(1, 10):
#         print("%dx%d =%d" %(단, 수, 단*수) )
#     print()

# 구구단 출력하기 - 2
for 수 in range(1, 10):
    for 단 in range(2, 10):
        print("%dx%d =%d" %(단, 수, 단*수), end="\t")
    print()  # 다음 줄로 이동

    