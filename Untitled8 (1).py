#!/usr/bin/env python
# coding: utf-8

# In[18]:


- 조건1. 예외 처리가 필요한 곳을 찾아, 3가지의 예외 처리 구문을 코드에 포함해주세요. 
- 조건2. 계산기는 덧셈, 뺄셈, 곱셈, 나눗셈을 지원하며 이는 함수를 따로 만들어서 구현해주세요. 


# In[19]:


print("""
1. 더하기
2. 빼기
3. 곱하기
4. 나누기
""")

num = input("아래에 사용을 원하시는 사칙연산을 선택해주세요!: ")
a = int(input("A변수를 입력해주세요: "))
b = int(input("B변수를 입력해주세요: "))

if num == 1:
    print(a+b)
def min(a, b):
    return a-b
def mul(a, b):
    return a*b
def div(a, b):
    return a/b


# In[ ]:





# In[ ]:





# In[17]:


# <문제>.sort() 함수와 같은 동작을 하는 sort(List) 함수를 정의하시오. 
# <조건> 기존의 내장 함수 sort()는 사용 금지. 없다고 생각하고 직접 정의해보세요^^~

def sort(List):
    result = []
    for i in range(len(List)):
        c = min(List)
        result.append(c)
        List.remove(c)
    return result

l = [5, 9, 10, 8, 2, 1, 6, 3, 4, 7]
print(sort(l))


# In[ ]:




