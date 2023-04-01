package seminar01.units;

import seminar01.Spells;

import java.util.ArrayList;

public class Monk extends BaseHero {
    protected int mana;

    protected ArrayList<Spells> spells_book;

    public Monk(String name, boolean firstTeam) {
        super(150, name, firstTeam, 30, new int[]{5, 8});
        mana = 80;
    }

    @Override
    public String getInfo() {
        return "Монах " + name;
    }
}
