public interface Beverage {
    int getCost();
    String getTitle();
}

public class Americano implements Beverage {
    @Override
    public int getCost() {
        return 3000;
    }

    @Override
    public String getTitle() {
        return "Americano";
    }
}

public class CaffeLatte implements Beverage {
    @Override
    public int getCost() {
        return 4000;
    }

    @Override
    public String getTitle() {
        return "Cafe Latte";
    }
}

public class caffeMocha implements Beverage {
    @Override
    public int getCost() {
        return 4500;
    }

    @Override
    public String getTitle() {
        return "Cafe Mocha";
    }
}
