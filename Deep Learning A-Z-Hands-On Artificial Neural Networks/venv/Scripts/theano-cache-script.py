#!"C:\Users\safar\Documents\GitHub\Safarie1103\Deep Learning A-Z-Hands-On Artificial Neural Networks\venv\Scripts\python.exe"
# EASY-INSTALL-ENTRY-SCRIPT: 'Theano==1.0.4','console_scripts','theano-cache'
__requires__ = 'Theano==1.0.4'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('Theano==1.0.4', 'console_scripts', 'theano-cache')()
    )
