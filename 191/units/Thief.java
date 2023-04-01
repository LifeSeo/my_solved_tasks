package seminar01.units;

public class Thief extends BaseHero {

    public Thief(String name, boolean firstTeam) {
        super(100, name, firstTeam, 50, new int[]{8, 15});
    }

    @Override
    public String getInfo() {
        return "Вор " + name;
    }
}
