#!/usr/bin/env python

# Copy avid interplay log to network location with a unique name.
# Hens Zimmerman, February 04, 2017.
# Daily at midnight via cron.
# 0 0 * * * /home/henszimmerman/Desktop/xfer.py &> /dev/null

import errno
import os
import shutil
import uuid

# Source:
# /var/log/avid/avid-interplay-central/interplay_central_0.log

source = "/var/log/avid/avid-interplay-central/interplay_central_0.log"

# Do we have a log file to copy at all?

if not os.path.isfile(source):
    exit

# Destination:
# /home/henszimmerman/Desktop/Parallels Shared Folders/440Hz/make/Python/Facility/files/
# NB: Must end with path delimiter.

destination = "/home/henszimmerman/Desktop/Parallels Shared Folders/440Hz/make/Python/Facility/files/"

# Make sure destination directory exists.

try:
    os.makedirs(destination)
except OSError:
    pass

# Copy file to new unique name.

unique = uuid.uuid1()

shutil.copy2(source, destination + str(unique) + ".log")

