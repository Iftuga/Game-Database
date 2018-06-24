#!/usr/bin/python
# -*- coding: utf-8 -*-

from importlib.machinery import SourceFileLoader
import os
path = os.path.abspath("main.py")
display = SourceFileLoader("display.py", path [:-7]+"scripts/display.py").load_module()
display.display()
