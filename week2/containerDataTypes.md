1. List

A list in Python is an ordered collection of items.

Ordered → The items maintain the order in which they are inserted.

Changeable (mutable) → Items can be changed, added, or removed after the list is created.

Allows duplicates → Since lists are indexed, items with the same value are allowed.

Lists can contain different data types (strings, numbers, booleans, even other lists).

Common methods:

append() → Adds an element at the end.

copy() → Returns a copy of the list.

remove() / pop() → Removes elements.

sort(), reverse(), etc.

2. Tuple

A tuple is an ordered collection like a list.

Immutable → Once created, tuple elements cannot be changed, added, or removed.

Allows duplicates → Items with the same value are permitted.

Supports indexing and slicing just like lists.

Tuples can be unpacked into variables:

(a, b, c) = (1, 2, 3)


Common methods:

count() → Returns the number of times a value occurs.

index() → Returns the position of a value.

3. Set

A set is an unordered collection of unique items.

Unordered → Items have no defined order (order may change every time you print).

Unindexed → Items cannot be accessed using index positions.

Does not allow duplicates → If a duplicate item is added, it will be ignored.

Sets are mutable, so you can add or remove items, but you cannot change existing values.

Common methods:

add() → Add an element.

remove() / discard() → Remove an element.

union(), intersection(), difference().

4. Dictionary

A dictionary stores data in key: value pairs.

Ordered (Python 3.7+) → Maintains insertion order.

Mutable → Keys and values can be changed, added, or removed.

Does not allow duplicate keys → If a key is repeated, the last assignment will overwrite the previous one.

Keys must be unique and immutable (string, number, tuple).

Values can be of any type.

Common methods:

get() → Returns value for a key.

update() → Updates dictionary with new key:value pairs.

pop() → Removes a specific key.

popitem() → Removes the last inserted key:value pair.

clear() → Empties the dictionary.

✅ So, in short:

List → Ordered, changeable, allows duplicates.

Tuple → Ordered, unchangeable, allows duplicates.

Set → Unordered, unchangeable items, no duplicates.

Dictionary → Key: value pairs, ordered, changeable, no duplicate keys.

