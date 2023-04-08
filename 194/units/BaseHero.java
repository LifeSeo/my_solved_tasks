package seminar01.units;

import java.util.*;

public abstract class BaseHero implements GameInterface {

    protected static int count;

    protected String className;

    protected boolean team;

    protected String name;

    protected static int lastFirstTeamX = 1;
    protected static int lastFirstTeamY = 1;

    protected static int lastSecondTeamX = 10;
    protected static int lastSecondTeamY = 1;

    protected int hp;

    public int getHp() {
        return hp;
    }

    protected int maxHp;

    protected int armor;
    protected int[] damage;

    protected Coords position;

    public int[] getCoords() {
        return new int[]{position.y, position.x};
    }

    protected int initiative;

    protected static PriorityQueue<BaseHero> initiativeList = new PriorityQueue<>(new Comparator<>() {
        @Override
        public int compare(BaseHero o1, BaseHero o2) {
            return o2.initiative - o1.initiative;
        }
    });

    protected int id;

    protected static int idCounter = 0;

    protected static ArrayList<BaseHero> allTeam = new ArrayList<>();

    protected String state;

    public String getHeroName() {
        return name;
    }

    protected static ArrayList<BaseHero> holyTeam = new ArrayList<>();

    protected static ArrayList<BaseHero> darkTeam = new ArrayList<>();

    @Override
    public String toString() {
        return this.name + " \uD83D\uDC97: " + this.hp + " \uD83D\uDEE1️: " + this.armor + " \uD83C\uDFBF: " +
                this.initiative + " ⚔️: " + Math.round(Math.abs((damage[0] + damage[1]) / 2)) + " Статус: " + this.state
                .replace("Dead", "\uD83D\uDC80")
                .replace("Stand", "\uD83D\uDE42");
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
            holyTeam.add(this);
        } else {
            this.position = new Coords(lastSecondTeamX, lastSecondTeamY++);
            darkTeam.add(this);
        }
        this.team = team;
        this.armor = armor;
        this.damage = damage;
        this.initiative = initiative;
        this.id = idCounter++;
        this.state = "Stand";
        allTeam.add(this);
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


    protected BaseHero findClosestEnemy(ArrayList<BaseHero> enemyTeam) {
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

    protected void getDamage(int damage) {
//        System.out.println(this.getInfo() + " получает " + damage + " урона");
        if (this.hp - damage > 0) {
            this.hp -= damage;
        } else {
            hp = 0;
            state = "Dead";
//            System.out.println(this.getInfo() + " умирает");
//            getAllyTeam().remove(this);
        }
    }

    @Override
    public void step() {
        if (Objects.equals(state, "Dead")) return;
//        String text = "Ходит " + getInfo();
//        if (this.team)
//            text += " из первой команды";
//        else text += " из второй команды";
//        System.out.println(text);
    }

    public static PriorityQueue<BaseHero> getInitiativeList() {
        return initiativeList;
    }

    public int getInitiative() {
        return initiative;
    }

    public static ArrayList<BaseHero> getAllTeam() {
        return allTeam;
    }

    public int getId() {
        return id;
    }

    protected ArrayList<BaseHero> getAllyTeam() {
        if (team) return holyTeam;
        return darkTeam;
    }

    protected ArrayList<BaseHero> getEnemiesTeam() {
        if (team) return darkTeam;
        return holyTeam;
    }

    public static ArrayList<BaseHero> filterLiveTeam(ArrayList<BaseHero> team) {
        ArrayList<BaseHero> liveTeam = new ArrayList<>();
        for (BaseHero hero : team) {
            if (!Objects.equals(hero.state, "Dead")) liveTeam.add(hero);
        }
        return liveTeam;
    }

    public static ArrayList<BaseHero> getHolyTeam() {
        return holyTeam;
    }

    public static ArrayList<BaseHero> getDarkTeam() {
        return darkTeam;
    }

    public String getState() {
        return state;
    }

    public String getClassIcon() {
        switch (this.className) {
            default:
                return "" + this.className.charAt(0);
        }
    }
}
