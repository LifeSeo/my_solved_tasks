public class Main {
    public static void main(String[] args) {
        App app = new App();
        app.createRandomToysFile();
        app.loadPrizeToysPool();
        app.prizeDraw(10);
    }
}
