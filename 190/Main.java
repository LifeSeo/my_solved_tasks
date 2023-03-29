package seminar01;

import seminar01.units.*;

import java.util.ArrayList;
import java.util.Random;

public class Main {
    public static void main(String[] args) {
        ArrayList<BaseHero> heroes = rndClassesArrList();
        heroes.forEach(n -> System.out.println(n));

//        heroes.forEach(n -> System.out.println(n.getInfo() + " " + n.name));
    }

    private static String getName() {
        return Names.values()[new Random().nextInt(Names.values().length)].toString();
    }

    private static ArrayList<BaseHero> rndClassesArrList(){
        ArrayList<BaseHero> heroes = new ArrayList<>();
        for (int i = 0; i < 8; i++) {
            int random = new Random().nextInt(6);
            switch (random){
                case 0: heroes.add(new Bowman(getName()));
                break;
                case 1: heroes.add(new Crossbowman(getName()));
                break;
                case 2: heroes.add(new Mage(getName()));
                break;
                case 3: heroes.add(new Monk(getName()));
                break;
                case 4: heroes.add(new Spearman(getName()));
                break;
                case 5: heroes.add(new Thief(getName()));
                break;
                default: heroes.add(new Peasant(getName()));
            }
        }
        return heroes;
    }

}
