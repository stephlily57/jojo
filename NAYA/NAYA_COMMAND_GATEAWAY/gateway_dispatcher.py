# gateway_dispatcher.py

from NAYA_INTERFACE.bus.command_bus import CommandBus

command_bus = CommandBus()


def dispatch_to_core(intent):

    command_bus.emit({
        "intent_id": intent.intent_id,
        "category": intent.category,
        "action": intent.action,
        "target": intent.target,
        "context": intent.context
    })
