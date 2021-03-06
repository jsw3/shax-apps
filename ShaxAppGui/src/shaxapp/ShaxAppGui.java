package shaxapp;

import javax.swing.JComboBox;
import org.xml.sax.InputSource;
import javax.xml.xpath.*;

/**
 *
 * @author JoeWallace
 * 
 * the XML file was generated by a Python script I also wrote, which uses 
 * regular expressions to extract the text of Shakespeare's plays from 
 * the text of his First Folio. It also generates information about each 
 * play, some of which is included in the XML file and displayed in this application. 
 * This is a basic template from which to develop a potentially more complex
 * GUI able to display different kinds of data.
 */
public class ShaxAppGui extends javax.swing.JFrame {

    /**
     * Creates new form ShaxAppGui
     */
    public ShaxAppGui() {
        initComponents();
    }

    /**
     * This method is called from within the constructor to initialize the form.
     * WARNING: Do NOT modify this code. The content of this method is always
     * regenerated by the Form Editor.
     */
    @SuppressWarnings("unchecked")
    
    // <editor-fold defaultstate="collapsed" desc="Generated Code">//GEN-BEGIN:initComponents
    private void initComponents() {

        jLabel1 = new javax.swing.JLabel();
        jComboBox2 = new javax.swing.JComboBox<>();
        jLabel3 = new javax.swing.JLabel();
        jScrollPane2 = new javax.swing.JScrollPane();
        jTextPane1 = new javax.swing.JTextPane();

        setDefaultCloseOperation(javax.swing.WindowConstants.EXIT_ON_CLOSE);
        setTitle("First Folio Info");
        setLocation(new java.awt.Point(100, 100));
        setResizable(false);

        jLabel1.setText("Select a Play");

        jComboBox2.setModel(new javax.swing.DefaultComboBoxModel<>(new String[] { "Shakespeare's First Folio", "The Tempest", "The Two Gentlemen of Verona", "The Merry Wiues of Windsor", "Measvre, For Measure", "The Comedie of Errors", "Much adoe about Nothing", "Loues Labour's lost", "A Midsommer Nights Dreame", "The Merchant of Venice", "As you Like it", "The Taming of the Shrew", "All's Well, that Ends Well", "Twelfe Night, Or what you will", "The Winters Tale", "The life and death of King John", "The life and death of King Richard the Second", "The First Part of Henry the Fourth", "The Second Part of Henry the Fourth", "The Life of Henry the Fift", "The first Part of Henry the Sixt", "The second Part of Henry the Sixt", "The third Part of Henry the Sixt", "The Tragedie of Richard the Third", "The Famous History of the Life of King Henry the Eight", "The Tragedie of Coriolanus", "The Tragedie of Titus Andronicus", "The Tragedie of Romeo and Juliet", "The Life of Timon of Athens", "The Tragedie of Julius Caesar", "The Tragedie of Macbeth", "The Tragedie of Hamlet", "The Tragedie of King Lear", "The Tragedie of Othello, the Moore of Venice", "The Tragedie of Anthonie, and Cleopatra", "The Tragedie of Cymbeline" }));
        jComboBox2.setCursor(new java.awt.Cursor(java.awt.Cursor.DEFAULT_CURSOR));
        jComboBox2.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                changePlay(evt);
            }
        });

        jLabel3.setHorizontalAlignment(javax.swing.SwingConstants.CENTER);
        jLabel3.setIcon(new javax.swing.ImageIcon(getClass().getResource("/shaxapp/ff_image.jpg"))); // NOI18N
        jLabel3.setText("jLabel3");

        jScrollPane2.setBackground(new java.awt.Color(238, 238, 238));
        jScrollPane2.setBorder(null);
        jScrollPane2.setForeground(new java.awt.Color(238, 238, 238));

        jTextPane1.setEditable(false);
        jTextPane1.setBackground(new java.awt.Color(238, 238, 238));
        jTextPane1.setBorder(null);
        jTextPane1.setContentType("text/html"); // NOI18N
        jTextPane1.setText("<html>\n  <head>\n\n  </head>\n  <body>\n    <p style=\"margin-top: 0; font-family:Lucida Grande; font-size:13pt\">\nPlay: Shakespeare's First Folio<br><br>\nDate: 1623<br><br>\nWords: 830, 568<br><br>\nLexical Variety: 5.06 %<br><br>\nFiction vs Non-Fiction Score: 35.46%\n      \n    </p>\n  </body>\n</html>\n");
        jScrollPane2.setViewportView(jTextPane1);

        javax.swing.GroupLayout layout = new javax.swing.GroupLayout(getContentPane());
        getContentPane().setLayout(layout);
        layout.setHorizontalGroup(
            layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(layout.createSequentialGroup()
                .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                    .addGroup(layout.createSequentialGroup()
                        .addGap(19, 19, 19)
                        .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                            .addComponent(jLabel3, javax.swing.GroupLayout.PREFERRED_SIZE, 464, javax.swing.GroupLayout.PREFERRED_SIZE)
                            .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.TRAILING)
                                .addComponent(jScrollPane2, javax.swing.GroupLayout.PREFERRED_SIZE, 394, javax.swing.GroupLayout.PREFERRED_SIZE)
                                .addComponent(jComboBox2, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE))))
                    .addGroup(layout.createSequentialGroup()
                        .addGap(27, 27, 27)
                        .addComponent(jLabel1)))
                .addContainerGap(22, Short.MAX_VALUE))
        );
        layout.setVerticalGroup(
            layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(layout.createSequentialGroup()
                .addGap(30, 30, 30)
                .addComponent(jLabel1)
                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                .addComponent(jComboBox2, javax.swing.GroupLayout.PREFERRED_SIZE, 27, javax.swing.GroupLayout.PREFERRED_SIZE)
                .addGap(5, 5, 5)
                .addComponent(jScrollPane2, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)
                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                .addComponent(jLabel3, javax.swing.GroupLayout.PREFERRED_SIZE, 270, javax.swing.GroupLayout.PREFERRED_SIZE)
                .addContainerGap(32, Short.MAX_VALUE))
        );

        pack();
    }// </editor-fold>//GEN-END:initComponents

    private void changePlay(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_changePlay
        /* this changes the value of the text field using the getter function below */
        
        JComboBox cb = (JComboBox)evt.getSource();
        
        String play = (String)cb.getSelectedItem();
        String filename = "src/shaxapp/FolioXML.xml";
        String expression = "//play[@playTitle=\""+play+"\"]/";
        
        String date = getXMLValue(expression+"date", filename);
        String words = getXMLValue(expression+"words", filename);
        String lexical_variety = getXMLValue(expression+"lex_var", filename);
        String fiction_v_non = getXMLValue(expression+"fic_non", filename);
        
        jTextPane1.setText("<html><p style=\"margin-top:0; font-family:Lucida Grande; font-size:13pt\">Play: "
                +play+"<br><br>Date: "+date+
                "<br><br>Words: "+words+"<br><br>Lexical Variety: "+
                lexical_variety+"<br><br>Fiction vs Nonfiction Score: "+
                fiction_v_non+"</p></html>");
    }//GEN-LAST:event_changePlay
    
    private String getXMLValue(String expression, String filename) {
        /* a function that reads an XML file and returns a value */      
        
        XPath xpath = XPathFactory.newInstance().newXPath();
        InputSource inputSource = new InputSource(filename);
        String exception = "no results";
        try {
            String result = xpath.evaluate(expression, inputSource);
            return result;
        } catch (XPathExpressionException e) {
            return exception;
        }
    }
    /**
     * @param args the command line arguments
     */
    public static void main(String args[]) {
        /* Set the Nimbus look and feel */
        //<editor-fold defaultstate="collapsed" desc=" Look and feel setting code (optional) ">
        /* If Nimbus (introduced in Java SE 6) is not available, stay with the default look and feel.
         * For details see http://download.oracle.com/javase/tutorial/uiswing/lookandfeel/plaf.html 
         */
        /*try {
            for (javax.swing.UIManager.LookAndFeelInfo info : javax.swing.UIManager.getInstalledLookAndFeels()) {
                if ("Nimbus".equals(info.getName())) {
                    javax.swing.UIManager.setLookAndFeel(info.getClassName());
                    break;
                }
            }
        } catch (ClassNotFoundException ex) {
            java.util.logging.Logger.getLogger(ShaxAppGui.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        } catch (InstantiationException ex) {
            java.util.logging.Logger.getLogger(ShaxAppGui.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        } catch (IllegalAccessException ex) {
            java.util.logging.Logger.getLogger(ShaxAppGui.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        } catch (javax.swing.UnsupportedLookAndFeelException ex) {
            java.util.logging.Logger.getLogger(ShaxAppGui.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        }
        //</editor-fold>
        */

        /* Create and display the form */
        java.awt.EventQueue.invokeLater(new Runnable() {
            @Override
            public void run() {
                new ShaxAppGui().setVisible(true);
            }
        });
    }

    // Variables declaration - do not modify//GEN-BEGIN:variables
    private javax.swing.JComboBox<String> jComboBox2;
    private javax.swing.JLabel jLabel1;
    private javax.swing.JLabel jLabel3;
    private javax.swing.JScrollPane jScrollPane2;
    private javax.swing.JTextPane jTextPane1;
    // End of variables declaration//GEN-END:variables
}

