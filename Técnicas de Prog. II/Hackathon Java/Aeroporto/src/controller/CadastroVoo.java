package controller;
import model.Aeroporto;
import model.Voo;
import javax.swing.*;
import java.awt.*;

public class CadastroVoo {
    private Aeroporto aeroporto;

    public CadastroVoo(Aeroporto aeroporto) {
        this.aeroporto = aeroporto;
    }

    public void formularioCadastro() {
        JFrame f = new JFrame("Cadastro de Voo");
        f.setDefaultCloseOperation(JFrame.DISPOSE_ON_CLOSE);
        f.setSize(300, 200);
        f.setLayout(new GridLayout(5, 2));

        JLabel labelNumero = new JLabel("Número do Voo:");
        JTextField textNumero = new JTextField();

        JLabel labelOrigem = new JLabel("Origem:");
        JTextField textOrigem = new JTextField();

        JLabel labelDestino = new JLabel("Destino:");
        JTextField textDestino = new JTextField();

        JLabel labelAssentos = new JLabel("Assentos Disponíveis:");
        JTextField textAssentos = new JTextField();

        JButton Salvar = new JButton("Salvar");
        Salvar.addActionListener(e -> {
            String numeroVoo = textNumero.getText();
            String origem = textOrigem.getText();
            String destino = textDestino.getText();
            int assentosDisponiveis = Integer.parseInt(textAssentos.getText());

            Voo voo = new Voo();
            voo.setNumeroVoo(numeroVoo);
            voo.setOrigem(origem);
            voo.setDestino(destino);
            voo.setAssentosDisponiveis(assentosDisponiveis);

            aeroporto.addVoo(voo);

            textNumero.setText("");
            textOrigem.setText("");
            textDestino.setText("");
            textAssentos.setText("");
        });

        f.add(labelNumero);
        f.add(textNumero);
        f.add(labelOrigem);
        f.add(textOrigem);
        f.add(labelDestino);
        f.add(textDestino);
        f.add(labelAssentos);
        f.add(textAssentos);
        f.add(Salvar);

        f.setLocationRelativeTo(null);
        f.setVisible(true);
    }
}
