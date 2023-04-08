package seminar01.units;

public class Spearman extends BaseHero {

    public Spearman(String name, boolean firstTeam) {
        super("Копейщик",50, name, firstTeam, 30, new int[]{12, 24}, 7);
    }


    @Override
    public String getInfo() {
        return className + " " + name;
    }
}
