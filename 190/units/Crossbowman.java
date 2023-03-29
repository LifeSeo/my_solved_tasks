package seminar01.units;

public class Crossbowman extends Shooter {

    int arrows;

    int accuracy;

    public Crossbowman(String name) {
        super(100, name, 1, 6, 75, new int[]{8, 14},  10, 80);
    }

    @Override
    public String getInfo() {
        return "Арбалетчик";
    }
}
