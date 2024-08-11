package view;
import model.Voo;
import model.Aeroporto;

public class Main{
    public static void main(String[] args) {
        Voo voo1 = new Voo();
        Voo voo2 = new Voo();
        Aeroporto aeroporto = new Aeroporto();

        voo1.setNumeroVoo("123");
        voo1.setOrigem("SP");
        voo1.setDestino("RJ");
        voo1.setAssentosDisponiveis(50);

        voo2.setNumeroVoo("456");
        voo2.setOrigem("PA");
        voo2.setDestino("MG");
        voo2.setAssentosDisponiveis(60);

        voo1.imprimirPassagem();
        voo2.realizarPagamento("ida", true);
        aeroporto.exibirVoos();
        aeroporto.buscarVoo("123");
    }
}