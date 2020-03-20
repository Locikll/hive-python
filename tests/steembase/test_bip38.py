import unittest
import os
import sys
from hivebase.account import PrivateKey
import hivebase.bip38


class Testcases(unittest.TestCase):
    def test_encrypt(self):
        self.assertEqual([
            format(
                hivebase.bip38.encrypt(
                    PrivateKey(
                        "5HqUkGuo62BfcJU5vNhTXKJRXuUi9QSE6jp8C3uBJ2BVHtB8WSd"),
                    "TestingOneTwoThree"), "encwif"),
            format(
                hivebase.bip38.encrypt(
                    PrivateKey(
                        "5KN7MzqK5wt2TP1fQCYyHBtDrXdJuXbUzm4A9rKAteGu3Qi5CVR"),
                    "TestingOneTwoThree"), "encwif"),
            format(
                hivebase.bip38.encrypt(
                    PrivateKey(
                        "5HtasZ6ofTHP6HCwTqTkLDuLQisYPah7aUnSKfC7h4hMUVw2gi5"),
                    "Satoshi"), "encwif")
        ], [
            "6PRN5mjUTtud6fUXbJXezfn6oABoSr6GSLjMbrGXRZxSUcxThxsUW8epQi",
            "6PRVWUbkzzsbcVac2qwfssoUJAN1Xhrg6bNk8J7Nzm5H7kxEbn2Nh2ZoGg",
            "6PRNFFkZc2NZ6dJqFfhRoFNMR9Lnyj7dYGrzdgXXVMXcxoKTePPX1dWByq"
        ])

    def test_decrypt(self):
        self.assertEqual([
            format(
                hivebase.bip38.decrypt(
                    "6PRN5mjUTtud6fUXbJXezfn6oABoSr6GSLjMbrGXRZxSUcxTh"
                    "xsUW8epQi", "TestingOneTwoThree"), "wif"),
            format(
                hivebase.bip38.decrypt(
                    "6PRVWUbkzzsbcVac2qwfssoUJAN1Xhrg6bNk8J7Nzm5H7kxEb"
                    "n2Nh2ZoGg", "TestingOneTwoThree"), "wif"),
            format(
                hivebase.bip38.decrypt(
                    "6PRNFFkZc2NZ6dJqFfhRoFNMR9Lnyj7dYGrzdgXXVMXcxoKTe"
                    "PPX1dWByq", "Satoshi"), "wif")
        ], [
            "5HqUkGuo62BfcJU5vNhTXKJRXuUi9QSE6jp8C3uBJ2BVHtB8WSd",
            "5KN7MzqK5wt2TP1fQCYyHBtDrXdJuXbUzm4A9rKAteGu3Qi5CVR",
            "5HtasZ6ofTHP6HCwTqTkLDuLQisYPah7aUnSKfC7h4hMUVw2gi5"
        ])


if __name__ == '__main__':
    unittest.main()