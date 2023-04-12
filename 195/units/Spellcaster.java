package seminar01.units;

import java.util.ArrayList;
import java.util.Objects;

public abstract class Spellcaster extends BaseHero {

    int smallSpellCost;
    int bigSpellCost;
    double power;
    int mana;

    int maxMana;

    {
        smallSpellCost = 10;
        bigSpellCost = 30;
    }

    public Spellcaster(String className, int hp, String name, boolean team, int armor, int[] damage, int initiative,
                       int mana) {
        super(className, hp, name, team, armor, damage, initiative);
        this.mana = mana;
        maxMana = mana;
    }

    @Override
    public void step() {
        if (Objects.equals(state, "Dead")) return;
        if (filterLiveTeam(getEnemyTeam()).isEmpty()) return;
        turnBegin();
        ArrayList<BaseHero> allyTeam = getAllyTeam();
        if (hasLiveAlly("Фермер") && mana + 25 < maxMana) {
            mana += 25;
            BaseHero peasant = getLiveAlly("Фермер");
            peasant.state = "Busy";
            log(getInfo() + " берёт зелье маны от " + peasant.getInfo());
        }
        if (mana >= smallSpellCost)
            castSpell();
        else {
            log(getInfo() + " берёт банку маны на складе");
            mana += 25;
        }
    }

    public void castSpell() {
    }

    @Override
    public String toString() {
        return super.toString().replace("Статус", "\uD83D\uDCA7: " + mana + " Статус");
    }
}
