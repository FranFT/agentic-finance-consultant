from datetime import datetime
from pydantic import BaseModel

class Invoice(BaseModel):
    """Invoice information"""
    vendor_name: str
    invoice_number: int
    invoice_date: datetime.date
    due_date: datetime.date
    total_amount: float