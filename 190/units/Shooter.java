package seminar01.units;

public abstract class Shooter extends BaseHero {

    int arrows;

    int accuracy;

    public Shooter(int hp, String name, int x, int y, int armor, int[] damage, int arrows, int accuracy) {
        super(hp, name, x, y, armor, damage);
        this.arrows = arrows;
        this.accuracy = accuracy;
    }

    protected void shoot() {
        System.out.println("Shoot!");
    }

    @Override
    public void step(){
        System.out.println("Shooter");
    };
}
