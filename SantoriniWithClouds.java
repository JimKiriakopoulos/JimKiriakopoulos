import javax.swing.*;
import java.awt.*;
import java.net.URI;
import java.net.URL;
import javax.imageio.ImageIO;
import java.io.InputStream;
import java.util.Random;

public class SantoriniWithClouds extends JPanel {

    private Image santoriniImage;

    public SantoriniWithClouds() {
        try {
            // Χρησιμοποιούμε URI και μετατρέπουμε σε URL
            URI imageURI = new URI("https://upload.wikimedia.org/wikipedia/commons/thumb/a/a1/Monts_G%C3%A9raniens_depuis_Corinthe.jpg/408px-Monts_G%C3%A9raniens_depuis_Corinthe.jpg");
            URL imageURL = imageURI.toURL(); // Μετατροπή από URI σε URL

            // Φορτώνουμε την εικόνα από το URL
            santoriniImage = ImageIO.read(imageURL);
        } catch (Exception e) {
            System.out.println("Δεν ήταν δυνατή η φόρτωση της εικόνας.");
            e.printStackTrace();
        }
    }

    @Override
    protected void paintComponent(Graphics g) {
        super.paintComponent(g);

        // Σχεδιάζουμε την εικόνα της Σαντορίνης στο πάνελ
        g.drawImage(santoriniImage, 0, 0, getWidth(), getHeight(), this);

        // Προσθέτουμε τα σύννεφα
        Graphics2D g2d = (Graphics2D) g;
        g2d.setRenderingHint(RenderingHints.KEY_ANTIALIASING, RenderingHints.VALUE_ANTIALIAS_ON);

        // Δυναμική δημιουργία σύννεφων με τυχαία θέση και μεγέθη
        Random rand = new Random();

        // Προσθήκη γκρι σύννεφου
        g2d.setColor(new Color(169, 169, 169)); // Γκρι σύννεφα
        g2d.fillOval(rand.nextInt(getWidth()), rand.nextInt(getHeight() / 2), rand.nextInt(200) + 100, rand.nextInt(80) + 50); // Γκρι σύννεφο

        // Προσθήκη σκούρου γκρι σύννεφου
        g2d.setColor(new Color(105, 105, 105)); // Σκούρο γκρι σύννεφο
        g2d.fillOval(rand.nextInt(getWidth()), rand.nextInt(getHeight() / 2), rand.nextInt(250) + 150, rand.nextInt(100) + 60); // Σκούρο γκρι σύννεφο

        // Προσθήκη άσπρου σύννεφου
        g2d.setColor(Color.WHITE); // Άσπρο σύννεφο
        g2d.fillOval(rand.nextInt(getWidth()), rand.nextInt(getHeight() / 2), rand.nextInt(180) + 100, rand.nextInt(70) + 40); // Άσπρο σύννεφο

        // Προσθήκη μαύρου σύννεφου
        g2d.setColor(Color.BLACK); // Μαύρο σύννεφο
        g2d.fillOval(rand.nextInt(getWidth()), rand.nextInt(getHeight() / 2), rand.nextInt(250) + 150, rand.nextInt(100) + 60); // Μαύρο σύννεφο
    }

    public static void main(String[] args) {
        JFrame frame = new JFrame("Santorini with Clouds");
        SantoriniWithClouds panel = new SantoriniWithClouds();

        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setSize(800, 600);
        frame.add(panel);
        frame.setVisible(true);
    }
}
