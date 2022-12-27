public interface Observer {
    void update(Video video);
}

public class SubscriberA implements Observer{
    public void update(Video video) {
        System.out.println("SubscriberA Notofications ");
    }
}

public class SubscriberB implements Observer {
    public void update(Video video) {
        System.out.println("SubscriberB Notofications ");
    }
}

public class SubscriberC implements Observer {
    public void update(Video video) {
        System.out.println("SubscriberC Notofications ");
    }
}

public interface Subject {
    void attach(Observer observer);
    void detach(Observer observer);
    void notifyObserver();
}

public class Youtube implements Subject {
    private List<Observer> observers;
    private Video video;

    public Youtube(List<Observer> observers) {
        this.observers = observers;
    }

    @Override
    public void attach(Observer observer) {
        observers.add(observer);
    }

    @Override
    public void detach(Observer observer) {
        observers.remove(observer);
    }

    @Override
    public void notifyObserver() {
        for (Observer observer: observers) {
            observer.update(video);
        }
    }

    public void newVideo(Video video) {
        this.video = video;
        notifyObserver();
    }
}
