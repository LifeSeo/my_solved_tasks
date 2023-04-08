package seminar01.units;

import seminar01.Spells;

import java.util.ArrayList;

public class Monk extends BaseHero {
    protected int mana;

    protected ArrayList<Spells> spellsBook;

    public Monk(String name, boolean firstTeam) {
        super("Монах", 50, name, firstTeam, 5, new int[]{2, 4}, 8);
        mana = 80;
    }

    @Override
    public String getInfo() {
        return className + " " + name;
    }
}
