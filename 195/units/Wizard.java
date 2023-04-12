package seminar01.units;

import seminar01.Spells;

import java.util.Random;

public class Wizard extends Spellcaster {

    protected Spells[] spellsBook = new Spells[3];

    public Wizard(String name, boolean firstTeam) {
        super("Волшебник", 50, name, firstTeam, 5, new int[]{2, 4}, 7, 40);
        spellsBook[0] = new Spells("Фаербол");
        spellsBook[1] = new Spells("Увеличение брони");
        spellsBook[2] = new Spells("Увеличение урона");
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
