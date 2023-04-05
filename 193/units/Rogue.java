package seminar01.units;

public class Rogue extends BaseHero {

    public Rogue(String name, boolean firstTeam) {
        super("Разбойник",50, name, firstTeam, 15, new int[]{9, 28}, 7);
    }

    @Override
    public String getInfo() {
        return className + " " + name;
    }
}
