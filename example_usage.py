from client import SubsumptionArbiter

def main():
    arb = SubsumptionArbiter()
    arb.add_layer(0, "cruise", lambda s: "drive_straight")
    arb.add_layer(5, "avoid_collision", lambda s: "emergency_brake" if s.get("proximity_cm", 100) < 20 else None)
    res = arb.arbitrate({"proximity_cm": 15})
    print("Subsumption Architecture Verification:")
    print(f"Layer: {res['active_layer']}")
    print(f"Action: {res['action']} (Expected: emergency_brake)")

if __name__ == "__main__":
    main()
