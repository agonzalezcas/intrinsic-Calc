import java.awt.*;
import java.awt.event.ActionEvent;

import javax.swing.*;
import javax.swing.event.*;

public class IntrinsicValueGUI extends JFrame implements Action {

	public IntrinsicValueGUI() {

        Container c = getContentPane();
        JPanel mainPanel = new JPanel();
        mainPanel.setLayout(new GridLayout(2, 8));

        JLabel label1 = new JLabel("Enter Value: ");
        JTextField textfield1 = new JTextField(2);
        JLabel label2 = new JLabel("Enter Value: ");
        JTextField textfield2 = new JTextField(2);
        JLabel label3 = new JLabel("Enter Value: ");
        JTextField textfield3 = new JTextField(2);
        JLabel label4 = new JLabel("Enter Value: ");
        JTextField textfield4 = new JTextField(2);

        JLabel label5 = new JLabel("Enter Value: ");
        JTextField textfield5 = new JTextField(2);
        JLabel label6 = new JLabel("Enter Value: ");
        JTextField textfield6 = new JTextField(2);
        JLabel label7 = new JLabel("Enter Value: ");
        JTextField textfield7 = new JTextField(2);
        JLabel label8 = new JLabel("Enter Value: ");
        JTextField textfield8 = new JTextField(2);



		setSize(400,400);
		setVisible(true);
		mainPanel.add(label1);
		mainPanel.add(textfield1);
		mainPanel.add(label2);
		mainPanel.add(textfield2);
		mainPanel.add(label3);
		mainPanel.add(textfield3);
		mainPanel.add(label4);
		mainPanel.add(textfield4);

		mainPanel.add(label5);
		mainPanel.add(textfield5);
		mainPanel.add(label6);
		mainPanel.add(textfield6);
		mainPanel.add(label7);
		mainPanel.add(textfield7);
		mainPanel.add(label8);
		mainPanel.add(textfield8);

		bottomButtons();

		c.add(mainPanel);
		//c.add(bottomPanel);


	}

	public void bottomButtons() {
		JPanel bottomPanel = new JPanel();
		JButton buutton1 = new JButton("Calculate");
        JButton button2 = new JButton("Reset");
        button1.addActionListener(this);

        bottomPanel.add(button1);
		bottomPanel.add(button2);

	}

	  public void actionPerformed(ActionEvent e) {

	  }


	public static void main(String[] args)
	{
		new IntrinsicValueGUI();

	}



}
