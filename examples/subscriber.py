#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (c) 2018 Maarten Los
# See LICENSE.rst for details.

import sys
from inbus.client.subscriber import Subscriber
isRunning = True

if len(sys.argv) < 2:
    print "Usage: " + sys.argv[0] + " <app-name>"
    sys.exit(1)


with Subscriber(sys.argv[1]) as s:
    while isRunning:
        try:
            payload, applicationType = s.get_published_message()
            print "Received :'" + payload + "' (Type: " + str(applicationType) + ")"
        except RuntimeError:
            print "Error receiving Inbus message"
        except KeyboardInterrupt:
            print "Exiting..."
            isRunning = False
