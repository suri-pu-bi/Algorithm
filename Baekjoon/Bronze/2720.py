# Bronze 3
# 세탁소 사장 동혁


Quarter = 25
Dime = 10
Nickel = 5
Penny = 1

testcase_list = []

T = int(input())
for i in range(0,T) :
    testcase = int(input())
    if testcase <= 500 :
        testcase_list.append(testcase)


for i in range(T) :
    num_q = testcase_list[i]// Quarter
    num_d = testcase_list[i]% Quarter // Dime
    num_n = testcase_list[i]% Quarter % Dime // Nickel
    num_p = testcase_list[i]% Quarter % Dime % Nickel // Penny
    print(num_q, num_d, num_n, num_p, end=" ")
    print()