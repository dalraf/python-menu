#!/bin/bash
docker run -v "$(pwd)/src/:/src/" cdrx/pyinstaller-windows "pyinstaller --onefile python-menu.py"
