# BANKING-SYSTEM-PYTHON
🏦 A simple CLI-based Bank Management System in Python using CSV for storage. Supports account creation, deposit, withdrawal, and deletion. Ideal for beginners learning file handling and Python basics.
🏦 Bank Management System (CLI-based in Python)
This is a simple command-line based Bank Management System built with Python and CSV file handling. It allows users to create bank accounts, deposit or withdraw money, and manage account records — all from the terminal.

📂 Features
Create a new account with name, mobile number, and account type

Auto-generate a unique 10-digit account number

Deposit money into an existing account

Withdraw money from an account (no overdraft check yet)

Delete an account by account number

All data stored persistently in a CSV file (customer.csv)

🧾 Account CSV Format
The customer.csv file stores each account in the following format:

Name, Mobile Number, Account Type, Account Number, Balance
Example:

John Doe,9876543210,saving,1234567890,5000
🚀 How to Run
Make sure you have Python 3 installed.

Save the Python script (bank_system.py) in your working directory.

Open terminal or command prompt and run:

python bank_system.py
Follow on-screen prompts to interact with the system.

📌 Requirements
Python 3.x

No external libraries required (uses only built-in modules: csv, random)

📈 Improvements You Can Add
Balance validation before withdrawal

Account update/edit feature

Password/PIN security

Interest calculation for savings accounts

GUI using Tkinter or PyQt

Convert to a database system (e.g., SQLite or MySQL)
