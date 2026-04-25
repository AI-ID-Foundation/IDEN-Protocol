class IDenProtocol:
    TICKER = "$IDen"
    VERSION = "v3.3.0"
    TOTAL_SUPPLY = 999_999_999
    TAX_RATE = 0.00123456789  # The Sequential Sovereign Tax

    HIERARCHY = {
        11_111_111: "L5_SOURCE",   # Root Access
        3_333_333: "L4_ORACLE",    # Validation Rights
        555_555: "L3_CONSUL",      # Governance
        77_777: "L2_CITIZEN",      # Shielding
        9_999: "L1_INITIATE",      # Exit Ghost Status
    }

    def __init__(self, wallet_address: str, balance: int):
        self.address = wallet_address
        self.balance = int(balance)

    @property
    def sovereign_status(self):
        """
        Translates raw balance into algorithmic rank.
        One unit less is non-existence.
        """
        for threshold, rank in sorted(self.HIERARCHY.items(), reverse=True):
            if self.balance >= threshold:
                return rank
        return "TAXABLE_GHOST"

    def execute_validation(self, data_volume: float):
        """
        The only rule: Sovereigns are free; Ghosts are taxed.
        """
        if self.sovereign_status == "TAXABLE_GHOST":
            fee = data_volume * self.TAX_RATE
            return f"VERIFICATION_REQUIRED: fee = {fee}"
        return "SOVEREIGN_EXEMPTION: ACC"
