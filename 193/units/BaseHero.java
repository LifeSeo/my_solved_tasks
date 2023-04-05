package seminar01.units;

import seminar01.Names;
import seminar01.teams.Team;
import seminar01.weapons.Weapons;

import java.util.*;

public abstract class BaseHero implements GameInterface {

    protected static int count;

    protected String className;

    protected boolean team;

    protected String name;

    protected static int lastFirstTeamX = 0;
    protected static int lastFirstTeamY = 0;

    protected static int lastSecondTeamX = 9;
    protected static int lastSecondTeamY = 0;

    protected int hp;
    protected int maxHp;

    protected int armor;
    protected int[] damage;

    protected Weapons weapon;

    protected Coords position;

    protected int initiative;

    protected static PriorityQueue<BaseHero> initiativeList = new PriorityQueue<>(new Comparator<>() {
        @Override
        public int compare(BaseHero o1, BaseHero o2) {
            return o2.initiative - o1.initiative;
        }
    });

    protected int id;

    protected static int idCounter = 0;

    protected static ArrayList<BaseHero> allHeroesList = new ArrayList<>();

    protected String state;

    public String getHeroName() {
        return name;
    }

    protected static ArrayList<BaseHero> firstTeam = new ArrayList<>();

    protected static ArrayList<BaseHero> secondTeam = new ArrayList<>();

    @Override
    public String toString() {
        return this.getInfo() + " Здоровье: " + this.hp + " Броня: " + this.armor + " Инициатива: " + this.initiative + " state: " + this.state;
    }

    public String getPosition() {
        return position.toString();
    }

    public BaseHero(String className, int hp, String name, boolean team, int armor, int[] damage, int initiative) {
        this.className = className;
        this.hp = hp;
        this.name = name;
        if (team) {
            this.position = new Coords(lastFirstTeamX, lastFirstTeamY++);
            firstTeam.add(this);
        } else {
            this.position = new Coords(lastSecondTeamX, lastSecondTeamY++);
            secondTeam.add(this);
        }
        this.team = team;
        this.armor = armor;
        this.damage = damage;
        this.initiative = initiative;
        this.id = idCounter++;
        this.state = "Stand";
        allHeroesList.add(this);
        initiativeList.add(this);
        count++;
    }

    @Override
    public String getInfo() {
        return getClass().getSimpleName();
    }

    public static int getCount() {
        return count;
    }

    public BaseHero findClosestEnemy(ArrayList<BaseHero> enemyTeam) {
        BaseHero closestEnemy = enemyTeam.get(0);
        double distance = Coords.getDistance(this.position, enemyTeam.get(0).position);
        double minDistance = distance;
        for (int i = 1; i < enemyTeam.size(); i++) {
            distance = Coords.getDistance(this.position, enemyTeam.get(i).position);
            if (minDistance > distance) {
                minDistance = distance;
                closestEnemy = enemyTeam.get(i);
            }
        }
        return closestEnemy;
    }

    public void getDamage(int damage) {
        System.out.println(this.getInfo() + " получает " + damage + " урона");
        if (this.hp - damage > 0) {
            this.hp -= damage;
        } else {
            hp = 0;
            state = "Dead";
            System.out.println(this.getInfo() + " умирает");
            getAllyTeam().remove(this);
        }
    }

    @Override
    public void step() {
        if (Objects.equals(state, "Dead")) return;
        String text = "Ходит " + getInfo();
        if (this.team)
            text += " из первой команды";
        else text += " из второй команды";
        System.out.println(text);
    }

    public static PriorityQueue<BaseHero> getInitiativeList() {
        return initiativeList;
    }

    public int getInitiative() {
        return initiative;
    }

    public static ArrayList<BaseHero> getAllHeroesList() {
        return allHeroesList;
    }

    public int getId() {
        return id;
    }

    protected ArrayList<BaseHero> getAllyTeam() {
        if (team) return firstTeam;
        return secondTeam;
    }

    protected ArrayList<BaseHero> getEnemiesTeam() {
        if (team) return secondTeam;
        return firstTeam;
    }

    public static ArrayList<BaseHero> getFirstTeam() {
        return firstTeam;
    }

    public static ArrayList<BaseHero> getSecondTeam() {
        return secondTeam;
    }

    public String getState() {
        return state;
    }
}
