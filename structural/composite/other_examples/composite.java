// component
interface Node {
    public String getName();
}

// leaf
class File implements Node {
    private String name;
    @Override
    public String getName(){ 
        return name;
    }
}

// composite
class Directory implements Node {
    private String name;
    private List<Node> children;
    @Override
    public String getName(){ 
        return name;
    }
    public void add(Node node) {
        children.add(node);
    }
}


// main
public class Main {
    public static void main(String[] args) 
    {
        Directory dir = new Directory();
        dir.add(new File());
        dir.add(new File());
        Directory secDir = new Directory();
        secDir.add(new File())
        dir.add(secDir);
    }
}
