package seminar01;

public enum SpellBook {

    healOne(1, -1), healFive(2, -5), healTen(3, -10),

    damageOne(1, 1), damageFive(2, 5), damageTen(3, 10),

    ressurect(25, Float.NaN);

    private final float cost, power;

    SpellBook(int cost, float power) {
        this.cost = cost;
        this.power = power;
    }

    public float getCost() {
        return cost;
    }

    public float getPower() {
        return power;
    }

}
