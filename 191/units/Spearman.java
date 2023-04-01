package seminar01.units;

import seminar01.Spells;

import java.util.ArrayList;

public class Spearman extends BaseHero {

    public Spearman(String name, boolean firstTeam) {
        super(200, name, firstTeam, 100, new int[]{10, 20});
    }


    @Override
    public String getInfo() {
        return "Копейщик " + name;
    }
}
