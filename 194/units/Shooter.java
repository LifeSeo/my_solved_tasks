package seminar01.units;

import seminar01.teams.Team;

import java.util.ArrayList;
import java.util.Objects;
import java.util.Random;

public abstract class Shooter extends BaseHero {

    protected int arrows;

    protected int accuracy;

    public Shooter(String className, int hp, String name, boolean team, int armor, int[] damage, int arrows, int accuracy) {
        super(className, hp, name, team, armor, damage, 10);
        this.arrows = arrows;
        this.accuracy = accuracy;
    }

    protected void shoot(BaseHero enemy) {
        this.arrows--;
        int dmg = new Random().nextInt(damage[0], damage[1]);
//        System.out.println(this.getInfo() + " стреляет в " + enemy.getInfo());
        enemy.getDamage(dmg);
    }

    protected boolean hasLiveStandPeasant(ArrayList<BaseHero> allyTeam) {
        for (BaseHero hero : allyTeam) {
            if (Objects.equals(hero.className, "Фермер") && Objects.equals(hero.state, "Stand")) {
                return true;
            }
        }
        return false;
    }

    protected BaseHero getLivePeasant(ArrayList<BaseHero> allyTeam) {
        for (BaseHero hero : allyTeam) {
            if (Objects.equals(hero.className, "Фермер") && Objects.equals(hero.state, "Stand")) {
                return hero;
            }
        }
        return this;
    }

    @Override
    public void step() {
        super.step();
        if (Objects.equals(state, "Dead")) return;
        ArrayList<BaseHero> allyTeam = getAllyTeam();
        ArrayList<BaseHero> enemyTeam = filterLiveTeam(getEnemiesTeam());
        if (enemyTeam.isEmpty()) return;
        if (hasLiveStandPeasant(allyTeam)) {
            this.arrows++;
            BaseHero peasant = getLivePeasant(allyTeam);
            peasant.state = "Busy";
//            System.out.println(getInfo() + " берёт стрелу от " + peasant.getInfo());
        }
        if (this.arrows <= 0) return;
        BaseHero closestEnemy = findClosestEnemy(enemyTeam);
        shoot(closestEnemy);
    }

    @Override
    public String toString() {
        return super.toString().replace("Статус", "➶: " + arrows + " Статус");
    }
}

