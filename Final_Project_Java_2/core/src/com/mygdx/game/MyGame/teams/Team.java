package com.mygdx.game.MyGame.teams;

import java.util.ArrayList;
import java.util.Iterator;
import java.util.Random;

import static com.mygdx.game.MyGame.Game.getName;

import com.mygdx.game.MyGame.units.BaseHero;
import com.mygdx.game.MyGame.units.Bowman;
import com.mygdx.game.MyGame.units.Crossbowman;
import com.mygdx.game.MyGame.units.Farmer;
import com.mygdx.game.MyGame.units.Monk;
import com.mygdx.game.MyGame.units.Rogue;
import com.mygdx.game.MyGame.units.Spearman;
import com.mygdx.game.MyGame.units.Wizard;

public class Team<T extends BaseHero> implements Iterable<BaseHero> {
    ArrayList<BaseHero> heroes = new ArrayList<>();

    private String name;

    public String getTeamName() {
        return this.name;
    }

    public Team() {
        this.heroes = new ArrayList<>();
    }

    public Team(String name) {
        this.heroes = new ArrayList<>();
        this.name = name;
    }

    public void createTeam(boolean firstTeam) {
        for (int i = 0; i < 10; i++) {
            int random = new Random().nextInt(6);
            switch (random) {
                case 0:
                    heroes.add(new Bowman(getName(), firstTeam));
                    break;
                case 1:
                    heroes.add(new Crossbowman(getName(), firstTeam));
                    break;
                case 2:
                    heroes.add(new Wizard(getName(), firstTeam));
                    break;
                case 3:
                    heroes.add(new Monk(getName(), firstTeam));
                    break;
                case 4:
                    heroes.add(new Spearman(getName(), firstTeam));
                    break;
                case 5:
                    heroes.add(new Rogue(getName(), firstTeam));
                    break;
                default:
                    heroes.add(new Farmer(getName(), firstTeam));
            }
        }
    }

    public BaseHero get(Integer index) {
        return heroes.get(index);
    }

    @Override
    public Iterator<BaseHero> iterator() {

        return new Iterator<BaseHero>() {

            private int index = 0;

            @Override
            public boolean hasNext() {
                return index < heroes.size();
            }

            @Override
            public BaseHero next() {
                return heroes.get(index++);
            }

        };

    }

    public int size() {
        return heroes.size();
    }

    public void add(T hero) {
        heroes.add(hero);
    }

    public boolean isEmpty() {
        return heroes.isEmpty();
    }

    public boolean contains(T human) {
        return heroes.contains(human);
    }
}
