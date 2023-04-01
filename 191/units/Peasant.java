package seminar01.units;

public class Peasant extends BaseHero {

    public Peasant(String name, boolean firstTeam) {
        super(200, name, firstTeam, 20, new int[]{3, 5});
    }

    @Override
    public String getInfo() {
        return "Крестьянин " + name;
    }
}
