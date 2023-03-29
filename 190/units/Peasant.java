package seminar01.units;

public class Peasant extends BaseHero {

    public Peasant(String name) {
        super(200, name, 1, 6, 20, new int[]{3, 5});
    }

    @Override
    public String getInfo() {
        return "Крестьянин";
    }
}
