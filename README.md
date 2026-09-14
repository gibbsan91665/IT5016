# IT5016 — Software Development Portfolio

## Overview

This repository contains assessment prototypes and laboratory exercises demonstrating procedural programming and object-oriented programming in Python.

The main programs are:

1. **Purchase Requisition System — Part A:** A function-based application for collecting staff details, calculating requisition totals, and assigning approval status.
2. **Purchase Requisition System — Part B:** An object-oriented version that stores requisition data in objects and tracks shared statistics.
3. **Inventory Management System:** A menu-driven prototype for adding, updating, and displaying inventory items.
4. **Simple Library System:** An object-oriented application that models books, members, borrowing, and returns.
5. **Week 4 Exercises:** Small examples covering functions, parameters, return values, arithmetic, and global variables.

These programs show a progression from basic functions and shared variables to classes, instance attributes, and object collaboration.

## Requirements and Organisation

- Python 3
- A terminal or Python-compatible IDE
- No third-party packages are required

## Program Features and Logic

### Part A: Procedural Purchase Requisition System

The program uses four functions:

- `staff_info()` collects staff information and generates a requisition ID.
- `requisitions_total()` collects item prices and calculates the total.
- `requisition_approval()` determines the approval status.
- `display_requisitions()` runs the workflow and displays the final details.

Staff information is returned as a dictionary. Later functions add the total, status, and approval reference to that dictionary.

**Business rules:**

- Requisition IDs begin at `10001`.
- A total below 500 is automatically approved.
- A total of exactly 500 or more remains pending.
- An approval reference combines the staff ID with the final three digits of the requisition ID.
- Entering `done` or an empty item name ends item entry.

For example, staff ID `FN19` and requisition ID `10001` produce approval reference `FN19001` when approved.

The counter generates distinct IDs within one program run. It resets when the program restarts.

### Part B: Object-Oriented Purchase Requisition System

The `RequisitionSystem` class represents an individual requisition while also maintaining shared statistics.

**Instance attributes** store information belonging to one requisition:

- Staff details and requisition ID
- Item names and prices
- Total value
- Approval status and reference

**Class attributes** store values shared across requisition objects:

- ID counter
- Total requisitions processed
- Approved and pending counts
- Combined requisition value

The constructor, `__init__()`, sets the initial state and assigns an ID. The `display_statistics()` class method displays the shared totals.

Compared with Part A, this version stores item details and retries invalid price input for the same item. It also rejects negative prices.

The demonstration creates two objects. Their approval outcomes depend on the values entered; the printed “Under 500” and “Over 500” headings do not enforce those amounts.

### Inventory Management System

Inventory records are stored in a dictionary keyed by item ID. Each record contains a name, quantity, and unit price.

The main functions are:

| Function | Responsibility |
| --- | --- |
| `add_inventory_item()` | Collect and store an item with an automatically generated ID |
| `calculate_total_value()` | Add a new item and calculate quantity multiplied by price |
| `update_inventory(item_id)` | Update an existing item's quantity and price |
| `display_inventory_item(item_id)` | Display an item's details and calculated value |

Item IDs begin at `1000`. The menu provides access to these functions and an exit option.

The program rejects negative quantities and prices and handles missing item IDs with user-friendly messages.

**Important behaviour:** Menu option 2 adds a new item before calculating its value. It does not calculate the value of an existing item or the entire inventory.

### Simple Library System

The library program uses three classes:

- `Book` stores a title, author, and borrowing status.
- `Member` stores a name and a list of borrowed books.
- `Library` manages collections and coordinates borrowing and returns.

The demonstration adds three books, registers two members, lends a book to Alice, rejects Bob's attempt to borrow the same book, and processes Alice's return.

Book-title matching is case-insensitive.

## Software Design Principles Demonstrated

### 1. Modularity

Modularity divides a program into smaller, understandable components.

**Evidence in the code:**

- The requisition programs separate staff entry, total calculation, approval, and display into named functions or methods.
- The inventory program has separate operations for adding, updating, and displaying records.
- The arithmetic exercise defines `add()` and `multiply()` separately.

**Benefit:** Smaller components make the programs easier to read and locate when changes are needed.

