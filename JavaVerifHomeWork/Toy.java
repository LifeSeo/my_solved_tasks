import java.util.ArrayList;
import java.util.List;
import java.util.Queue;
import java.util.Random;
import java.util.stream.Collectors;

public class Toy {
    private static int idCounter;
    private int id;
    private String name;
    private int count;

    private int dropRate;

    static {
        idCounter = 0;
    }

    public Toy(String name, int count, int dropRate) {
        this.id = idCounter++;
        this.name = name;
        this.count = count;
        this.dropRate = dropRate;
    }

    public Toy(int idCounter, String name, int count, int dropRate) {
        this.id = idCounter;
        this.name = name;
        this.count = count;
        this.dropRate = dropRate;
    }

    @Override
    public String toString() {
        return name + " id " + id;
    }

    public int getDropRate() {
        return dropRate;
    }

    public void setDropRate(int dropRate) {
        this.dropRate = dropRate;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public int getCount() {
        return count;
    }

    public void setCount(int count) {
        this.count = count;
    }

    public int getId() {
        return id;
    }
}
