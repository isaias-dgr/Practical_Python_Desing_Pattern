import statistics


class Invoice:
    def __init__(self) -> None:
        pass


class InvoiceLine:
    def __init__(self) -> None:
        pass


class Customer:
    def __init__(self) -> None:
        pass


class Item:
    def __init__(self) -> None:
        pass


class Receipt:
    def __init__(self) -> None:
        pass


class LoyaltyAccount:
    def __init__(self) -> None:
        pass


class Sale:

    def __init__(self) -> None:
        pass

    @staticmethod
    def make_invoice(customer): return Invoice(customer)

    @staticmethod
    def make_customer(customer_id): return Customer(customer_id)

    @staticmethod
    def make_item(item_barcode): return Item(item_barcode)

    @staticmethod
    def make_invoice_line(item): return InvoiceLine(item)

    @staticmethod
    def make_receipt(invoice, payment_type):
        return Receipt(invoice, payment_type)

    @staticmethod
    def make_loyality_account(customer):
        return LoyaltyAccount(customer)

    @staticmethod
    def fetch_invoice(customer_id): return Invoice(customer_id)

    @staticmethod
    def fetch_customer(customer_id): return Customer(customer_id)

    @staticmethod
    def fetch_item(item_barcode): return Item(item_barcode)

    @staticmethod
    def fetch_invoice_line(line_item_id): return InvoiceLine(line_item_id)

    @staticmethod
    def make_loyality_account(customer_id):
        return LoyaltyAccount(customer_id)

    @staticmethod
    def make_reciept(invoice_id):
        return Receipt(invoice_id)

    @staticmethod
    def add_item(invoice, item_barcode, amount_purchased):
        item = Item.fetch(item_barcode)
        item.amount_in_stock - amount_purchased
        item.save()
        invoice_line = InvoiceLine.make(item)
        invoice.add_line(invoice_line)

    @staticmethod
    def finalize(invoice):
        invoice.calculate()
        invoice.save()

        loyalt_account = LoyaltyAccount.fetch(invoice.customer)
        loyalt_account.calculate(invoice)
        loyalt_account.save()

    @staticmethod
    def generate_receipt(invoice, payment_type):
        receipt = Receipt(invoice, payment_type)
        receipt.save()


def nice_sales_processor(customer_id,  item_dict_list, payment_type):
    invoice = Sale.make_invoice(customer_id)

    for item_dict in item_dict_list:
        Sale.add_item(invoice, item_dict.get("barcode"),
                      item_dict_list.get("amount_purchased"))

    Sale.finalize(invoice)
    Sale.generate_receip(invoice, payment_type)
