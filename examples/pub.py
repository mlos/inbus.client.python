#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (c) 2018 Maarten Los
# See LICENSE.rst for details.

from inbus.client.publisher import Publisher

p = Publisher("super-app")
p.publish("xx")
