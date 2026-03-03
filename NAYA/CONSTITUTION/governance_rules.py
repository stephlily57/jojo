class GovernanceRules:
    CORE_IS_STRATEGIC_AUTHORITY = True
    REAPERS_IS_SECURITY_AUTHORITY = True
    THREE_SCENARIOS_REQUIRED = True
    SHI_IS_INDICATIVE_ONLY = True

    @classmethod
    def validate(cls):
        if not cls.REAPERS_IS_SECURITY_AUTHORITY:
            raise Exception("Reapers must remain security authority.")
        return True
