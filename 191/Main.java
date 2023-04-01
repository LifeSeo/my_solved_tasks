package seminar01;

import seminar01.units.*;

import java.util.ArrayList;
import java.util.Random;

public class Main {

    public static void main(String[] args) {
//        ArrayList<BaseHero> heroes = rndClassesArrList();
//        heroes.forEach(n -> System.out.println(n));
//        System.out.println("_".repeat(40));
//        System.out.println("Всего персонажей: " + BaseHero.getCount());

//        if (heroes.get(0) instanceof Shooter) ((Shooter) heroes.get(0)).step();

//        heroes.forEach(n -> System.out.println(n.getInfo() + " " + n.name));

        ArrayList<BaseHero> firstTeam = createFirstTeam();

        ArrayList<BaseHero> secondTeam = createSecondTeam();

        System.out.println("Первая команда\n" + "_".repeat(40));
        firstTeam.forEach(n -> System.out.println(n.getHeroName() + " " + n.getPosition()));
        System.out.println("Вторая команда\n" + "_".repeat(40));
        secondTeam.forEach(n -> System.out.println(n.getHeroName() + " " + n.getPosition()));

        System.out.println("Ходы\n" + "_".repeat(40));
//        firstTeam.forEach(n -> System.out.println(n.getInfo()));
        firstTeam.forEach(n -> n.step(secondTeam));
//        secondTeam.forEach(n -> System.out.println(n.getInfo()));
        secondTeam.forEach(n -> n.step(firstTeam));

//        System.out.println(firstTeam.get(1).findClosestEnemy(secondTeam));

    }


    private static String getName() {
        return Names.values()[new Random().nextInt(Names.values().length)].toString();
    }

//    private static ArrayList<BaseHero> rndClassesArrList(){
//        ArrayList<BaseHero> heroes = new ArrayList<>();
//        for (int i = 0; i < 8; i++) {
//            int random = new Random().nextInt(6);
//            switch (random){
//                case 0: heroes.add(new Bowman(getName()));
//                break;
//                case 1: heroes.add(new Crossbowman(getName()));
//                break;
//                case 2: heroes.add(new Mage(getName()));
//                break;
//                case 3: heroes.add(new Monk(getName()));
//                break;
//                case 4: heroes.add(new Spearman(getName()));
//                break;
//                case 5: heroes.add(new Thief(getName()));
//                break;
//                default: heroes.add(new Peasant(getName()));
//            }
//        }
//        return heroes;
//    }


    public static ArrayList<BaseHero> createFirstTeam() {
        ArrayList<BaseHero> heroes = new ArrayList<>();
        for (int i = 0; i < 10; i++) {
            int random = new Random().nextInt(6);
            switch (random) {
                case 0:
                    heroes.add(new Bowman(getName(), true));
                    break;
                case 1:
                    heroes.add(new Crossbowman(getName(), true));
                    break;
                case 2:
                    heroes.add(new Mage(getName(), true));
                    break;
                case 3:
                    heroes.add(new Monk(getName(), true));
                    break;
                case 4:
                    heroes.add(new Spearman(getName(), true));
                    break;
                case 5:
                    heroes.add(new Thief(getName(), true));
                    break;
                default:
                    heroes.add(new Peasant(getName(), true));
            }
        }
        return heroes;
    }

    public static ArrayList<BaseHero> createSecondTeam() {
        ArrayList<BaseHero> heroes = new ArrayList<>();
        for (int i = 0; i < 10; i++) {
            int random = new Random().nextInt(6);
            switch (random) {
                case 0:
                    heroes.add(new Bowman(getName(), false));
                    break;
                case 1:
                    heroes.add(new Crossbowman(getName(), false));
                    break;
                case 2:
                    heroes.add(new Mage(getName(), false));
                    break;
                case 3:
                    heroes.add(new Monk(getName(), false));
                    break;
                case 4:
                    heroes.add(new Spearman(getName(), false));
                    break;
                case 5:
                    heroes.add(new Thief(getName(), false));
                    break;
                default:
                    heroes.add(new Peasant(getName(), false));
            }
        }
        return heroes;
    }

}
