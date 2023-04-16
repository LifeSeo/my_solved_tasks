package com.mygdx.game.MyGame.units;

import java.util.Random;

public class Wizard extends Spellcaster {

    public Wizard(String name, boolean firstTeam) {
        super("Волшебник", 50, name, firstTeam, 5, new int[]{2, 4}, 7, 40);
    }

    @Override
    public String getInfo() {
        return className + " " + name;
    }

    protected void castFireball(BaseHero enemy) {
        mana -= bigSpellCost;
        log(getInfo() + " применяет заклинание Фаербол на " + enemy.getInfo());
        enemy.getDamage(new Random().nextInt(15, 31));
    }

    protected void castAcceleration(BaseHero ally) {
        mana -= smallSpellCost;
        ally.initiative += 2;
        ally.initiativeBuff += 2;
        log(getInfo() + " применяет заклинание Ускорение на " + ally.getInfo());
    }

    @Override
    public void castSpell() {
        if (mana >= bigSpellCost) {
            BaseHero closestEnemy = findClosestEnemy();
            Coords enemyPosition = closestEnemy.getPosition();
            castFireball(closestEnemy);
        } else if (mana >= smallSpellCost) {
            castAcceleration(findClosestEnemy().findClosestEnemy());
        }

    }
}
