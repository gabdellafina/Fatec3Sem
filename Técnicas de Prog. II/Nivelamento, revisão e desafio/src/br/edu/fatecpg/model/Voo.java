package model;
import javax.swing.*;
import java.awt.*;

public class Voo {
    private String numeroVoo;
    private String origem;
    private String destino;
    private int assentosDisponiveis;

    public Voo () {
    }

    public String getNumeroVoo() {
        return numeroVoo;
    }

    public void setNumeroVoo(String numeroVoo) { this.numeroVoo = numeroVoo; }

    public String getOrigem() {
        return origem;
    }

    public void setOrigem(String origem) { this.origem = origem; }

    public String getDestino() {
        return destino;
    }

    public void setDestino(String destino) { this.destino = destino; }

    public int getAssentosDisponiveis() {
        return assentosDisponiveis;
    }

    public void setAssentosDisponiveis(int assentosDisponiveis) {
        this.assentosDisponiveis = assentosDisponiveis;
    }

    public boolean verificarDisponibilidade(int quantidadeAssentos) {
        if (assentosDisponiveis >= quantidadeAssentos) {
            return true;
        }
        return false;
    }
    
    public boolean realizarReserva(int quantidadeAssentos) {
        if (verificarDisponibilidade(quantidadeAssentos)) {
            assentosDisponiveis -= quantidadeAssentos;
            return true;
        }
        return false;
    }

    public double realizarPagamento(String tipoViagem, boolean pontosTuristicos) {
        if (tipoViagem.equals("ida")) {
            return 50;
        } else {
            if (pontosTuristicos) {
                return 150;
            } else {
                return 100;
            }
        }
    }

    public void imprimirPassagem() {
        System.out.println("Número do voo: " + numeroVoo);
        System.out.println("Origem: " + origem);
        System.out.println("Destino: " + destino);
        System.out.println("Assentos Disponíveis: " + assentosDisponiveis);
    }

}
