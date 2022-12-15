// Component
public interface Beverage {
    int getCost();
    String getTitle();
}

// ConcreteComponent
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

// ConcreteComponent
public class HerbalTea implements Beverage {
    @Override
    public int getCost() {
        return 4000;
    }

    @Override
    public String getTitle() {
        return "Herb Tea";
    }
}

// Decorator
public abstract class CondimentDecorator implements Beverage {
    private final Beverage beverage;

    public CondimentDecorator(Beverage beverage) {
        this.beverage = beverage;
    }

    @Override
    public int getCost() {
        return beverage.getCost();
    }
    @Override
    public String getTitle() {
        return beverage.getTitle();
    }
}

// ConcreteDecorator
public class Sugar extends CondimentDecorator {
    public Sugar(Beverage beverage) {
        super(beverage);
    }

    @Override
    public int getCost() {
        return super.getCost() + 200;
    }

    @Override
    public String getTitle() {
        return super.getTitle() + " Add Sugar ";
    }
}

// ConcreteDecorator
public class Shot extends CondimentDecorator {
    public Shot(Beverage beverage) {
        super(beverage);
    }

    @Override
    public int getCost() {
        return super.getCost() + 500;
    }

    @Override
    public String getTitle() {
        return super.getTitle() + " Add Shot ";
    }
}

Beverage americano = new Americano();
Beverage americanoOneShot = new Shot(americano);

System.out.println(americanoOneShot.getCost());
System.out.println(americanoOneShot.getTitle());

Beverage herbalTea = new HerbalTea();
Beverage herbalTeaOneSugar = new Sugar(herbalTea);

System.out.println(herbalTeaOneSugar.getCost());
System.out.println(herbalTeaOneSugar.getTitle());
