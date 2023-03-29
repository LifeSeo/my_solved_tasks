package seminar01.units;

public class Bowman extends Shooter {

    int arrows;

    int accuracy;

    public Bowman(String name) {
        super(100, name, 1, 6, 50, new int[]{6, 12},  10, 60);
    }

    @Override
    public String getInfo() {
        return "Лучник";
    }
}

