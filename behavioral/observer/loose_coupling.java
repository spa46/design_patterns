public interface Observer {
    void update(Video video);
}

public class Youtube {
    private Video video;
    private Observer observer;

    public Youtube(Observer observer) {
        this.observer = observer;
    }

    public void newVideo(Video video) {
        this.video = video;
        observer.update(video);
    }
}

public class SubscriberA implements Observer{
    public void update(Video video) {
        System.out.println("SubscriberA Notification ");
    }
}

public class SubscriberB implements Observer {
    public void update(Video video) {
        System.out.println("SubscriberB Notification ");
    }
}

public class SubscriberC implements Observer {
    public void update(Video video) {
        System.out.println("SubscriberC Notification ");
    }
}
