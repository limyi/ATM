# Simple ATM Program README Instruction

## Overview

This Python program simulates a simple ATM workflow. Users can insert a credit card, enter a 6-digit PIN number, choose an account type (Savings or Checking), and perform basic banking operations like checking the account balance, depositing money, and withdrawing money.

## Requirements

- Python 3.8.10 

## Getting Started

1. Clone or download this repository to your local machine.
     git clone https://github.com/limyi/ATM
   
2. Open a terminal or command prompt.

3. Navigate to the directory where you saved the files.

4. Execute the program by running the main file (`bear_robotics.py.py`) using Python:

   ```bash
   python3 bear_robotics.py

## Using the ATM Program

1. When you run the program, you will be prompted to enter your card number and 6-digit PIN.

2. If the card number and PIN are valid, you will be asked to select an account type (Savings or Checking).

3. Once you've selected your account type, you will be presented with the main menu where you can choose from the following options:

   - **1. See Balance:** View your account balance.
   - **2. Deposit Money:** Deposit money into your account.
   - **3. Withdraw Money:** Withdraw money from your account.
   - **4. Exit:** Exit the ATM program.

4. Follow the on-screen instructions to navigate through the program and perform your desired actions.


## Updating Card Number and PIN

You can update the card number and PIN number by modifying the `valid_card_numbers` and `valid_pins` lists in the `ATM` class. Here's how you can do it:

1. Open the `atm.py` file in a text editor or integrated development environment (IDE).

2. Locate the `is_valid_card` method in the `ATM` class.

3. You will find the following lines of code:

   ```python
   # Replace this with your card validation logic.
   valid_card_numbers = ['1234567890123456', '9876543210987654']
   valid_pins = ['123456', '654321']
