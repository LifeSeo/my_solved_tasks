package seminar01.units;

public class Spearman extends Infantry {

    public Spearman(String name, boolean firstTeam) {
        super("Копейщик",100, name, firstTeam, 100, new int[]{12, 24}, 9);
    }


    @Override
    public String getInfo() {
        return className + " " + name;
    }

    @Override
    public void step() {
        turnBegin();
        super.step();
    }
}
