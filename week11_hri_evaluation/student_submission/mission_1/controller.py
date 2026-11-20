"""Complete decide() using the transition requirements in the Lab 10 guide."""

ACTIVE = ("CLARIFY", "CONFIRM", "EXECUTING", "WAIT_READY")
REQUESTABLE = ("IDLE", "CLARIFY", "CONFIRM", "RECOVERY", "CANCELLED")
CUPS = ("red", "blue")


def decide(state, event):
    phase = state["phase"]
    kind = event["kind"]
    target = event["target"]
    named = target in CUPS

    # Cancellation has priority over every other rule during an active task.
    if kind == "CANCEL":
        if phase in ACTIVE:
            return "cancel"
        return "hold"

    # A new request may only start or replace a task before movement begins.
    if kind == "REQUEST":
        if phase in REQUESTABLE:
            return "select" if named else "clarify"
        return "hold"

    # A correction must name a cup; select stops the old task and clears its confirmation.
    if kind == "CORRECT":
        if phase in ACTIVE and named:
            return "select"
        return "hold"

    if kind == "CONFIRM" and phase == "CONFIRM":
        return "begin"

    # Release only while offering the cup and on a fresh READY event.
    if phase == "WAIT_READY" and kind == "READY":
        return "release"

    if kind == "TIMEOUT" and phase == "WAIT_READY":
        return "timeout"

    if kind == "TICK" and phase == "EXECUTING":
        return "advance"

    return "hold"
