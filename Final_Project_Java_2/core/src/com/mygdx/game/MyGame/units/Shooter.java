package com.mygdx.game.MyGame.units;

import com.mygdx.game.MyGame.teams.Team;

import java.util.Objects;
import java.util.Random;

public abstract class Shooter extends BaseHero {

    protected int arrows;

    protected int maxArrows;

    protected int accuracy;

    public Shooter(String className, int hp, String name, boolean team, int armor, int[] damage, int arrows, int accuracy) {
        super(className, hp, name, team, armor, damage, 10);
        this.arrows = arrows;
        maxArrows = arrows;
        this.accuracy = accuracy;
    }

    protected void shoot(BaseHero enemy) {
        this.arrows--;
        int dmg = new Random().nextInt(damage[0], damage[1]);
        log(this.getInfo() + " стреляет в " + enemy.getInfo());
        enemy.getDamage(dmg);
    }

    @Override
    public void step() {
        if (Objects.equals(state, "Dead")) return;
        Team<BaseHero> allyTeam = getAllyTeam();
        Team<BaseHero> enemyTeam = filterVisibleTeam(getEnemyTeam());
        if (enemyTeam.isEmpty()) return;
        turnBegin();
        if (hasLiveAlly("Фермер") && arrows != maxArrows) {
            arrows++;
            BaseHero peasant = getLiveAlly("Фермер");
            peasant.state = "Busy";
            log(getInfo() + " берёт стрелу от " + peasant.getInfo());
        }
        if (arrows >= 1) {
            shoot(findClosestEnemy());
        } else {
            log(getInfo() + " берёт стрелу со склада");
            arrows++;
        }
    }

    @Override
    public String toString() {
        return super.toString().replace("Статус", "➶: " + arrows + " Статус");
    }
}

