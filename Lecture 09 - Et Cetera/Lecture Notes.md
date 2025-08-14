CS50's Lecture (9):

## **1. Sets**

* A **set** stores unique items; automatically removes duplicates.
* Useful to extract distinct values from lists or dictionaries.
* **Example:**

  ```python
  houses = set()
  for student in students:
      houses.add(student["house"])
  ```
* Use `sorted(houses)` to iterate in order.

---

## **2. Global Variables**

* Defined **outside functions**, accessible anywhere.
* Problem: reassigning inside a function causes `UnboundLocalError`.
* **Solution:** use `global` keyword inside functions.
* **Better practice:** use a **class** to encapsulate state.

  ```python
  class Account:
      def __init__(self):
          self._balance = 0
      def deposit(self, n): self._balance += n
      def withdraw(self, n): self._balance -= n
  ```

---

## **3. Constants**

* Python has **no true constants**, but convention: **ALL\_CAPS variable names**.
* Placed at top of code; intended to remain unchanged.
* Example:

  ```python
  MEOWS = 3
  for _ in range(MEOWS):
      print("meow")
  ```
* Can define **class-level constants** accessible to all methods:

  ```python
  class Cat:
      MEOWS = 3
      def meow(self):
          for _ in range(Cat.MEOWS): print("meow")
  ```

---


