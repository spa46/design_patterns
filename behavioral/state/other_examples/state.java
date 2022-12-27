public interface State {
    void insertCoin(MachineContext machineContext);
    void returnCoin(MachineContext machineContext);
    void pushItem();
    String getState();
}

public class MachineContext {
    private State state;

    public MachineContext() {
        state = new NoCoinState();
    }

    public void setState(State state) {
        this.state = state;
    }

    public String getState() {
        return this.state.getState();
    }

    public void insertCoin() {
        this.state.insertCoin(this);
    }

    public void returnCoin() {
        this.state.returnCoin(this);
    }
}

public class CoinState implements State {
    @Override
    public void insertCoin(MachineContext machineContext) {
        machineContext.setState(this);
        System.out.println("코인 입력됨");
    }

    @Override
    public void returnCoin(MachineContext machineContext) {
        machineContext.setState(new NoCoinState());
        System.out.println("코인 반환");
    }

    @Override
    public void pushItem() {

    }

    public String getState() {
        return "코인있음";
    }
}

public class NoCoinState implements State {
    @Override
    public void insertCoin(MachineContext machineContext) {
        machineContext.setState(new CoinState());
        System.out.println("코인 입력됨");
    }

    @Override
    public void returnCoin(MachineContext machineContext) {
        System.out.println("코인이 없어요");
    }

    @Override
    public void pushItem() {
        System.out.println("");
    }

    public String getState() {
        return "코인없음";
    }
}

MachineContext machineContext = new MachineContext();

machineContext.insertCoin();
System.out.println(machineContext.getState());

machineContext.returnCoin();
machineContext.returnCoin();
System.out.println(machineContext.getState());

// 코인 입력됨
// 코인있음
// 코인 반환
// 코인이 없어요
// 코인없음
