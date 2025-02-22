# Python基础

## 基础

### 注释

```python
# 单行注释
''' 多行注释 '''
print()
```

### 输出

```python
# 输出单行
x=1
y=2
print(f"一个简单的数学问题：\"{x} + {y} = ?\"，答案是 {x+y}！") # f-strings

# 输出多行
print("""
这是第一行
这是第二行
""")
```

### 输入

```python
# 注意：返回的格式是字符串
name = input("输入你的名字：")

# 输入多个参数
a, b = input().split(",")
print(f"a = {a}, b = {b}")
```



## 数据类型和操作

- 类型：

  整数 Integer（int）、浮点数 Float、布尔值 Boolean（bool）、字符串 String（str）

  列表 List、元组 Tuple、集合 Set、字典 Dictionary（dict，或者 映射 map）、复数 Complex Number（complex)

- 操作

  `/` 指的是**浮点数**除法，它的结果是一个浮点数，例如 `2/1` 的结果是 `2.0`

  `//` 指的是**整除**除法，它的计算结果是整数，舍弃余数

  `%` 代表模运算（取余），结果为商的余数

## 变量与函数

- 变量

  ```python
  # 多变量赋值
  a, b, c = 1, 2, 6
  print(f"a={a}, b={b}, c={c}")
  ```

- 函数

  ```python
  def Multi_Return_Values():
      return 9, 2, 8
  a, b, c = Multi_Return_Values()
  print(f"a={a}, b={b}, c={c}")
  ```

## 条件

```python
def getGrade(score):
    if score >= 90:
        grade = "A"
    elif score >= 80:
        grade = "B"
    elif score >= 70:
        grade = "C"
    elif score >= 60:
        grade = "D"
    else:
        grade = "F"
    return grade

print("103 -->", getGrade(103))
print(" 88 -->", getGrade(88))
print(" 70 -->", getGrade(70))
print(" 61 -->", getGrade(61))
print(" 22 -->", getGrade(22))
```

## 循环

```python
def sumFromMToN(m, n):
    total = 0
    # 注意： range(x, y) 是左闭右开区间，包含 x，不包含 y
    for x in range(m, n+1):
        total += x
    return total
sumFromMToN(5, 10)
# output:45
```

## 字符串

```python
print("abc" + "def")	# abcdef
print("abc" * 3)		# abcabcabc
print("ring" in "strings") # True
print("wow" in "amazing!") # False
print("Yes" in "yes!") # False
print("" in "No way!") # True
print("聪明" in "聪明办法学 Python") # True
s = "Datawhale"
print(s[0:4])	#Data
print(s[4:9])	#whale
```

```python
# 翻转字符串
def reverseString(s):
    return s[::-1]

print(reverseString(s))
```