**Limitation:** Some components still perform several tasks. For example, `requisitions_total()` collects input and calculates a result rather than providing an independently testable calculation.

### 2. Separation of Concerns and Single Responsibility

These principles encourage different responsibilities to be handled in different parts of a program.

**Evidence in the code:**

The library system separates book data, member data, and library-level operations into `Book`, `Member`, and `Library`.

**Benefit:** A change to book display formatting can usually be made without changing the borrowing workflow.

**Limitation:** Separation is only partial. Many methods combine terminal input/output with business logic. In Part B, `requisition_approval()` starts data collection, decides the status, updates statistics, and prints results.

### 3. Encapsulation

Encapsulation groups related data and behaviour together.

**Evidence in the code:**

- `RequisitionSystem` groups requisition attributes with methods that process them.
- `Book` groups book details with its availability state.
- `Member` groups membership details with a borrowed-book list.

**Benefit:** Related information is kept together rather than spread across unrelated global variables.

**Limitation:** The attributes are public and can be changed directly. The classes demonstrate basic encapsulation, but do not fully protect their internal state from invalid changes.

### 4. DRY — Don't Repeat Yourself

DRY encourages reuse of shared logic instead of maintaining unnecessary duplicates.

**Evidence in the code:**

- `add_and_multiply()` reuses `add()` and `multiply()`.
- `calculate_total_value()` reuses `add_inventory_item()`.
- The requisition workflows call existing functions or methods rather than duplicating the entire input process.

**Benefit:** Shared behaviour can be changed in one place.

**Limitation:** Inventory quantity and price validation are repeated in the add and update functions. Reusable input-validation helpers would reduce this duplication.

Reusing an interactive function also introduces side effects: calculating inventory value currently requires adding a new record.

### 5. KISS — Keep It Simple

KISS favours straightforward solutions appropriate to the requirements.

**Evidence in the code:**

- Dictionaries and lists store prototype data.
- A simple conditional implements the approval rule.
- The inventory system uses a numbered terminal menu.

**Benefit:** The programs are easy to follow and require no external dependencies.

**Trade-off:** In-memory storage is suitable for demonstrations, but it does not preserve records after the application closes.

### 6. Defensive Programming

Defensive programming anticipates invalid input and unexpected situations.

**Evidence in the code:**

- `try`/`except ValueError` handles invalid numeric input.
- Part B and the inventory program reject negative prices.
- Inventory functions check whether an ID exists.
- The library checks whether a book is already borrowed.

**Benefit:** These checks reduce common input errors and provide clearer feedback.

**Limitation:** Validation is incomplete. Staff details and item names can be empty, dates are not validated, and floating-point inputs such as `nan` and `inf` are not rejected.

## Design Rationale and Learning Progression

The structure of the examples illustrates three stages of development:

1. **Basic functions:** Practise inputs, parameters, calculations, and return values.
2. **Procedural applications:** Connect functions into a workflow and share data through dictionaries or global variables.
3. **Object-oriented applications:** Group related state and behaviour into objects and coordinate interactions between them.

Part A uses a dictionary to transfer requisition information between functions. Part B instead retains this information on an object.

This makes managing multiple requisitions more natural, although shared class statistics introduce additional state that must be managed carefully.

The library example extends this approach by using several collaborating classes rather than putting all responsibilities into one class.

These are design interpretations based on the supplied code, rather than a record of development decisions made at the time.

## Summary of Comments and Code Review Findings

The comments and docstrings explain task boundaries, function purposes, ID generation, shared statistics, and the demonstration sequence.

Reviewing the implementation identified the following issues:

### Inventory Indentation

`add_inventory_item()` and `calculate_total_value()` contain inconsistent indentation. Python uses indentation to define blocks, so the supplied inventory script will not run until this is corrected.

Use four spaces for each indentation level.

### Reprocessing a Requisition

In Part B, calling `requisition_approval()` more than once on the same object:

- Counts the object again in the shared statistics.
- Resets the total but does not clear `self.items`.
- Can retain an old approval reference if a previously approved object becomes pending.

The current implementation therefore assumes each object is processed once.

### Validation Differences

Part A accepts negative prices. When a price is not numeric, it returns to the item-name prompt instead of retrying the price for that item.

