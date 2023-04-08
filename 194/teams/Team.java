package seminar01.teams;

import seminar01.units.*;

import java.util.ArrayList;
import java.util.Iterator;
import java.util.Random;

import static seminar01.Main.getName;

public class Team<T extends BaseHero> implements Iterable<BaseHero>{
    ArrayList<BaseHero> heroes = new ArrayList<>();

    private String name;

    public String getTeamName(){
        return this.name;
    }

    public Team(String name, boolean ally, int size) {
        this.heroes = new ArrayList<>();
        this.name = name;
        createTeam(size, ally);
    }

    private void createTeam(int size, boolean firstTeam) {
        for (int i = 0; i < size; i++) {
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

        Iterator<BaseHero> it = new Iterator<BaseHero>() {

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
        return it;

    }

    public int size() {
        return heroes.size();
    }
}
