#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (c) 2018 Maarten Los
# See LICENSE.rst for details.

import json
import socket

from inbus.shared.opcode import Opcode
from inbus.shared.defaults import Defaults


class Subscriber(object):

    def __init__(self, app_key, client_address=(Defaults.LOCALHOST, 0),
                 server_address=Defaults.INBUS_ADDRESS, buffer_size=65536):
        self._app_key = app_key
        self._client_address = client_address
        self._server_address = server_address
        self._buffer_size = buffer_size
        self._socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self._socket.bind(self._client_address)

    def __enter__(self):
        # Register
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.sendto(self._to_outgoing_message(Opcode.SUBSCRIBE),
                    self._server_address)
        sock.close()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        # Deregister
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.sendto(self._to_outgoing_message(Opcode.UNSUBSCRIBE),
                    self._server_address)
        sock.close()

    def _to_outgoing_message(self, opcode):
        return json.dumps({'version': 1,
                           'opcode': opcode,
                           'application': [self._app_key, 0],
                           'address': list(self._socket.getsockname()),
                           'payload': ''})

    def get_published_message(self):
        """
        Listens for published messages
        :returns: A tuple (payload, applicationType)
        :raises RuntimeError: if the message cannot be decoded correctly
        """
        data, addr = self._socket.recvfrom(self._buffer_size)
        try:
            message = json.loads(data)
        except ValueError:
            return (None, None)

        try:
            payload = message["payload"]
            application = message["application"]
            applicationType = application[1]
        except KeyError:
            raise RuntimeError

        return payload, applicationType
