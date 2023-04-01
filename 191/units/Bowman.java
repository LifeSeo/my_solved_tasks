package seminar01.units;

public class Bowman extends Shooter {

    public Bowman(String name, boolean firstTeam) {
        super(100, name, firstTeam, 50, new int[]{6, 12},  10, 60);
    }

    @Override
    public String getInfo() {
        return "Лучник " + name;
    }
}

