package seminar01.units;

import seminar01.Spells;

public class Wizard extends BaseHero {
    protected int mana;

    protected Spells[] spellsBook = new Spells[3];

    public Wizard(String name, boolean firstTeam) {
        super("Волшебник", 50, name, firstTeam, 5, new int[]{2, 4}, 8);
        mana = 100;
        spellsBook[0] = new Spells("Фаербол");
        spellsBook[1] = new Spells("Увеличение брони");
        spellsBook[2] = new Spells("Увеличение урона");
    }

    @Override
    public String getInfo() {
        return className + " " + name;
    }

}
