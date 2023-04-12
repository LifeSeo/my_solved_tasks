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

    public static double getDistance(Coords coords1, Coords coords2){
        return Math.sqrt(Math.pow(coords1.x - coords2.x, 2) + Math.pow(coords1.y - coords2.y, 2));
    }

    public int getX() {
        return this.x;
    }

    public int getY() {
        return this.y;
    }
}
