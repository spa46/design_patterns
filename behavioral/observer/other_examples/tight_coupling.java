public class Video {
    private String title;
    private String content;
}

public class Youtube {
    private Video video;
    private SubscriberA subscriberA;
    private SubscriberB subscriberB;
    private SubscriberC subscriberC;

    public Youtube(SubscriberA subscriberA, SubscriberB subscriberB, SubscriberC subscriberC) {
        this.subscriberA = subscriberA;
        this.subscriberB = subscriberB;
        this.subscriberC = subscriberC;
    }

    public void newVideo(Video video) {
        this.video = video;
        subscriberA.update(video);
        subscriberB.update(video);
        subscriberC.update(video);
    }
}

public class SubscriberA {
    public void update(Video video) {
        System.out.println("SubscriberA Notification ");
    }
}

public class SubscriberB {
    public void update(Video video) {
        System.out.println("SubscriberB Notification ");
    }
}

public class SubscriberC {
    public void update(Video video) {
        System.out.println("SubscriberC Notification ");
    }
}
