#!/usr/bin/python3
"""unittesting module
"""
import os
import sys
import unittest
import datetime
import cmd
from models.base_model import BaseModel
from console import HBNBCommand
from io import StringIO


class testconsole(unittest.TestCase):
    """class unittesting console
    """

    def crt(self):
        """create module
        """

        out_back = sys.stdout
        sys.out = StringIO

        HBNBCommand.onecmd("create")

        out = sys.stdout.getvalue()
        sys.stdout.close(); sys.stdout = out_back

        self.assertIn("BaseModel", out)

        self.assertIn(" ", out)

    def T_quite(self):
        """testing quite method
        """
        self.assertTrue("quite", HBNBCommand.do_quit)

if __name__ == '__name__':
    unittest.main()