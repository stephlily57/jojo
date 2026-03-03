# bootstrap/gateway_initializer.py

from NAYA_COMMAND_GATEAWAY.gateway import CommandGateway
from NAYA_COMMAND_GATEAWAY.journal import IntentJournal


def initialize_gateway():

    journal = IntentJournal()
    gateway = CommandGateway(journal)

    return gateway
