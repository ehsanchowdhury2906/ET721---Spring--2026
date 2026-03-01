"""
Ehsan chowdhury,
lab 9, unit testing
feb 28, 2026
"""

import unittest
from bankaccount import *


class TestBankAccount(unittest.TestCase):

       # 1 
    def setUp(self):
        self.account = BankAccount(owner="John Doe", balance=1000)

       #  2
    def test_initial_balance(self):
        self.assertEqual(self.account.get_balance(), 1000)

       #  3
    def test_deposit(self):
        self.account.deposit(500)
        self.assertEqual(self.account.get_balance(), 1500)

       #  4
    def test_withdrawal(self):
        self.account.withdraw(200)
        self.assertEqual(self.account.get_balance(), 800)
       
       #  5
    def test_withdrawal_insufficient_funds(self):
        with self.assertRaises(ValueError):
            self.account.withdraw(9999)
     
       #  6
    def test_sequence_of_deposits_and_withdrawals(self):
        self.account.deposit(500)    # 1000 + 500 = 1500
        self.account.withdraw(200)   # 1500 - 200 = 1300
        self.account.deposit(100)    # 1300 + 100 = 1400
        self.account.withdraw(400)   # 1400 - 400 = 1000
        self.assertEqual(self.account.get_balance(), 1000)


if __name__ == "__main__":
    unittest.main()