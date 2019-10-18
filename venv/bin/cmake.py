#!/home/buse/PycharmProjects/projeDeneme/venv/bin/python
# EASY-INSTALL-ENTRY-SCRIPT: 'CmakePy==0.1.2','console_scripts','cmake.py'
__requires__ = 'CmakePy==0.1.2'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('CmakePy==0.1.2', 'console_scripts', 'cmake.py')()
    )
