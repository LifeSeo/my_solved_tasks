package seminar01.units;

public class Crossbowman extends Shooter {

    public Crossbowman(String name, boolean firstTeam) {
        super("Арбалетчик", 50, name, firstTeam, 10, new int[]{10, 20}, 10, 80);
    }

    @Override
    public String getInfo() {
        return className + " " + name;
    }
}
