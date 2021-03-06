#!/usr/bin/env python

# Copyright (c) Microsoft. All rights reserved.
# Licensed under the MIT license. See LICENSE file in the project root for
# full license information.
from azure.iot.device import IoTHubModuleClient
from azure.iot.device import auth
import json


def normalize_event_body(body):
    if isinstance(body, bytes):
        return body.decode("utf-8")
    else:
        return json.dumps(body)


def message_to_object(message):
    return json.loads(message.data.decode("utf-8"))


class InternalModuleGlueSync:
    def __init__(self):
        self.client = None

    def connect_from_environment(self, transport_type):
        print("connecting from environment")
        auth_provider = auth.from_environment()
        self.client = IoTHubModuleClient.from_authentication_provider(
            auth_provider, transport_type
        )
        self.client.connect()

    def connect(self, transport_type, connection_string, cert):
        print("connecting using " + transport_type)
        auth_provider = auth.from_connection_string(connection_string)
        if "GatewayHostName" in connection_string:
            auth_provider.ca_cert = cert
        self.client = IoTHubModuleClient.from_authentication_provider(
            auth_provider, transport_type
        )
        self.client.connect()

    def disconnect(self):
        print("disconnecting")
        if self.client:
            self.client.disconnect()
            self.client = None

    def enable_input_messages(self):
        pass

    def enable_methods(self):
        raise NotImplementedError()

    def enable_twin(self):
        raise NotImplementedError()

    def send_event(self, event_body):
        print("sending event")
        self.client.send_event(normalize_event_body(event_body))
        print("send confirmation received")

    def wait_for_input_message(self, input_name):
        print("Waiting for input message")
        message = self.client.receive_input_message(input_name)
        print("Message received")
        return message_to_object(message)

    def invoke_module_method(self, device_id, module_id, method_invoke_parameters):
        raise NotImplementedError()

    def invoke_device_method(self, device_id, method_invoke_parameters):
        raise NotImplementedError()

    def roundtrip_method_call(self, methodName, requestAndResponse):
        raise NotImplementedError()

    def send_output_event(self, output_name, event_body):
        print("sending output event")
        self.client.send_to_output(normalize_event_body(event_body), output_name)
        print("send confirmation received")

    def wait_for_desired_property_patch(self):
        raise NotImplementedError()

    def get_twin(self):
        raise NotImplementedError()

    def send_twin_patch(self, props):
        raise NotImplementedError()
