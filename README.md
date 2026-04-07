# Smart-Payment-Processing-System_Nitu-sharma_202501100700201_B
# Smart Payment Processing System (OOP in Python)

## Overview

This project implements a **Smart Payment Processing System** using **Object-Oriented Programming (OOP)** concepts in Python. It demonstrates key principles such as **abstraction, inheritance, and polymorphism** through multiple payment methods.

The system allows users to process payments using different payment modes like Credit Card, UPI, PayPal, and Digital Wallet, each with its own business logic.

---

## Features

* Common abstract base class for all payment methods
* Multiple payment types with unique processing logic
* Automatic receipt generation
* Wallet balance management with transaction validation
* Runtime polymorphism using a unified payment processor

---

## Technologies Used

* Python 3
* OOP Concepts (Abstraction, Inheritance, Polymorphism)

---

## Class Structure

### 1. Payment (Abstract Base Class)

* Stores user details
* Defines abstract method:

  * `pay(amount)`
* Provides:

  * `generate_receipt()`

---

### 2. Payment Methods

#### CreditCardPayment

* Applies:

  * 2% gateway fee
  * 18% GST on gateway fee
* Final amount = original + fee + GST

#### UPIPayment

* Cashback:

  * ₹50 if amount > 1000
* Final amount = original - cashback

#### PayPalPayment

* Applies:

  * 3% international fee
  * ₹20 fixed charge
* Final amount = original + charges

#### WalletPayment

* Maintains wallet balance
* Deducts amount if sufficient balance
* Fails transaction if balance is insufficient

---

## Polymorphism

The function below demonstrates **runtime polymorphism**:

```python
def process_payment(payment, amount):
    payment.pay(amount)
```

The same function behaves differently depending on the payment object passed.

---


## Example Output

```
User: Nitu
Original Amount: ₹1000
------------------------------
User: Nitu
Original Amount: ₹1500
Final Amount Paid: ₹1450
------------------------------
User: Nitu
Original Amount: ₹2000
Final Amount Paid: ₹2080.0
------------------------------
User: Nitu
Original Amount: ₹500
Final Amount Paid: ₹500
------------------------------
Remaining Wallet Balance: ₹1000
------------------------------
User: Nitu
Transaction Failed: Insufficient Balance
------------------------------
```

## Concepts Demonstrated

* Abstraction using abstract base class
* Inheritance for extending payment types
* Polymorphism through common interface
* Encapsulation of payment logic
