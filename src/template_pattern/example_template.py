from abc import ABCMeta, abstractmethod


class ThirdPartyInteractionTemplate(metaclass=ABCMeta):

    def sync_stock_items(self):
        self._sync_stock_items_step_1()
        self._sync_stock_items_step_2()
        self._sync_stock_items_step_3()
        self._sync_stock_items_step_4()

    def send_transaction(self, transaction):
        self._send_transaction(transaction)

    @abstractmethod
    def _sync_stock_items_step_1(self): pass

    @abstractmethod
    def _sync_stock_items_step_2(self): pass

    @abstractmethod
    def _sync_stock_items_step_3(self): pass

    @abstractmethod
    def _sync_stock_items_step_4(self): pass

    def _send_transaction(self, transaction): pass


class System1(ThirdPartyInteractionTemplate):

    def _sync_stock_items_step_1(self):
        print("running stock sync between local and remote system 1")

    def _sync_stock_items_step_2(self):
        print("retrieving remote stock items from system 1")

    def _sync_stock_items_step_3(self):
        print("updating local items")

    def _sync_stock_items_step_4(self):
        print("sendimg updates to third party system 1")

    def _send_transaction(self, transaction):
        print(f"send transaction to system 1 {transaction}")


class System2(ThirdPartyInteractionTemplate):

    def _sync_stock_items_step_1(self):
        print("running stock sync between local and remote system 2")

    def _sync_stock_items_step_2(self):
        print("retrieving remote stock items from system 2")

    def _sync_stock_items_step_3(self):
        print("updating local items")

    def _sync_stock_items_step_4(self):
        print("sendimg updates to third party system 2")

    def _send_transaction(self, transaction):
        print(f"send transaction to system 2 {transaction}")


class System3(ThirdPartyInteractionTemplate):

    def _sync_stock_items_step_1(self):
        print("running stock sync between local and remote system 3")

    def _sync_stock_items_step_2(self):
        print("retrieving remote stock items from system 3")

    def _sync_stock_items_step_3(self):
        print("updating local items")

    def _sync_stock_items_step_4(self):
        print("sendimg updates to third party system 3")

    def _send_transaction(self, transaction):
        print(f"send transaction to system 3 {transaction}")


def main():

    transaction = {
        "id": 1,
        "items": [
            {
                "item_id": 1,
                "amount_purchased": 3,
                "value": 238
            }
        ]
    }

    for C in [System1, System2, System3]:
        print("="*10)
        system = C()
        system.sync_stock_items()
        system.send_transaction(transaction)


if __name__ == "__main__":
    main()
