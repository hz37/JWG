#!/usr/bin/python

# Erase old security cam photos from xs4all ftp account.
# This file is running in Linino linux on Gloria's LED clock
# via cron with built-in Python.
# Hens Zimmerman, 27-1-2015.
# Now for two cameras! 03-02-2015
# Now running on godaddy cron. 20-11-2015
# 01-07-2017: switching storage from xs4all to godaddy
# busy writing MPP402. Oh my...
# 12-05-2018: Now direct access to filesystem. Awaiting final grade.

from datetime import date
import os
import re
import shutil

def DeleteOldPhotos(camera, delta, now):
  for dirname, dirnames, filenames in os.walk('/home/hz37/' + camera):
    for subdirname in dirnames:
      m = re.match('(\d{4})(\d{2})(\d{2})', subdirname)
      d = date(int(m.group(1)), int(m.group(2)), int(m.group(3)))
      if (now - d).days > delta:
        shutil.rmtree(os.path.join(dirname, subdirname), ignore_errors=True, onerror=None)

# Anything older than n_days will be deleted.
n_days = 31

# Get date of today.
today = date.today()

DeleteOldPhotos('cam1', n_days, today)
DeleteOldPhotos('cam2', n_days, today)
