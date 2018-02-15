#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (c) 2018 Maarten Los
# See LICENSE.rst for details.

from inbus.client.subscriber import Subscriber
from inbus.shared.opcode import Opcode

is_running = True

with Subscriber("super-app") as s:
    while is_running:
        try:
            payload = s.get_published_message()
            if not payload:
                print "Unknown content"
            else:
                print payload
        except KeyboardInterrupt:
            print "AA"
            is_running = False
