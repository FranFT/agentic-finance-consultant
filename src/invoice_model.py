from datetime import date
from typing import List
from pydantic import BaseModel, Field, PositiveInt

class LineItem(BaseModel):
    """
    Defining individual line items.
    """
    description: str = Field(..., description="Description of the product or service.")
    quantity: PositiveInt = Field(..., description="Number of items.")
    unit_price: float = Field(..., description="Price per single unit")
    total: float = Field(..., description="Total amount for this line item.")

class Invoice(BaseModel):
    """
    Defining main invoice model
    """
    vendor_name: str
    invoice_number: int
    invoice_date: date
    line_items: List[LineItem] = Field(..., description="List of line items in the invoice.")

    # Calculate total amount automatically.
    @property
    def total_amount(self) -> float:
        return sum(item.total for item in self.line_items)