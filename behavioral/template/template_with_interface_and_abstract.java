public interface Flight {
    void checkBaggage();
}

public interface Ticket {
    void checkPassport();
    void checkTicket();
    void checkFlight();
    void checkAirportLocation();
}

public abstract class AbstractAirport implements Flight, Ticket{
    public void check() {
        checkPassport();
        checkBaggage();
        checkTicket();
        checkFlight();
        checkAirportLocation();
    }

    public void checkPassport() {
        System.out.println("check passport");
    }
    public void checkBaggage() {
        System.out.println("check baggage");
    }
    public void checkTicket() {
        System.out.println("check ticket");
    }
    public void checkFlight() {
        System.out.println("check flight");
    }
    public void checkAirportLocation() {
        System.out.println("check airport location");
    }

    //    abstract method
    public abstract void checkAirportLocation();
}

public class GimpoAbstractAirport extends AbstractAirport {
    public void checkAirportLocation() {
        System.out.println("check departure: Incheon");
    }
}

public class IncheonAirport extends AbstractAirport {
    public void checkAirportLocation() {
        System.out.println("check departure: Gimpo");
    }
}
