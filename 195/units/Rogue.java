package seminar01.units;

import java.util.Objects;

public class Rogue extends Infantry {

    public Rogue(String name, boolean firstTeam) {
        super("Разбойник", 50, name, firstTeam, 30, new int[]{9, 29}, 11);
    }

    @Override
    public String getInfo() {
        return className + " " + name;
    }

    @Override
    public void step() {
        turnBegin();
        if (Objects.equals(state, "Dead")) return;
        if (!Objects.equals(state, "Hide")) {
            state = "Hide";
            log(getInfo() + " прячется");
        } else {
            state = "Stand";
            log(getInfo() + " раскрылся");
        }
        super.step();
    }

    @Override
    public String toString() {
        return super.toString().replace("Hide", "\uD83D\uDC00");
    }
}
