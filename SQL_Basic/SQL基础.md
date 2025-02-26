# SQL基础

## 数据库

- 层次数据库（Hierarchical Database，HDB）

- 关系数据库（Relational Database，RDB）

  - Oracle Database：甲骨文公司的RDBMS
  - SQL Server：微软公司的RDBMS
  - DB2：IBM公司的RDBMS
  - PostgreSQL：开源的RDBMS
  - MySQL：开源的RDBMS

  如上是5种具有代表性的RDBMS，其特点是由行和列组成的二维表来管理数据，这种类型的 DBMS 称为关系数据库管理系统（Relational Database Management System，RDBMS）。

- 面向对象数据库（Object Oriented Database，OODB）

- XML数据库（XML Database，XMLDB）

- 键值存储系统（Key-Value Store，KVS），举例：MongoDB

## 基本操作

### 创建 / 删除表

```sql
CREATE TABLE < 表名 >
( < 列名 1> < 数据类型 > < 该列所需约束 > < 默认设置 > ,
  < 列名 2> < 数据类型 > < 该列所需约束 > < 默认设置 > ,
  < 列名 3> < 数据类型 > < 该列所需约束 > < 默认设置 > ,
  < 列名 4> < 数据类型 > < 该列所需约束 > < 默认设置 > ,
  .
  .
  .
  < 该表的约束 1> , < 该表的约束 2> ,……);
DROP TABLE < 表名 > ;
```

### 增删改查

#### 增（INSERT）

```mysql
INSERT INTO <表名> (列1, 列2, 列3, ……) VALUES (值1, 值2, 值3, ……);  

-- eg.假设有一个名为`students`的表，包含`id`, `name`, `age`, `class`四个字段：
INSERT INTO students (id, name, age, class)
VALUES (1, '张三', 20, '计算机科学与技术1班');
```

#### 删（DELETE）

```mysql
DELETE FROM <表名> WHERE <条件>;

-- eg.删除`students`表中`id`为1的记录：
DELETE FROM students
WHERE id = 1;
```

#### 改（UPDATE）

```mysql
UPDATE <表名>
SET 列1 = 值1, 列2 = 值2, ……
WHERE <条件>;

-- eg.更新`students`表中`id`为1的学生年龄：
UPDATE students
SET age = 21
WHERE id = 1;
```

#### 查（SELECT）

```mysql
SELECT 列1, 列2, …… FROM <表名>
WHERE <条件>;

-- eg.查询`students`表中所有学生的姓名和年龄：
SELECT name, age FROM students;
-- eg.查询`id`为1的学生的所有信息：
SELECT * FROM students
WHERE id = 1;
```

