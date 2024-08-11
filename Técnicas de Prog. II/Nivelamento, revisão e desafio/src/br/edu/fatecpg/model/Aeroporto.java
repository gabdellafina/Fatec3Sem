package model;
import java.util.ArrayList;

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
        for (Voo voo : listaVoos) {
            System.out.println(voo);
        }
    }

}
