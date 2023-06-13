import java.io.*;
import java.util.stream.Collectors;

public class WorkWithFiles {
    public static void writePrizeToy(Object object, String text, String filePath) {
        if (object != null)
            try (
                    FileWriter writer = new FileWriter(filePath, true)) {
                writer.write(object + text + "\n");
                writer.flush();
            } catch (
                    IOException ex) {
                System.out.println(ex.getMessage());
            }
    }

    public static String readFile(String path) throws IOException {
        BufferedReader reader = new BufferedReader(new FileReader(new File(path)));
        return reader.lines().collect(Collectors.joining(System.lineSeparator()));
    }

    public static String readLinesToArrayList(String filePath){

        String content = null;
        try {
            content = readFile(filePath);
        } catch (IOException e) {
            e.printStackTrace();
        }

        return content;
    }

    public static void write(String text, String filename) {
        if (text != null)
            try (
                    FileWriter writer = new FileWriter(filename, false)) {
                writer.write(text + "\n");
                writer.flush();
            } catch (
                    IOException ex) {
                System.out.println(ex.getMessage());
            }
    }

}
