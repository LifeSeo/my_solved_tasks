package seminar01.units;

public class Coords {
    protected int x, y;

    public Coords(int x, int y){
        this.x = x;
        this.y = y;
    }

    @Override
    public String toString() {
        return "x: " + this.x + "y: " + this.y ;
    }

    public static double getDistance(Coords coords_1, Coords coords_2){
        return Math.sqrt(Math.pow(coords_1.x - coords_2.x, 2) + Math.pow(coords_1.y - coords_2.y, 2));
    }
}
