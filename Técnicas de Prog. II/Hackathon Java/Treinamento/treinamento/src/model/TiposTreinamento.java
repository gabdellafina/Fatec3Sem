package model;

public class TiposTreinamento {

    class TreinamentoPresencial extends Treinamento {
        private String local;

        public TreinamentoPresencial(int id, String nomeInstrutor, String linguagemEnsinada, String local) {
            super(id, nomeInstrutor, linguagemEnsinada);
            this.local = local;
        }

        public String getTipo() {
            return "Presencial";
        }

        public String getLocal() {
            return local;
        }
    }

    class TreinamentoOnline extends Treinamento {
        private String linkAcesso;

        public TreinamentoOnline(int id, String nomeInstrutor, String linguagemEnsinada, String linkAcesso) {
            super(id, nomeInstrutor, linguagemEnsinada);
            this.linkAcesso = linkAcesso;
        }

        public String getTipo() {
            return "Online";
        }

        public String getLinkAcesso() {
            return linkAcesso;
        }
    }
}
