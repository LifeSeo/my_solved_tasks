package seminar01.units;

import seminar01.Names;
import seminar01.weapons.Weapons;

import java.util.ArrayList;
import java.util.Random;

public abstract class BaseHero implements GameInterface {

    protected Coords position;

    protected static int count;

    protected String class_name;

    protected boolean team;

    protected String name;

    protected static int lastFirstTeamX = 0;
    protected static int lastFirstTeamY = 0;

    protected static int lastSecondTeamX = 9;
    protected static int lastSecondTeamY = 0;

    protected int hp;
    protected int max_hp;

    protected int armor;
    protected int[] damage;

    protected Weapons weapon;

    public String getHeroName(){
        return name;
    }
    @Override
    public String toString() {
        return this.getInfo() + " " + this.name + " Здоровье: " + this.hp + " Броня: " + this.armor;
    }

    public String getPosition() {
        return position.toString();
    }

    public BaseHero(int hp, String name, boolean team, int armor, int[] damage) {
        this.hp = hp;
        this.name = name;
        if (team) {
            this.position = new Coords(lastFirstTeamX, lastFirstTeamY++);
        } else {
            this.position = new Coords(lastSecondTeamX, lastSecondTeamY++);
        }
        this.armor = armor;
        this.damage = damage;
        count++;
    }

    protected int getInt() {
        return 1;
    }

    @Override
    public String getInfo() {
        return getClass().getSimpleName();
    }

    public static int getCount() {
        return count;
    }

    private static String getName() {
        return Names.values()[new Random().nextInt(Names.values().length)].toString();
    }

    public BaseHero findClosestEnemy(ArrayList<BaseHero> enemyTeam) {
        BaseHero closestEnemy = enemyTeam.get(0);
        double distance = Coords.getDistance(this.position, enemyTeam.get(0).position);
        double minDistance = distance;
        for (int i = 1; i < enemyTeam.size(); i++) {
            if (enemyTeam.get(i).hp <= 0) continue;
            distance = Coords.getDistance(this.position, enemyTeam.get(i).position);
            if (minDistance > distance) {
                minDistance = distance;
                closestEnemy = enemyTeam.get(i);
            }
        }
        return closestEnemy;
    }
    public void getDamage(int damage) {
        if (this.hp - damage > 0) {
            this.hp -= damage;
        }
        // else { die(); }
    }

    @Override
    public void step(ArrayList<BaseHero> enemyTeam) {

    }
}
