Working with JSON in Python: Explanation
1. What is JSON?

JSON (JavaScript Object Notation) is a lightweight data-interchange format that is:

Text-based and human-readable.

Represented as key-value pairs, similar to Python dictionaries.

Widely used in APIs, configuration files, and web services to exchange data.

Example JSON:
{
    "id": 100,
    "name": "Alice",
    "marks": 100,
    "skills": ["python", "java"]
}


Why JSON is popular:

Human-readable – easy for developers to read and write.

Language-independent – almost all programming languages can parse JSON.

Lightweight – smaller and faster than XML.

Interoperable – used for data exchange between servers and clients, including web and mobile applications.

Reference:

JSON Official Website

Python JSON Documentation

2. Why use JSON?

JSON is used because:

APIs rely on it – Most modern APIs return data in JSON format. For example, when fetching user info from GitHub:

{
    "login": "octocat",
    "id": 583231
}


Storage and configuration – JSON files can store app settings or local data.

Data interchange – Between Python programs, JavaScript, databases, and web servers.

Ease of parsing – JSON is simple to convert into Python dictionaries or JavaScript objects.

3. Python JSON Module

Python provides the json module to work with JSON. The most common functions are:

a) json.dumps()

Purpose: Converts a Python object (like dict, list) into a JSON string.

Use-case: When sending data to an API or saving JSON to a file.

import json

data = {"id": 100, "name": "Alice"}
json_data = json.dumps(data)  # Convert dict → JSON string
print(json_data)


Output:

{"id": 100, "name": "Alice"}


Key point: The result is a string, not a Python dict.

b) json.loads()

Purpose: Converts a JSON string into a Python object (dict or list).

Use-case: Parsing API responses or reading JSON from a file.

api_response = '{"id": 100, "name": "Alice"}'
data = json.loads(api_response)  # Convert JSON string → Python dict
print(data["name"])


Output:

Alice

c) Parsing JSON string

Parsing means converting the JSON text into a Python object so you can work with it in code.

json.loads() is used for this purpose.

Example:

json_string = '{"skills": ["python", "java"]}'
parsed = json.loads(json_string)
print(parsed["skills"][0])  # Output: python

d) Modifying JSON

Once JSON is parsed into Python objects, you can modify it like any dictionary or list:

import json

# Parse JSON string
json_str = '{"id": 100, "name": "Alice", "marks": 100, "skills": ["python", "java"]}'
data = json.loads(json_str)

# Modify fields
data["marks"] = 105
data["skills"].append("C++")

# Convert back to JSON string
json_data = json.dumps(data, indent=4)
print(json_data)


Output:

{
    "id": 100,
    "name": "Alice",
    "marks": 105,
    "skills": ["python", "java", "C++"]
}


Explanation:

Parsing converts JSON string → Python dict.

You can update values or add new keys.

json.dumps() converts the modified dict back → JSON string, ready to send to APIs or store.


References

Python JSON Module Documentation: https://docs.python.org/3/library/json.html

JSON Official Website: https://www.json.org/json-en.html

Real Python Guide on JSON: https://realpython.com/python-json/
