public abstract class Airport {
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

public class IncheonAirport extends Airport {
    public void checkAirportLocation() {
        System.out.println("check departure: Incheon");
    }
}

public class GimpoAirport extends Airport {
    public void checkAirportLocation() {
        System.out.println("check departure: Gimpo");
    }
}
