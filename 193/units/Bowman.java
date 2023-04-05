package seminar01.units;

public class Bowman extends Shooter {

    public Bowman(String name, boolean firstTeam) {
        super("Лучник",50, name, firstTeam, 10, new int[]{8, 16},  10, 60);
    }

    @Override
    public String getInfo() {
        return className + " " + name;
    }
}

