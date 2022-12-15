public class Machine {
    final static int SOLD_OUT = 0;
    final static int NO_COIN = 1;
    final static int COIN = 2;

    public int state = NO_COIN;

    public void insertCoin() {
        if (state == NO_COIN) {

        } else if (state == COIN) {

        }
    }

    public void returnCoin() {
        if (state == NO_COIN) {

        } else if (state == COIN) {

        }
    }

    public void pushItem() {
        if (state == NO_COIN) {

        } else if (state == COIN) {

        } else if (state == SOLD_OUT) {

        }
    }
}
