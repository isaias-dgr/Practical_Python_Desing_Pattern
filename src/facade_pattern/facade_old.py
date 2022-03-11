from datetime import datetime
import random

from pydantic import parse_obj_as


class Invoice:

    def __init__(self, customer):
        self.timesstamp = datetime.now()
        self.number = self.generate_number()
        self.lines = []
        self.total = 0
        self.tax = 0
        self.customer = customer

    def save(self):
        pass

    def send_to_printer(self):
        pass

    def add_lines(self, invoice_line):
        self.lines.append(invoice_line)
        self.calculate()

    def remove_line(self, line_item):
        try:
            self.lines.remove(line_item)
        except:
            print(
                f"could not remove {line_item} because there is no such item in the invoice")

    def calculate(self):
        self.total = sum(x.total * x.amount for x in self.lines)
        self.tax = sum(x.total * x.tax_rate for x in self.lines)

    def generated_number(self):
        rand = random.randint(1, 1000)
        return f"{self.timesstamp}{rand}"


class InvoiceLine:

    def __init__(self, line_item):
        pass

    def save(self):
        pass


class Receipt:

    def __init__(self, invoice, payment_type):
        self.invoice = invoice
        self.customer = invoice.customer
        self.payment_type = payment_type
        pass

    def save(self):
        pass


class Item:

    def __init__(self):
        pass

    @classmethod
    def fetch(cls, item_barcode):
        pass

    def save(self):
        pass


class Customer:

    def __init__(self) -> None:
        pass

    @classmethod
    def fetch(cls, customer_code):
        pass

    def save(self):
        pass


class LoyalityAccount:

    def __init__(self):
        pass

    @classmethod
    def fetch(cls, customer):
        pass

    def calculate(self, invoice):
        pass

    def save(self):
        pass


def complex_sale_processor(customer_code, item_dict_list, payment_type):
    customer = Customer.fetch_customer(customer_code)
    invoice = Invoice

    for item_dict in item_dict_list:
        item = Item.fetch(item_dict.get("barcode"))
        item.amount_in_stock - item_dict.get("amount_purchased")
        item.save()

        invoice_line = InvoiceLine(item)
        invoice.add_line(invoice_line)

    invoice.calculate()
    invoice.save()

    loyalty_account = LoyalityAccount.fetch(customer)
    loyalty_account.calculate(invoice)
    loyalty_account.save()

    receipt = Receipt(invoice, payment_type)


def nice_sales_processor(customer_code, item_dict_list, payment_type):
    invoice = SomeInvoiceClass(customer_code)

    for item_dict in item_dict_list:
        invoice.add_item(item_dict.get("barcode"),
                         item_dict_list.get("amount_purchased"))

    invoice.finalize()
    invoice.generate_receipt(payment_type)
