"""Brooks' Subsumption Architecture Behavior Arbiter
100% Python Standard Library.
"""

class SubsumptionArbiter:
    """Layered behavior arbitration with priority override."""
    def __init__(self):
        self.layers = []

    def add_layer(self, priority, name, eval_fn):
        self.layers.append((priority, name, eval_fn))
        self.layers.sort(key=lambda x: x[0], reverse=True)

    def arbitrate(self, sensors):
        for priority, name, eval_fn in self.layers:
            action = eval_fn(sensors)
            if action is not None:
                return {
                    "active_layer": name,
                    "priority": priority,
                    "action": action
                }
        return {"active_layer": "default", "priority": -1, "action": "idle"}
