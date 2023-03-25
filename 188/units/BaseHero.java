package seminar01.units;

import seminar01.weapons.Weapons;

import java.util.Random;

public abstract class BaseHero {
    public String name;
    protected String class_name;

    protected int x;
    protected int y;

    protected int hp;
    protected int max_hp;

    protected int armor;
    protected int[] damage;

    protected Weapons weapon;

    @Override
    public String toString() {
        return name + " " + hp + " " + armor + " " + class_name;
    }

    public BaseHero(int hp, String name, int x, int y, int armor, int[] damage, String class_name){
        this.hp = hp;
        this.name = name;
        this.x = x;
        this.y = y;
        this.armor = armor;
        this.damage = damage;
        this.class_name = class_name;
    }

    protected int getInt(){
        return 1;
    }
}
