from abc import abstractmethod, ABCMeta
from enum import Enum
from enum import auto

class StateType(str, Enum):
    def _generate_next_value_(name, start, count, last_values):
        return name

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    FOR_SALE = auto()
    SOLD_OUT = auto()

class State(metaclass=ABCMeta):
    @abstractmethod
    def get_state(self):
        pass

    @abstractmethod
    def sale(self, context):
        pass

    @abstractmethod
    def cancel(self, context):
        pass

    @abstractmethod
    def take_back(self, context):
        pass

    @abstractmethod
    def exchange(self, context):
        pass

class StatusContext:
    def __init__(self, item_name, init_qty, sale_qty, state):
        self.__for_sale = ForSale()
        self.__sold_out = SoldOut()
        self.sale_qty = sale_qty
        self.init_qty = init_qty
        self._state = self.__sold_out if state == StateType.SOLD_OUT else self.__for_sale

    def sale(self):
        self._state.sale(self)

    def cancel(self):
        self._state.cancel(self)

    def increase_init_qty(self):
        self.init_qty += self.sale_qty

    def decrease_init_qty(self):
        self.init_qty -= self.sale_qty

    def set_state_sold_out(self):
        self._state = self.__sold_out
        print('품절로 변경')

    def set_state_for_sale(self):
        self._state = self.__for_sale

    @property
    def state(self):
        return self._state.get_state()

class ForSale(State):
    def get_state(self):
        return StateType.FOR_SALE

    def sale(self, context):
        left_qty = context.init_qty - context.sale_qty
        if left_qty < 0:
            raise ValueError('남은 수량보다 판매 수량이 더 많음')

        if left_qty == 0:
            context.set_state_sold_out()
            context.decrease_init_qty()
        else:
            context.decrease_init_qty()

        print('물건 판매됨')

    def cancel(self, context):
        context.set_state_for_sale()
        context.increase_init_qty()

    def take_back(self, quantity):
        pass

    def exchange(self, quantity):
        pass

class SoldOut(State):
    def get_state(self):
        return StateType.SOLD_OUT

    def sale(self, context):
        raise ValueError('품절인 상품은 구매할 수 없음')

    def cancel(self, context):
        context.set_state_for_sale()
        context.increase_init_qty()

    def take_back(self, context):
        pass

    def exchange(self, context):
        pass

item_info = {
    'item_name': '상품1',
    'init_qty': 10,
    'sale_qty': 2,
    'state': StateType.FOR_SALE
}

status_context = StatusContext(**item_info)
status_context.sale()
print(f'남은수량: {status_context.init_qty} 판매상태: {status_context.state}')

# 물건 판매됨
# 남은수량: 8 판매상태: FOR_SALE
