package com.mygdx.game.MyGame.units;

import java.util.Objects;

public class Farmer extends BaseHero {

    public Farmer(String name, boolean firstTeam) {
        super("Фермер", 50, name, firstTeam, 5, new int[]{2, 4}, 1);
    }

    @Override
    public String getInfo() {
        return className + " " + name;
    }

    @Override
    public void step() {
        if (Objects.equals(state, "Dead")) return;
        if (filterVisibleTeam(getEnemyTeam()).isEmpty()) return;
        turnBegin();
        if (Objects.equals(this.state, "Busy")) {
            log(getInfo() + " пополнил запасы");
            this.state = "Stand";
        }
    }

//    @Override
//    public String toString() {
//        return super.toString() + " " + this.state;
//    }
}
