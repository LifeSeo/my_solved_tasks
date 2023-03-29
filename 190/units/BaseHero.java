package seminar01.units;

import seminar01.weapons.Weapons;

import java.util.Random;

public abstract class BaseHero implements GameInterface {
    public String name;

    protected int x;
    protected int y;

    protected int hp;
    protected int max_hp;

    protected int armor;
    protected int[] damage;

    protected Weapons weapon;

    @Override
    public String toString() {
        return this.getInfo() + " " + this.name + " Здоровье: " + this.hp + " Броня: " + this.armor;
    }

    public BaseHero(int hp, String name, int x, int y, int armor, int[] damage) {
        this.hp = hp;
        this.name = name;
        this.x = x;
        this.y = y;
        this.armor = armor;
        this.damage = damage;
    }

    protected int getInt() {
        return 1;
    }

    @Override
    public void step() {

    }

    @Override
    public String getInfo() {
        return getClass().getSimpleName();
    }
}
