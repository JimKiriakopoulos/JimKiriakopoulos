import javax.swing.*;
import java.awt.*;

public class CatDrawing  extends JPanel {
    @Override
    protected void paintComponent(Graphics g) {
        super.paintComponent(g);

        // Σώμα της γάτας (Ωοειδές)
        g.setColor(Color.GRAY);
        g.fillOval(100, 150, 200, 120); // Σώμα γάτας

        // Κεφάλι της γάτας (Κύκλος)
        g.setColor(Color.GRAY);
        g.fillOval(150, 50, 100, 100); // Κεφάλι γάτας

        // Ματιά της γάτας (Δύο μάτια)
        g.setColor(Color.WHITE);
        g.fillOval(175, 75, 20, 20); // Αριστερό μάτι
        g.fillOval(205, 75, 20, 20); // Δεξί μάτι

        // Μαύροι μαθητές
        g.setColor(Color.BLACK);
        g.fillOval(180, 80, 8, 8); // Αριστερός μαθητής
        g.fillOval(210, 80, 8, 8); // Δεξί μαθητής

        // Μύτη της γάτας (Ροζ τρίγωνο)
        int[] xPoints = {200, 190, 210}; 
        int[] yPoints = {100, 120, 120};
        g.setColor(Color.PINK);
        g.fillPolygon(xPoints, yPoints, 3); // Μύτη

        // Στόμα της γάτας (Καμπύλη γραμμή)
        g.setColor(Color.BLACK);
        g.drawArc(190, 120, 20, 10, 0, -180); // Στόμα

        // Αυτιά της γάτας (Τρίγωνα)
        g.setColor(Color.GRAY);
        int[] leftEarX = {150, 130, 170};
        int[] leftEarY = {60, 20, 60};
        g.fillPolygon(leftEarX, leftEarY, 3); // Αριστερό αυτί

        int[] rightEarX = {250, 230, 270};
        int[] rightEarY = {60, 20, 60};
        g.fillPolygon(rightEarX, rightEarY, 3); // Δεξί αυτί

        // Ουρά της γάτας (Καμπύλη γραμμή)
        g.setColor(Color.GRAY);
        g.drawLine(300, 150, 400, 100); // Ουρά γάτας
        g.drawLine(400, 100, 350, 200); // Ουρά γάτας (δεύτερο κομμάτι)
    }

    public static void main(String[] args) {
        JFrame frame = new JFrame("Realistic Cat Drawing");
        CatDrawing catPanel = new CatDrawing();

        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setSize(500, 400);
        frame.add(catPanel);
        frame.setVisible(true);
    }
}