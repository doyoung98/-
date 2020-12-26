#!/usr/bin/env python
# coding: utf-8

# In[1]:


# <문제> 정수를 2개 이상 입력하면, 정수별 팩토리얼값의 총계/평균/최대/최소값을 출력하는 프로그램을 만들어주세요..
- 조건1. 입력받는 정수는 5 이상 이어야 합니다.
- 조건2. 정수를 2개 이상 입력받아야 합니다.
- 조건3. 출력값에는 세자리수마다 콤마(,)를 찍어주세요
- 조건4. def는 1회만 사용합니다.

# 입력 예시 : 5, 12, 6
# 출력 예시 : 
총계 : 479,002,440
평균 : 159,667,480
최대 : 479,001,600
최소 : 120


# In[54]:


def factorialresult(*args):
    total = []
    for arg in args:
        num = 1
        if arg <5:
            print("(error)5이상의 정수를 입력바랍니다")
            continue
        for i in range(1, arg+1):
            num *= i
        total.append(num)
    print(total)
    print("총계:{}".format(sum(total)))
    print("평균:{}".format(sum(total)/len(total)))
    print("최대:{}".format(max(total)))
    print("최소:{}".format(min(total)))
    
factorialresult(5,12,6)


# In[ ]:




