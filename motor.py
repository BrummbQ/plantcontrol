#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from RPIO import PWM

from SimpleXMLRPCServer import SimpleXMLRPCServer
from SimpleXMLRPCServer import SimpleXMLRPCRequestHandler


class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)


class Control:
    def __init__(self):
        self.servo = PWM.Servo()

    def set_rate(self, rate, pin):
        self.servo.set_servo(pin, rate)


if __name__ == "__main__":
    # Create server
    server = SimpleXMLRPCServer(("", 1337),
                                requestHandler=RequestHandler, allow_none=True)
    server.register_introspection_functions()
    server.register_instance(Control())
    server.serve_forever()