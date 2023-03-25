package seminar01.units;

public class Crossbowman extends BaseHero {

    int arrows;

    int accuracy;

    public Crossbowman(String name) {
        super(100, name, 1, 6, 75, new int[]{8, 14}, "Арбалетчик");
        arrows = 10;
        accuracy = 50;
    }
}
