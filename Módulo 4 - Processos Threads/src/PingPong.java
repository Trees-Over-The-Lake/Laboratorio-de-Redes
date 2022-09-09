public class PingPong extends Thread {
   private static int lastTeamPlay;
   private String palavra;

   public PingPong(String palavra) {
      this.palavra = palavra;
   }

   public void run() {
      try {
         for (int i = 0; i < 10; i++) {

            if ((palavra.equals("ping A") || palavra.equals("ping B")) && lastTeamPlay == 2) { // Se for o time A/B
               play(1);
               Thread.sleep(100);
            } else { // Se for o time C/D
               play(2);
               Thread.sleep(100);
            }
            System.out.print("\n" + palavra + " "
                  + " : " + i);
         }
      } catch (InterruptedException e) {
         return;
      }
   }

   public static synchronized void play(int team) {
      if (lastTeamPlay != team)
         lastTeamPlay = team;
   }

   public static void main(String[] args) {
      Thread A = new PingPong("ping A");
      Thread B = new PingPong("ping B");
      Thread C = new PingPong("pong C");
      Thread D = new PingPong("pong D");

      A.start();
      B.start();
      C.start();
      D.start();
   }
}