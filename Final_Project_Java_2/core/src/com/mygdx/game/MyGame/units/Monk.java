package com.mygdx.game.MyGame.units;

import java.util.Random;

public class Monk extends Spellcaster {

    public Monk(String name, boolean firstTeam) {
        super("Монах", 50, name, firstTeam, 5, new int[]{2, 4}, 8, 40);
    }

    @Override
    public String getInfo() {
        return className + " " + name;
    }

    protected void castHeal(BaseHero ally) {
        mana -= bigSpellCost;
        log(getInfo() + " применяет заклинание Исцеление на " + ally.getInfo());
        ally.getDamage(-(new Random().nextInt(15, 31)));
    }

    protected void castStoneArmor(BaseHero ally) {
        mana -= smallSpellCost;
        ally.armor += 15;
        ally.armorBuff += 15;
        log(getInfo() + " применяет заклинание Каменный Доспех на " + ally.getInfo());
    }

    @Override
    public void castSpell() {
        if (mana >= bigSpellCost && hasInjuredAlly()) {
            castHeal(findLowestHpAlly());
        } else if (mana >= smallSpellCost) {
            if (hasLiveAlly("Разбойник")) {
                castStoneArmor(getLiveAlly("Разбойник"));
            } else if (hasLiveAlly("Копейщик")) {
                castStoneArmor(getLiveAlly("Копейщик"));
            } else castStoneArmor(findClosestEnemy().findClosestEnemy());
        }

    }
}
