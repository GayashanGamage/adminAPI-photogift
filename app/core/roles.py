from enum import Enum

class Role(str, Enum):
    ADMIN = "admin"
    CUSTOMER_SUPPORT = "customer_support"
    DESIGNER = "designer"
    AFFILIATE = "affiliate"