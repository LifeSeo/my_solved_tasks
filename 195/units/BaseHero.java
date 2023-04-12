package seminar01.units;

import java.io.FileWriter;
import java.io.IOException;
import java.util.*;

public abstract class BaseHero implements GameInterface {

    protected String className;

    protected boolean team;

    protected String name;

    protected int hp;

    public int getHp() {
        return hp;
    }

    protected int maxHp;

    protected int armor;
    protected int armorBuff;
    protected int[] damage;

    protected Coords position;

    protected int initiative;

    protected int initiativeBuff;

//    protected static PriorityQueue<BaseHero> initiativeList = new PriorityQueue<>(new Comparator<>() {
//        @Override
//        public int compare(BaseHero o1, BaseHero o2) {
//            return o2.initiative - o1.initiative;
//        }
//    });

    protected int id;

    protected String state;

    protected static int idCounter;

    protected static ArrayList<BaseHero> holyTeam;

    protected static ArrayList<BaseHero> darkTeam;

    protected static ArrayList<BaseHero> allTeam;

    protected static int count;

    protected static int lastFirstTeamX;
    protected static int lastFirstTeamY;

    protected static int lastSecondTeamX;
    protected static int lastSecondTeamY;

    {
        state = "Stand";
    }

    static {
        idCounter = 0;
        holyTeam = new ArrayList<>();
        darkTeam = new ArrayList<>();
        allTeam = new ArrayList<>();
        lastFirstTeamX = 1;
        lastFirstTeamY = 1;
        lastSecondTeamX = 10;
        lastSecondTeamY = 1;
    }

    public String getHeroName() {
        return name;
    }

    @Override
    public String toString() {
        return getClassIcon() + " " + this.name + " \uD83D\uDC97: " + this.hp + " \uD83D\uDEE1️: " + this.armor + " \uD83C\uDFBF: " +
                this.initiative + " ⚔️: " + Math.round(Math.abs((damage[0] + damage[1]) / 2)) + " Статус: " + this.state
                .replace("Dead", "\uD83D\uDC80")
                .replace("Stand", "\uD83D\uDE42")
                + " x" + position.x + " y" + position.y;
    }

    public Coords getPosition() {
        return this.position;
    }

    public BaseHero(String className, int hp, String name, boolean team, int armor, int[] damage, int initiative) {
        this.className = className;
        this.hp = hp;
        maxHp = hp;
        this.name = name;
        this.team = team;
        this.getAllyTeam().add(this);
        this.setPosition();
        this.armor = armor;
        this.damage = damage;
        this.initiative = initiative;
        this.id = idCounter++;
        allTeam.add(this);
//        initiativeList.add(this);
        count++;
    }

    protected void setPosition() {
        if (team) {
            this.position = new Coords(lastFirstTeamX, lastFirstTeamY++);
        } else this.position = new Coords(lastSecondTeamX, lastSecondTeamY++);
    }

    @Override
    public String getInfo() {
        return getClass().getSimpleName();
    }

    public static int getCount() {
        return count;
    }


    protected BaseHero findClosestEnemy() {
        ArrayList<BaseHero> enemyTeam = filterLiveTeam(getEnemyTeam());
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
        if (damage > 0)
            log(getInfo() + " получает " + damage + " урона");
        else
            log(getInfo() + " восстанавливает " + -damage + " здоровья");
        if (armor > 0) {
            armor -= damage;
            if (armor >= 0) return;
            else {
                damage = Math.abs(armor);
                armor = 0;
            }
        }
        if (hp - damage > 0) {
            hp -= damage;
        } else {
            hp = 0;
            state = "Dead";
            log(getInfo() + " умирает");
        }
    }

    @Override
    public void step() {
    }

    public void turnBegin() {
        if (Objects.equals(state, "Dead")) return;
        String text = "Ходит " + getInfo();
        if (team)
            text += " из первой команды";
        else text += " из второй команды";
        log(text);
    }

//    public static PriorityQueue<BaseHero> getInitiativeList() {
//        return initiativeList;
//    }

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

    protected ArrayList<BaseHero> getEnemyTeam() {
        if (team) return darkTeam;
        return holyTeam;
    }

    public static ArrayList<BaseHero> filterLiveTeam(ArrayList<BaseHero> team) {
        ArrayList<BaseHero> liveTeam = new ArrayList<>();
        for (BaseHero hero : team) {
            if (Objects.equals(hero.state, "Stand")) liveTeam.add(hero);
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

    protected boolean checkPosition(int pos_x, int pos_y) {
        if (pos_x > 10 || pos_y > 10 || pos_x < 1 || pos_y < 1)
            return false;
        for (BaseHero hero : getAllyTeam())
            if (hero.position.x == pos_x && hero.position.y == pos_y)
                return false;
        return true;
    }

    protected boolean hasLiveAlly(String className) {
        for (BaseHero hero : getAllyTeam()) {
            if (Objects.equals(hero.className, className) && Objects.equals(hero.state, "Stand")) {
                return true;
            }
        }
        return false;
    }

    protected BaseHero getLiveAlly(String className) {
        for (BaseHero hero : getAllyTeam()) {
            if (Objects.equals(hero.className, className) && Objects.equals(hero.state, "Stand")) {
                return hero;
            }
        }
        return this;
    }

    protected void log(String text) {
        try (FileWriter writer = new FileWriter("actionsLog.txt", true)) {
            writer.write(text + "\n");
            writer.flush();
        } catch (IOException ex) {
            System.out.println(ex.getMessage());
        }
    }

    protected boolean hasInjuredAlly() {
        for (BaseHero hero : filterLiveTeam(getAllyTeam())) {
            if (hero.maxHp != hp) return true;
        }
        return false;
    }

    protected BaseHero findLowestHpAlly() {
        ArrayList<BaseHero> allyTeam = filterLiveTeam(getAllyTeam());
        int maxHpDiff = allyTeam.get(0).maxHp - allyTeam.get(0).hp;
        BaseHero lowestHpAlly = allyTeam.get(0);
        for (BaseHero hero : allyTeam) {
            if (maxHpDiff < hero.maxHp - hero.hp) {
                maxHpDiff = hero.maxHp - hero.hp;
                lowestHpAlly = hero;
            }
        }
        return lowestHpAlly;
    }
}
