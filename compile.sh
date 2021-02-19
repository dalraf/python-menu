#!/bin/bash
docker run -v "$(pwd):/src/" cdrx/pyinstaller-windows "pyinstaller --onefile python-menu.py"
