package com.mygdx.game.MyGame.units;

import java.util.Objects;
import java.util.Random;

public abstract class Infantry extends BaseHero {
    public Infantry(String className, int hp, String name, boolean team, int armor, int[] damage, int initiative) {
        super(className, hp, name, team, armor, damage, initiative);
    }

    protected void attack(BaseHero enemy) {
        log(getInfo() + " атакует " + enemy.getInfo());
        enemy.getDamage(new Random().nextInt(damage[0], damage[1]));
    }

    @Override
    public void step() {
        if (Objects.equals(state, "Dead")) return;
        if (filterVisibleTeam(getEnemyTeam()).isEmpty()) return;
        BaseHero closestEnemy = findClosestEnemy();
        Coords enemyPosition = closestEnemy.getPosition();
        double distance = Coords.getDistance(position, enemyPosition);
        if (distance <= 1) {
            attack(closestEnemy);
            return;
        }

        int x_diff = enemyPosition.getX() - getPosition().getX();
        int y_diff = enemyPosition.getY() - getPosition().getY();

        int move_x = 0;
        int move_y = 0;

        int s_x = (int) Math.signum(x_diff);
        int s_y = (int) Math.signum(y_diff);
        if (Math.abs(x_diff) > Math.abs(y_diff)) {
            move_x += s_x;
        } else move_y += s_y;
        boolean flag = true;
        if (!checkPosition(position.x + move_x, position.y + move_y)) {
            move_x = 0;
            move_y = 0;
            flag = false;
            if (checkPosition(position.x + move_x, position.y + move_y + s_y)) {
                move_y = s_y;
                flag = true;
            }
            if (!flag)
                if (checkPosition(position.x + s_x, position.y + move_y)) {
                    move_x = s_x;
                    flag = true;
                }
        }

        log(getInfo() + " направляется к " + closestEnemy.getInfo());

        position.x += move_x;
        position.y += move_y;

        resetBuffs();
    }

    protected void resetBuffs() {
        initiative -= initiativeBuff;
        initiativeBuff = 0;
        if (armor - armorBuff >= 0)
            armor -= armorBuff;
        else armor = 0;
        armorBuff = 0;
    }
}
