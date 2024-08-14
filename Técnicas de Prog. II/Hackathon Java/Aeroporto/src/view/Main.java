package view;
import model.Voo;
import model.Aeroporto;
import controller.CadastroVoo;

public class Main{
    public static void main(String[] args) {
        Voo voo1 = new Voo();
        Voo voo2 = new Voo();
        Aeroporto aeroporto = new Aeroporto();
        CadastroVoo cadastroVoo = new CadastroVoo(aeroporto);

        voo1.setNumeroVoo("123");
        voo1.setOrigem("SP");
        voo1.setDestino("RJ");
        voo1.setAssentosDisponiveis(50);

        voo2.setNumeroVoo("456");
        voo2.setOrigem("PA");
        voo2.setDestino("MG");
        voo2.setAssentosDisponiveis(60);

        aeroporto.addVoo(voo1);
        aeroporto.addVoo(voo2);

        voo1.imprimirPassagem();
        voo2.realizarPagamento("ida", true);
        aeroporto.exibirVoos();
        cadastroVoo.formularioCadastro();

    }
}