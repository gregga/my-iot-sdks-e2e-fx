import connexion
import six

from swagger_server.models.certificate import Certificate  # noqa: E501
from swagger_server.models.connect_response import ConnectResponse  # noqa: E501
from swagger_server.models.roundtrip_method_call_body import RoundtripMethodCallBody  # noqa: E501
from swagger_server import util

from swagger_server.module_glue import ModuleGlue
module_glue = ModuleGlue()

def module_connect_from_environment_transport_type_put(transportType):  # noqa: E501
    """Connect to the azure IoT Hub as a module using the environment variables

     # noqa: E501

    :param transportType: Transport to use
    :type transportType: str

    :rtype: ConnectResponse
    """
    return module_glue.connect_from_environment(transportType)

def module_connect_transport_type_put(transportType, connectionString, caCertificate=None):  # noqa: E501
    """Connect to the azure IoT Hub as a module

     # noqa: E501

    :param transportType: Transport to use
    :type transportType: str
    :param connectionString: connection string
    :type connectionString: str
    :param caCertificate:
    :type caCertificate: dict | bytes

    :rtype: ConnectResponse
    """
    if connexion.request.is_json:
        caCertificate = Certificate.from_dict(connexion.request.get_json())  # noqa: E501
    return module_glue.connect(transportType, connectionString, caCertificate)


def module_connection_id_device_method_device_id_put(connectionId, deviceId, methodInvokeParameters):  # noqa: E501
    """call the given method on the given device

     # noqa: E501

    :param connectionId: Id for the connection
    :type connectionId: str
    :param deviceId:
    :type deviceId: str
    :param methodInvokeParameters:
    :type methodInvokeParameters:

    :rtype: object
    """
    return module_glue.invoke_device_method(connectionId, deviceId, methodInvokeParameters)


def module_connection_id_disconnect_put(connectionId):  # noqa: E501
    """Disconnect the module

    Disconnects from Azure IoTHub service.  More specifically, closes all connections and cleans up all resources for the active connection # noqa: E501

    :param connectionId: Id for the connection
    :type connectionId: str

    :rtype: None
    """
    module_glue.disconnect(connectionId)


def module_connection_id_enable_input_messages_put(connectionId):  # noqa: E501
    """Enable input messages

     # noqa: E501

    :param connectionId: Id for the connection
    :type connectionId: str

    :rtype: None
    """
    module_glue.enable_input_messages(connectionId)


def module_connection_id_enable_methods_put(connectionId):  # noqa: E501
    """Enable methods

     # noqa: E501

    :param connectionId: Id for the connection
    :type connectionId: str

    :rtype: None
    """
    module_glue.enable_methods(connectionId)


def module_connection_id_enable_twin_put(connectionId):  # noqa: E501
    """Enable module twins

     # noqa: E501

    :param connectionId: Id for the connection
    :type connectionId: str

    :rtype: None
    """
    module_glue.enable_twin(connectionId)


def module_connection_id_event_put(connectionId, eventBody):  # noqa: E501
    """Send an event

     # noqa: E501

    :param connectionId: Id for the connection
    :type connectionId: str
    :param eventBody:
    :type eventBody: str

    :rtype: None
    """
    module_glue.send_event(connectionId, eventBody)


def module_connection_id_input_message_input_name_get(connectionId, inputName):  # noqa: E501
    """Wait for a message on a module input

     # noqa: E501

    :param connectionId: Id for the connection
    :type connectionId: str
    :param inputName:
    :type inputName: str

    :rtype: str
    """
    return module_glue.wait_for_input_message(connectionId, inputName)


def module_connection_id_module_method_device_id_module_id_put(connectionId, deviceId, moduleId, methodInvokeParameters):  # noqa: E501
    """call the given method on the given module

     # noqa: E501

    :param connectionId: Id for the connection
    :type connectionId: str
    :param deviceId:
    :type deviceId: str
    :param moduleId:
    :type moduleId: str
    :param methodInvokeParameters:
    :type methodInvokeParameters:

    :rtype: object
    """
    return module_glue.invoke_module_method(connectionId, deviceId, moduleId, methodInvokeParameters)


def module_connection_id_output_event_output_name_put(connectionId, outputName, eventBody):  # noqa: E501
    """Send an event to a module output

     # noqa: E501

    :param connectionId: Id for the connection
    :type connectionId: str
    :param outputName:
    :type outputName: str
    :param eventBody:
    :type eventBody: str

    :rtype: None
    """
    module_glue.send_output_event(connectionId, outputName, eventBody)


def module_connection_id_roundtrip_method_call_method_name_put(connectionId, methodName, requestAndResponse):  # noqa: E501
    """Wait for a method call, verify the request, and return the response.

    This is a workaround to deal with SDKs that only have method call operations that are sync.  This function responds to the method with the payload of this function, and then returns the method parameters.  Real-world implemenatations would never do this, but this is the only same way to write our test code right now (because the method handlers for C, Java, and probably Python all return the method response instead of supporting an async method call) # noqa: E501

    :param connectionId: Id for the connection
    :type connectionId: str
    :param methodName: name of the method to handle
    :type methodName: str
    :param requestAndResponse:
    :type requestAndResponse: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        requestAndResponse = RoundtripMethodCallBody.from_dict(connexion.request.get_json())  # noqa: E501
    return module_glue.roundtrip_method_call(connectionId, methodName, requestAndResponse)


def module_connection_id_twin_desired_prop_patch_get(connectionId):  # noqa: E501
    """Wait for the next desired property patch

     # noqa: E501

    :param connectionId: Id for the connection
    :type connectionId: str

    :rtype: object
    """
    return module_glue.wait_for_desired_property_patch(connectionId)


def module_connection_id_twin_get(connectionId):  # noqa: E501
    """Get the device twin

     # noqa: E501

    :param connectionId: Id for the connection
    :type connectionId: str

    :rtype: object
    """
    return module_glue.get_twin(connectionId)


def module_connection_id_twin_patch(connectionId, props):  # noqa: E501
    """Updates the device twin

     # noqa: E501

    :param connectionId: Id for the connection
    :type connectionId: str
    :param props:
    :type props:

    :rtype: None
    """
    return  module_glue.send_twin_patch(connectionId, props)
