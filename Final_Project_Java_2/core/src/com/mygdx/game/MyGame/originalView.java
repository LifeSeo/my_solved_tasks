package com.mygdx.game.MyGame;

import com.mygdx.game.MyGame.units.BaseHero;

import java.util.Collections;

public class originalView {
    private static int step = 1;
    private static final int[] l = {0};
    private static final String top10 = formatDiv("a") + String.join("", Collections.nCopies(9, formatDiv("-b"))) + formatDiv("-c");
    private static final String midl10 = formatDiv("d") + String.join("", Collections.nCopies(9, formatDiv("-e"))) + formatDiv("-f");
    private static final String bottom10 = formatDiv("g") + String.join("", Collections.nCopies(9, formatDiv("-h"))) + formatDiv("-i");

    private static void tabSetter(int cnt, int max) {
        int dif = max - cnt + 2;
        if (dif > 0) System.out.printf("%" + dif + "s", ":\t");
        else System.out.print(":\t");
    }

    private static String formatDiv(String str) {
        return str.replace('a', '\u250c')
                .replace('b', '\u252c')
                .replace('c', '\u2510')
                .replace('d', '\u251c')
                .replace('e', '\u253c')
                .replace('f', '\u2524')
                .replace('g', '\u2514')
                .replace('h', '\u2534')
                .replace('i', '\u2518')
                .replace('-', '\u2500');
    }

    private static String getChar(int x, int y) {
        String out = "| ";
        for (BaseHero human : Game.allTeam) {
            if (human.getCoords()[0] == x && human.getCoords()[1] == y) {
                if (human.getHp() != 0) {
                    if (BaseHero.getDarkTeam().contains(human)) {
                        out = "|" + (AnsiColors.ANSI_GREEN + human.getClassIcon() + AnsiColors.ANSI_RESET);
                        break;
                    }
                    if (BaseHero.getHolyTeam().contains(human)) {
                        out = "|" + (AnsiColors.ANSI_BLUE + human.getClassIcon() + AnsiColors.ANSI_RESET);
                        break;
                    }
                } else {
                    out = "|" + (AnsiColors.ANSI_RED + human.getClassIcon() + AnsiColors.ANSI_RESET);
                    break;
                }
            }
        }
        return out;
    }

    public static void view() {
        if (step == 1) {
            System.out.print(AnsiColors.ANSI_RED + "First step" + AnsiColors.ANSI_RESET);
        } else {
            System.out.print(AnsiColors.ANSI_RED + "Step:" + step + AnsiColors.ANSI_RESET);
        }
        step++;
        for (BaseHero v: Game.allTeam){
            l[0] = Math.max(l[0], v.toString().length());
        }
        System.out.print("_".repeat(l[0] * 2));
        System.out.println();
        System.out.print(top10 + "    ");
        System.out.print(AnsiColors.ANSI_BLUE + "Blue side" + AnsiColors.ANSI_RESET);
        //for (int i = 0; i < l[0]-9; i++)
        System.out.print(" ".repeat(l[0] - 9));
        System.out.println(AnsiColors.ANSI_GREEN + " \tGreen side" + AnsiColors.ANSI_RESET);
        for (int i = 1; i < 11; i++) {
            System.out.print(getChar(1, i));
        }
        System.out.print("|    ");
        System.out.print(Game.holyTeam.get(0));
        tabSetter(Game.holyTeam.get(0).toString().length(), l[0]);
        System.out.println(Game.darkTeam.get(0));
        System.out.println(midl10);

        for (int i = 2; i < 10; i++) {
            for (int j = 1; j < 11; j++) {
                System.out.print(getChar(i, j));
            }
            System.out.print("|    ");
            System.out.print(Game.holyTeam.get(i - 1));
            tabSetter(Game.holyTeam.get(i - 1).toString().length(), l[0]);
            System.out.println(Game.darkTeam.get(i - 1));
            System.out.println(midl10);
        }
        for (int j = 1; j < 11; j++) {
            System.out.print(getChar(10, j));
        }
        System.out.print("|    ");
        System.out.print(Game.holyTeam.get(9));
        tabSetter(Game.holyTeam.get(9).toString().length(), l[0]);
        System.out.println(Game.darkTeam.get(9));
        System.out.println(bottom10);
    }
}
