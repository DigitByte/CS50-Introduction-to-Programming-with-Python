CS50P – Lecture Notes (8)

## **1. Concepts**

* **Class:** Blueprint for objects.
* **Object:** Instance of a class.
* **Attributes:** Data stored in an object.
* **Methods:** Functions inside a class.
* **Encapsulation:** Protect attributes with getters/setters.
* **Inheritance:** Child class reuses parent class code.
* **Operator Overloading:** Customize operators (`+`, `-`) for objects.

---

## **2. Class Basics**

* Constructor: `__init__(self, attr1, attr2)`
* Print representation: `__str__(self)`
* Access attributes: `object.attr`

**Example:**

```python
class Student:
    def __init__(self, name, house):
        self.name = name
        self.house = house
```

---

## **3. Encapsulation**

* **Getter:** `@property`
* **Setter:** `@attr.setter` with validation
* Protects attributes and ensures valid values

---

## **4. Class & Static Methods**

* **Class method:** `@classmethod` → operates on class (`cls`)
* **Static method:** `@staticmethod` → independent of class or instance

---

## **5. Inheritance**

* Child class inherits from parent: `class Child(Parent):`
* Call parent constructor: `super().__init__(args)`

**Example:**

```python
class Wizard:
    def __init__(self, name): self.name = name

class Student(Wizard):
    def __init__(self, name, house):
        super().__init__(name)
        self.house = house
```

---

## **6. Exceptions**

* Validate data: `raise ValueError("message")`
* Exceptions hierarchy: `BaseException → Exception → ValueError, KeyError, etc.`

---

## **7. Operator Overloading**

* Special methods customize behavior:

  * `__add__` → `+`
  * `__sub__` → `-`

---

## **8. Python Built-ins are OOP**

* Everything is a class:

```python
type(50)      # int
type("text")  # str
type([])      # list
type({})      # dict
```

---

 **Notes**

* Use classes to **group data & behavior**.
* Use **properties** for validation.
* Inheritance reduces code duplication.
* Exceptions make code safer.
* OOP + Python built-ins = powerful & consistent coding pattern.
