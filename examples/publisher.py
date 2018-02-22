#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (c) 2018 Maarten Los
# See LICENSE.rst for details.

import sys

from inbus.client.publisher import Publisher

if len(sys.argv) < 3:
    print "Usage: " + sys.argv[0] + " <message> <app-name> [<app-type>]"
    sys.exit(1)


appType = 0
if len(sys.argv) == 4:
    appType = int(sys.argv[3])

appName = sys.argv[2]
message = sys.argv[1]

p = Publisher(appName)

p.publish(message, appType)