Part B improves this behaviour with a nested validation loop.

Both versions can approve an empty requisition because its total is zero.

### Financial Precision

Prices use `float`, which can introduce binary floating-point rounding errors.

For financial calculations, `decimal.Decimal`, created from input strings, would be a more appropriate alternative.

### Library State Consistency

The normal `Library` workflow updates both book availability and the member's borrowed-book list.

However, directly calling `Member.borrow_book()` does not update availability or check for duplicate borrowing. The library also does not verify that a borrowing member is registered.

Additional checks would better preserve consistency.

### Naming and Cleanup improvements

- Rename 'display_requisitions()` to `display_requisitions()` and update its callers.
- Remove the unused `random` import.
- In the simple addition exercise, rename the local variable `add_numbers` to `total` to avoid reusing the function's name.
- Review the inventory currency prompts: a literal currency symbol does not need a preceding backslash in a normal Python string.

## Research and Further Reading


The following official references are recommended for checking the concepts and improvements discussed:

- [Python: Defining Functions](4. More Control Flow Tools — Python 3.14.7 documentation)  
  Function definitions, parameters, and reusable operations.

- [Python: Classes](9. Classes — Python 3.14.7 documentation)  
  Classes, instance attributes, and class variables.

- [Python: Errors and Exceptions](8. Errors and Exceptions — Python 3.14.7 documentation)  
  Handling conversion errors with `try` and `except`.

- [Python: Decimal Arithmetic](Decimal fixed-point and floating-point arithmetic — Python 3.14.7 documentation)  
  Decimal calculations for applications requiring financial precision.

- [PEP 8 — Style Guide for Python Code](PEP 8 – Style Guide for Python Code)  
  Consistent indentation, naming, and code layout.

## Running the Programs

Save the programs separately using the suggested filenames. Correct the inventory indentation before running it.

From the project directory, run the desired script:

```bash
python requisition_part_a.py
python requisition_part_b.py
python inventory_system.py
python library_system.py
```

Depending on the installation, use `python3` instead of `python`.

The requisition and inventory programs require terminal input. The library demonstration uses predefined books and members.

The `if __name__ == "__main__":` guards in the main programs prevent their demonstration blocks from running when those modules are imported.

## Testing Plan

The supplied examples include interactive demonstrations, but no automated assertions. The following tests are proposed and have not been executed for this README.

| Scenario | Expected result |
| --- | --- |
| Requisition total of 499.99 | Approved with an approval reference |
| Requisition total of exactly 500 | Pending with reference `N/A` on a new object |
| Requisition total of 500.01 | Pending |
| Part B receives a negative price | Reject it and request another price |
| Part B receives nonnumeric price input | Display an error and retry |
| Process one approved and one pending object once | Statistics show 2 total, 1 approved, and 1 pending |
| Inventory quantity 3 and unit price 12.50 | Item value is 37.50 |
| Update an unknown inventory ID | Display an error without changing inventory |
| Borrow an available book | Mark it borrowed and add it to the member's list |
| Borrow an already borrowed book | Reject the request |
| Return a borrowed book | Mark it available and remove it from the member's list |

Future automated tests should separate calculations and business rules from interactive input so they can be tested directly.

## Limitations and Future Improvements

Priority improvements are:

1. Fix the inventory indentation.
2. Strengthen validation for required fields, dates, and finite numeric values.
3. Prevent duplicate processing of requisition objects.
4. Separate input/output from calculations and approval logic.
5. Replace duplicated validation with reusable helpers.
6. Use decimal arithmetic for money.
7. Add automated tests, especially for approval boundaries and invalid input.
8. Save records and counters to a file or database.
9. Validate library membership and keep borrowing state consistent.
10. Replace the repeated approval threshold with a named constant.

IDs are only unique within their current run and counter scope. Approval references can repeat because they use only the final three digits of the requisition ID.

## Conclusion

This portfolio demonstrates modular programming, function reuse, basic encapsulation, simple business rules, and defensive input handling.

The strongest learning progression is the move from function-based workflows to objects that retain their own state and collaborate with other objects.

The prototypes meet useful learning goals, but require stronger validation, clearer responsibility boundaries, persistent storage, and verified testing before they could be considered production-ready.
