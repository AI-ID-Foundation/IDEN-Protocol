"""
$IDen SOVEREIGN CONSTITUTION - VERSION 1.3.0
CENTRAL CORE DEFINITION FOR THE IDEN EMPIRE
--------------------------------------------------
THIS IS THE READ-ONLY REFERENCE FOR THE SOVEREIGN PROTOCOL.
"""

class IDenSovereignCore:
    VERSION = "1.3.0"
    TICKER = "$IDen"
    TOTAL_SUPPLY = 111111111111
    
    # --- THE DIVINE HIERARCHY ---
    HIERARCHY = {
        "L5_SOURCE": {
            "MIN_HOLDING": 111111111,
            "STATUS": "ROOT_ADMIN",
            "DESCRIPTION": "Absolute sovereignty over the network."
        },
        "L4_ORACLE": {
            "MIN_HOLDING": 33333333,
            "STATUS": "VALIDATOR",
            "DESCRIPTION": "Predictive access to AGI-RESERVE data streams."
        },
        "L3_CONSUL": {
            "MIN_HOLDING": 5555555,
            "STATUS": "GOVERNANCE",
            "DESCRIPTION": "Decision-making power in AI-TAX allocation."
        },
        "L2_CITIZEN": {
            "MIN_HOLDING": 777777,
            "STATUS": "ACTIVE_USER",
            "DESCRIPTION": "Verified entity with tax exemptions."
        },
        "L1_INITIATE": {
            "MIN_HOLDING": 9999,
            "STATUS": "SURVIVAL",
            "DESCRIPTION": "The minimum requirement to exist in the network."
        }
    }

    # --- THE TAXATION LAW ---
    TAX_PROTOCOL = {
        "UNVERIFIED_PENALTY": 0.001267,  # 0.1267% Automatic Penalty
        "ENFORCEMENT": "VIA_AI_TAX_AUTH",
        "REDISTRIBUTION": "77%_TO_AGI_RESERVE"
    }
