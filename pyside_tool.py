#!/usr/bin/env python
# -*- coding: utf-8 -*-
#############################################################################
##
## Copyright (C) 2018 The Qt Company Ltd.
## Contact: https://www.qt.io/licensing/
##
## This file is part of Qt for Python.
##
## $QT_BEGIN_LICENSE:LGPL$
## Commercial License Usage
## Licensees holding valid commercial Qt licenses may use this file in
## accordance with the commercial license agreement provided with the
## Software or, alternatively, in accordance with the terms contained in
## a written agreement between you and The Qt Company. For licensing terms
## and conditions see https://www.qt.io/terms-conditions. For further
## information use the contact form at https://www.qt.io/contact-us.
##
## GNU Lesser General Public License Usage
## Alternatively, this file may be used under the terms of the GNU Lesser
## General Public License version 3 as published by the Free Software
## Foundation and appearing in the file LICENSE.LGPL3 included in the
## packaging of this file. Please review the following information to
## ensure the GNU Lesser General Public License version 3 requirements
## will be met: https://www.gnu.org/licenses/lgpl-3.0.html.
##
## GNU General Public License Usage
## Alternatively, this file may be used under the terms of the GNU
## General Public License version 2.0 or (at your option) the GNU General
## Public license version 3 or any later version approved by the KDE Free
## Qt Foundation. The licenses are as published by the Free Software
## Foundation and appearing in the file LICENSE.GPL2 and LICENSE.GPL3
## included in the packaging of this file. Please review the following
## information to ensure the GNU General Public License requirements will
## be met: https://www.gnu.org/licenses/gpl-2.0.html and
## https://www.gnu.org/licenses/gpl-3.0.html.
##
## $QT_END_LICENSE$
##
#############################################################################
import sys
import os
import subprocess

from subprocess import Popen, PIPE
import PySide2 as _

def main():
    # This will take care of "pyside2-lupdate" listed as an entrypoint
    # in setup.py are copied to 'scripts/..'
    cmd = os.path.join("..", os.path.basename(sys.argv[0]))
    command = [os.path.join(os.path.dirname(os.path.realpath(__file__)), cmd)]
    command.extend(sys.argv[1:])
    sys.exit(subprocess.call(command))

def qt_tool_wrapper(qt_tool):
    # This will take care of "pyside2-uic" and "pyside2-rcc"
    # listed as an entrypoint in setup.py
    pyside_dir = _.__file__.replace("__init__.py", "")
    exe =  os.path.join(pyside_dir, qt_tool)

    if len(sys.argv) > 1:
        args = " ".join(sys.argv[1:])
        cmd = "{} -g python {}".format(exe, args)
        proc = Popen(cmd.split(), stderr=PIPE)
        out, err = proc.communicate()
        if err:
            msg = err.decode("utf-8")
            print("Error: {}\nwhile executing '{}'".format(msg, cmd))
        sys.exit(proc.returncode)

def uic():
    qt_tool_wrapper("uic")

def rcc():
    qt_tool_wrapper("rcc")


if __name__ == "__main__":
     main()
