参考资料1： [Complexity of Python Operations](https://www.ics.uci.edu/~brgallar/week8_2.html)     
参考资料2： [Time Complexity Wiki](https://wiki.python.org/moin/TimeComplexity)


# List

List比较适合按照位置的indexing，但是**search，add，delete**这样的操作就非常不适合。索引和增减新元素的过程是O(1)，但是问题是操作之后由于list的特性，**之后所有的元素都要移动位置**，而且不按位置search的话都需要遍历所有的元素。

下面是几个list/array比较耗时的operation，复杂度为`O(N)`. **非常不建议在loop中使用**

The following Python list operations operate on a subset of the elements, but still have time complexity that depends on n = len(a).

|  code | worst-case time  | note |   
|---|---|---|
|  `a.insert(i, x)` |  `n-i` | 按照index位置插入元素，索引元素的步骤是O(1)，但是插入之后所有的item会移动 |  
|`a.pop(i)`   | `n-i`  | 按照index位置删除元素，索引元素的步骤是O(1)，但是删除之后所有的item会移动|
|  `del a[i]` |  `n-i` |   |
| `del [i:j]`  |  `n-i` |   |
| `a.remove(x)`  | `n`  |  每次也是删除first occurance。同样的，remove元素后，所有后面的元素会移动 |
| `a.index(x)`  | `n`   |  |
| `x in a`  | `n`   | `set`和`dict`的in运算复杂度为O(1) |
| `max(a)` or `min(a)`  | `n`   |  |
| `len(a)`  | `1`   |  |
| `count` or `remove` or`reverse`   | `n`   |注意`len`是O(1), `count`是count某个元素的频率。remove和index都是返回的first occurrence |


**Note**: `a.append(x)` takes constant amortized time, even though the worst-case time is linear.


# Set
set是一种unordered structure，是不能通过顺序索引的。    
Set不涉及两个set的运算，复杂度基本上都是O(1)，例如`remove`/`discard`, `add`
**注意：** Set没有`del`这个运算，因为既没有`key`也没有`index`     

|  code |example|  worst-case time  | note |   
|---|---|---|---|
|Length        | len(s)       | O(1)	     ||
|Add           | s.add(5)     | O(1)	     ||
|Containment   | x in/not in s| O(1)	     | compare to list/tuple - O(N)|
|Remove        | s.remove(5)  | O(1)	     | compare to list/tuple - O(N)|
|Discard       | s.discard(5) | O(1)	     | discard是不管有没有都能discard，remove的话，如果元素不存在则会报错|
|Pop           | s.pop()      | O(1)	     | compare to list - O(N)|
|Clear         | s.clear()    | O(1)	     | similar to s = set()|
|Construction  | set(...)     | len(...)      ||
|check ==, !=  | s != t       | O(min(len(s),lent(t))|
|<=/<          | `s <= t` or `s.issubset(t)`       | O(len(s1))    | issubset|
|>=/>          | s >= t       | O(len(s2))    | issuperset s <= t == t >= s|
|Union         | `s | t` or `s.union(t)`        | O(len(s)+len(t))|
|Intersection  | `s & t` or `s.intersection(t)`       | O(min(len(s),lent(t))|
|Difference    | `s - t` or `s.difference(t)`     | O(len(t))     ||
|Symmetric Diff| s ^ t        | O(len(s))     ||
|Iteration     | for v in s:  | O(N)          ||
|Copy          | s.copy()     | O(N)	     || 



# Dict / Defaultdict

可以看到大部分都是`O(1)`
                               Complexity
Operation     | Example      | Class         | Notes|
|---|---|---|---|
Index         | d[k]         | O(1)	     ||
Store         | d[k] = v     | O(1)	     ||
Length        | len(d)       | O(1)	     ||
Delete        | del d[k]     | O(1)	     ||
get/setdefault| d.method     | O(1)	     |`phoneext.get("kent","NO ENTRY")`, 不存在就赋值|
Pop           | d.pop(k)     | O(1)	     ||
Pop item      | d.popitem()  | O(1)	     ||
Clear         | d.clear()    | O(1)	     | similar to s = {} or = dict()|
Views         | d.keys()     | O(1)	     ||
Construction  | dict(...)    | len(...)      ||
Iteration     | for k in d:  | O(N)          | all forms: keys, values, items|
