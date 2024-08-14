package model;
import java.util.ArrayList;

public class Treinamento {
    private int id;
    private String nomeInstrutor;
    private String linguagemEnsinada;
    private ArrayList<Aluno> alunos = new ArrayList<Aluno>();
    protected int cargaHoraria;

    public Treinamento(int id, String nomeInstrutor, String linguagemEnsinada) {
        this.id = id;
        this.nomeInstrutor = nomeInstrutor;
        this.linguagemEnsinada = linguagemEnsinada;
    }

    public void adicionarAluno(Aluno aluno) {
        alunos.add(aluno);
    }

    public void verificarDisponibilidade() {
        // nao sei
    }

    public void definirCargaHoraria(int horas) {
        this.cargaHoraria = horas;
    }

    public void verificarUltimoTreinamento(Aluno aluno) {
        // nao sei
    }

    public double calcularMediaAlunos() {
        double soma = 0;
        for (Aluno aluno : alunos) {
            soma += aluno.getNotaFinal();
        }
        return soma / alunos.size();
    }
}


