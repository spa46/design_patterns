public interface Observer {
    void update(Subject subject);
}

public class SubscriberA implements Observer{
    public void update(Subject subject) {
        System.out.println("SubscriberA 영상 알림 ");

        if (subject instanceof Youtube) {
            Youtube youtube = (Youtube) subject;
            Video video = youtube.getVideo();
        }
    }
}

// B, C have same implementations 

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
            observer.update(this);
        }
    }

    public void newVideo(Video video) {
        this.video = video;
        notifyObserver();
    }

    public Video getVideo() {
        return video;
    }
}
