#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (c) 2018 Maarten Los
# See LICENSE.rst for details.

import json
import socket
import base64

from inbus.shared.opcode import Opcode
from inbus.shared.defaults import Defaults


class Publisher(object):
    """
    Publishes messages to Inbus
    """
    def __init__(self, app_key, server_address=Defaults.INBUS_ADDRESS):
        self._app_key = app_key
        self._server_address = server_address

    
    """
    Publishes a message to Inbus. 
    
    :param payload: the payload of the message. It will be encoded
        to base64 before sending it to Inbus
    :app_type: the application type
    """
    def publish(self, payload, app_type=0):
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.sendto(self._to_outgoing_message(payload, app_type),
                    self._server_address)
        sock.close()

    def _to_outgoing_message(self, payload, app_type):
        return json.dumps({'version': Defaults.INBUS_VERSION,
                           'opcode': Opcode.PUBLISH,
                           'application': [self._app_key, app_type],
                           'address': ['', 0],
                           'payload': base64.b64encode(payload)})
