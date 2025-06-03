import javax.swing.*;
import java.awt.*;

public class SantoriniDrawing extends JPanel {

    // Ζωγραφίζουμε τα στοιχεία της Σαντορίνης
    @Override
    protected void paintComponent(Graphics g) {
        super.paintComponent(g);
        
        // Θέτουμε το φόντο της θάλασσας
        g.setColor(new Color(0, 105, 148));  // Θάλασσα (γαλάζιο χρώμα)
        g.fillRect(0, 250, getWidth(), getHeight());  // Θάλασσα στο κάτω μέρος
        
        // Ζωγραφίζουμε τον ουρανό
        g.setColor(new Color(135, 206, 250));  // Ουρανός (ανοιχτό μπλε)
        g.fillRect(0, 0, getWidth(), 250);  // Ουρανός πάνω από τη θάλασσα
        
        // Ζωγραφίζουμε το παραδοσιακό σπίτι
        g.setColor(Color.WHITE);  // Χρώμα για το σπίτι
        g.fillRect(200, 150, 150, 100);  // Κύριο σώμα του σπιτιού

        g.setColor(new Color(69, 43, 43));  // Χρώμα για την πόρτα
        g.fillRect(245, 200, 30, 50);  // Πόρτα του σπιτιού

        g.setColor(new Color(0, 0, 0));  // Χρώμα για την οροφή
        Polygon roof = new Polygon();
        roof.addPoint(200, 150);  // Κορυφή της στέγης
        roof.addPoint(350, 150);  // Κορυφή της στέγης
        roof.addPoint(275, 100);  // Κορυφή της στέγης
        g.fillPolygon(roof);  // Στέγη
        
        // Ζωγραφίζουμε το ηφαίστειο στο βάθος
        g.setColor(new Color(169, 169, 169));  // Χρώμα για το ηφαίστειο
        g.fillArc(50, 300, 150, 100, 0, 180);  // Ηφαίστειο

        // Ζωγραφίζουμε μερικές βάρκες στη θάλασσα
        g.setColor(new Color(255, 69, 0));  // Χρώμα για βάρκα
        g.fillOval(120, 320, 30, 15);  // Μικρή βάρκα
        g.setColor(new Color(255, 255, 255));  // Λευκό για το πανί
        g.fillPolygon(new int[] {135, 140, 130}, new int[] {320, 310, 310}, 3);  // Πανί βάρκας
        
        g.setColor(new Color(255, 69, 0));  // Άλλη βάρκα
        g.fillOval(280, 350, 30, 15);  // Δεύτερη βάρκα
        g.setColor(new Color(255, 255, 255));  // Λευκό για το πανί
        g.fillPolygon(new int[] {295, 300, 290}, new int[] {350, 340, 340}, 3);  // Πανί βάρκας
    }

    public static void main(String[] args) {
        JFrame frame = new JFrame("Santorini Drawing");
        SantoriniDrawing panel = new SantoriniDrawing();

        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setSize(600, 600);
        frame.add(panel);
        frame.setVisible(true);
    }
}
