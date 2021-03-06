# Learn Python

Read Allen Downey's [Think Python](http://www.greenteapress.com/thinkpython/) for getting up to speed with Python 2.7 and computer science topics. It's completely available online, or you can buy a physical copy if you would like.

<a href="http://www.greenteapress.com/thinkpython/"><img src="img/think_python.png" style="width: 100px;" target="_blank"></a>

For quick and easy interactive practice with Python, many people enjoy [Codecademy's Python track](http://www.codecademy.com/en/tracks/python). There's also [Learn Python The Hard Way](http://learnpythonthehardway.org/book/) and [The Python Tutorial](https://docs.python.org/2/tutorial/).

---

### Q1. Lists &amp; Tuples

How are Python lists and tuples similar and different? Which will work as keys in dictionaries? Why?

>> They are both data structures with the ability to index and slice using brackets to reference items within either, and the ability to list duplicate items within either. Lists and tuples are different in the following ways:
>> * Lists are mutable while objects within tuples are immutable
>> * Lists can be and usually are sorted
>> * Items within lists are not grouped while tuples consist of groups of items
>> * Lists consist of items within [ ] separated by commas while tuples consist of groups of items within ( ) separated by commas inside of [ ] separated by commas
>> * Lists usually consist of similar elements (for example, brands of shoes) while tuples are typically heterogeneous items
>> Tuples will work as keys in dictionaries because dictionaries need to be able to map a key to its value by easily comparing keys. In other words, it needs to be hashable and Python lists are not hashable. Additionally, keys shouldn't be mutable and tuples are immutable while lists are mutable.

---

### Q2. Lists &amp; Sets

How are Python lists and sets similar and different? Give examples of using both. How does performance compare between lists and sets for finding an element. Why?

>> They are similar in that both contain collections of items separated by commas, and they are different in that lists can contain duplicate values while sets cannot. Sets are unique unordered collections of items. As example of a set would be users in group (like all the unique users in a LinkedIn college alumni group). An example of a list would be grades students received on a test. Sets perform much better for finding an element in a collection. They have an almost constant time to lookup elements while lists have a linear time to lookup elements.

---

### Q3. Lambda Function

Describe Python's `lambda`. What is it, and what is it used for? Give at least one example, including an example of using a `lambda` in the `key` argument to `sorted`.

>> `lambda ` is like an inline function. It allows you to use a function while not naming or storing it. It's often used with `map` or other functions where you input a callback function. An example would be passing the `lambda` function to the `sorted` method to iterate through a list of tuples that includes a user's first and last name to sort by the last name.

---

### Q4. List Comprehension, Map &amp; Filter

Explain list comprehensions. Give examples and show equivalents with `map` and `filter`. How do their capabilities compare? Also demonstrate set comprehensions and dictionary comprehensions.

>> List comprehension is a way of transforming one list into a new list. It's similar to `map` and `filter` in that both allow you to interate through an old list, transform values, and filter conditionally beforing adding the updated, filtered values to a new list. List comprehensions are usually the default in Python and make it easier to understand what code is doing.

>> The following examples both square each value in the list if it's an even value and add to a new list.  
>> * squared_evens = map(lambda n: n ** 2, filter(lambda n: n % 2 == 1, numbers))  
>> * squared_evens = [n ** 2 for n in numbers if n % 2 == 1]

>> Dictionary and set comprehensions are very similar. Set comprehensions take the same format as list comprehensions, but with {} instead of brackets. The above exampleof squaring all values in the list would be: squared_evens = {n ** 2 for n in numbers}. Dictionary comprehensions take the following format {key: value for (key, value) in iterable}. You can use dictionary comprehensions with the zip method to convert two lists (keys and values) into a dictionary(d): { d = k:v for (k,v) in zip(keys, values)}
---

### Complete the following problems by editing the files below:

### Q5. Datetime
Use Python to compute days between start and stop date.   
a.  

```
date_start = '01-02-2013'    
date_stop = '07-28-2015'
```

>> 937 days

b.  
```
date_start = '12312013'  
date_stop = '05282015'  
```

>> 513

c.  
```
date_start = '15-Jan-1994'      
date_stop = '14-Jul-2015'  
```

>> 7850

Place code in this file: [q5_datetime.py](python/q5_datetime.py)

---

### Q6. Strings
Edit the 7 functions in [q6_strings.py](python/q6_strings.py)

---

### Q7. Lists
Edit the 5 functions in [q7_lists.py](python/q7_lists.py)

---

### Q8. Parsing
Write a script as indicated (using the football data) in [q8_parsing.py](python/q8_parsing.py)





