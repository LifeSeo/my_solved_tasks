import java.util.Random;

public class App {
    PrizeToysDraw prizeToysDraw;
    String beforeFile = "beforeDrawToysPool.csv";

    String toysPoolFile = "toysPool.csv";

    String prizeToysFile = "prizeToys.txt";

    public App() {
        prizeToysDraw = new PrizeToysDraw();
    }

    public void prizeDraw(int count) {
        save(prizeToysDraw.toStringCsv(), beforeFile);
        save("Выданные призы", prizeToysFile);
        for (int i = 0; i < count; i++) {
            prizeToysDraw.dropPrizeToy();
            WorkWithFiles.writePrizeToy(prizeToysDraw.getPrizeToy(),
                    "", prizeToysFile);
        }
        save(prizeToysDraw.toStringCsv(), toysPoolFile);
    }

    public void createRandomToysFile() {
        Random rnd = new Random();
        PrizeToysDraw draw = new PrizeToysDraw();
        for (int i = 0; i < 5; i++) {
            draw.addToy(new Toy(getToyName(), rnd.nextInt(1, 5), rnd.nextInt(1, 101)));
        }
        save(draw.toStringCsv(), toysPoolFile);
    }

    private void save(String text, String filename) {
        WorkWithFiles.write(text, filename);
    }

    private static String getToyName() {
        return ToysNames.values()[new Random().nextInt(ToysNames.values().length)].toString();
    }

    public void loadPrizeToysPool(){
       prizeToysDraw.addingFromCsv(WorkWithFiles.readLinesToArrayList(toysPoolFile));
    }
}
