package seminar01.units;

import java.util.ArrayList;
import java.util.Objects;

public class Peasant extends BaseHero {

    public Peasant(String name, boolean firstTeam) {
        super("Крестьянин", 50, name, firstTeam, 5, new int[]{2, 4}, 1);
    }

    @Override
    public String getInfo() {
        return className + " " + name;
    }

    @Override
    public void step() {
        super.step();
        if (Objects.equals(state, "Dead")) return;
        if (Objects.equals(this.state, "Busy")) {
            System.out.println(getInfo() + " принёс стрелу");
            this.state = "Stand";
        }
    }

//    @Override
//    public String toString() {
//        return super.toString() + " " + this.state;
//    }
}
