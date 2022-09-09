public class Tenis extends Thread {
   private static int lastTeamPlay;
   private String palavra;
   private int team;

   public Tenis(String palavra, int team) {
      this.palavra = palavra;
      this.team = team;
   }

   public void run() {
      try {
         for (int i = 0; i < 100; i++) {
            play(this.team, this.palavra, i);
            sleep(100);
         }
      } catch (Exception e) {
         return;
      }
   }

   public static synchronized void play(int team, String palavra, int i) throws Exception {
      if (lastTeamPlay != team) {
         lastTeamPlay = team;
         System.out.print("\n" + palavra + "\t\t:" + i);
      }
   }

   public static void main(String[] args) {
      // Time 1
      Tenis A = new Tenis("Lucas", 1); 
      Tenis B = new Tenis("Aliado", 1);

      // Time 2
      Tenis C = new Tenis("Oponente A", 2);
      Tenis D = new Tenis("Oponente B", 2);

      // Iniciando todas as threads
      A.start();
      B.start();
      C.start();
      D.start();
   }
}