import os
from datetime import datetime

os.chdir('/Users/muhammedabdulquadirowais/Desktop/')

mod_tm = os.stat('owai.pdf').st_mtime

print(datetime.fromtimestamp(mod_tm),  '   '  , 1554954067)

print('  ')
print(os.stat('owai.pdf'))