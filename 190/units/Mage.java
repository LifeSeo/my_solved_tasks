package seminar01.units;

import seminar01.Spells;

import java.util.ArrayList;

public class Mage extends BaseHero {
    protected int mana;

    protected Spells[] spells_book = new Spells[3];

    public Mage(String name) {
        super(100, name, 1, 6, 15, new int[]{3, 5});
        mana = 100;
        spells_book[0] = new Spells("Фаербол");
        spells_book[1] = new Spells("Увеличение брони");
        spells_book[2] = new Spells("Увеличение урона");
    }

    @Override
    public String getInfo() {
        return "Маг";
    }

}
