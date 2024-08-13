package model;
import java.util.ArrayList;
import javax.swing.*;
import javax.swing.table.DefaultTableModel;

public class Aeroporto {
    private ArrayList<Voo> listaVoos = new ArrayList<Voo>();

    public Aeroporto() {
        this.listaVoos = new ArrayList<>();
    }

    public void addVoo(Voo voo) {
        listaVoos.add(voo);
    }

    public void removeVoo(Voo voo) {
        listaVoos.remove(voo);
    }

    public Voo buscarVoo(String numeroVoo) {
        for (Voo voo : listaVoos) {
            if (voo.getNumeroVoo().equals(numeroVoo)) {
                return voo;
            }
        }
        return null;
    }

    public void exibirVoos() {
        JFrame frame = new JFrame("Tabela de Voos");
        frame.setDefaultCloseOperation(JFrame.DISPOSE_ON_CLOSE);
        frame.setSize(600, 300);

        String[] columnNames = {"Número do Voo", "Origem", "Destino", "Assentos Disponíveis"};
        DefaultTableModel tabelaVoos = new DefaultTableModel(columnNames, 0);

        for (Voo voo : listaVoos) {
            Object[] rowData = {
                    voo.getNumeroVoo(),
                    voo.getOrigem(),
                    voo.getDestino(),
                    voo.getAssentosDisponiveis()
            };
            tabelaVoos.addRow(rowData);
        }

        JTable table = new JTable(tabelaVoos);
        JScrollPane scrollPane = new JScrollPane(table);
        frame.add(scrollPane);

        frame.setLocationRelativeTo(null);
        frame.setVisible(true);
    }

}
