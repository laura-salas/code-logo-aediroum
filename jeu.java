import javafx.scene.canvas.GraphicsContext;
import java.util.ArrayList;

// donc ca c'est le jeu
public class Jeu {
    public static final int HAUTEUR = 480;
    public static final int LARGEUR = 640;

    private ArrayList<Bulles> bulles;
    private Crabe crabetest;
    private Etoile etoileTest;
    private PoissonNormal poissonTest;
    private Balle balleTest;
    private Score score;
    // ca c'est temporaire c'est pour tester si les tires de balles marchaient
    private boolean caExiste;

    private int prochain3Secondes = 0;
    private int prochain5Secondes = 0;
    private int level = 1;

    public Jeu(){
        this.bulles = paquetBulles();
        this.crabetest = new Crabe(level);
        this.etoileTest = new Etoile(level);
        this.poissonTest = new PoissonNormal(level);
        this.caExiste = false;
        this.score = new Score();
    }

    // dessine les éléments selon les conditions
    public void draw (GraphicsContext context){
        for(Bulles b :bulles){
            b.draw(context);
        }
        poissonTest.draw(context);
        if(level>1){
            crabetest.draw(context);
            etoileTest.draw(context);
        }
        if(caExiste){
            balleTest.draw(context);
        }
        this.score.draw(context);

    }

    // permet de update les elements du jeu
    public void update(double dt){

        for(Bulles b :bulles){
            b.update(dt);
        }

        poissonTest.update(dt);

        if(level>1){
            crabetest.update(dt);
            etoileTest.update(dt);
        }

        if(caExiste){
            this.balleTest.update(dt);
            if(this.poissonTest.intersects(this.balleTest)){
                this.score.update();
                caExiste = false;
            }

            if(this.balleTest.getRayon() ==0 && this.poissonTest.intersects(this.balleTest) == false 
){
                caExiste = false;
            }

            this.poissonTest.testCollision(this.balleTest);
        }

        if(this.poissonTest.testSortie()){
            score.perteVie();
            poissonTest.sortirPoisson();
        }
    }

    // ajoute les bulles toutes les 3 secondes
    public void ajoutbulle(double tempsEcoule){
        if(Math.floor(tempsEcoule)==prochain3Secondes){
            this.bulles.clear();
            this.bulles = paquetBulles();
            prochain3Secondes+=3;
            this.poissonTest= new PoissonNormal(level);
        }
    }

    //ajoute des poissonNormaux toutes les 3 secondes
    public void ajoutPoissonNormaux(double tempsEcoule){
        if(Math.floor(tempsEcoule)==prochain3Secondes){
            this.poissonTest= new PoissonNormal(level);
            prochain3Secondes+=3;
        }
    }

    // ajoute les poissons speciaux toutes les 5 secondes
    public void ajoutPoissonSpeciaux(double tempsEcoule){
        if(Math.floor(tempsEcoule)==prochain5Secondes){
            if(level>1) {
                if(Math.random()<0.5){
                    this.etoileTest = new Etoile(level);
                }else{
                    this.crabetest = new Crabe(level);
                }
                prochain5Secondes += 5;
            }
        }
    }

    // permet de créer un pquet des 3 paquet de 5 bulles
    public ArrayList<Bulles> paquetBulles(){
        ArrayList<Bulles> groupeBulles = new ArrayList<Bulles>(3);
        for(int i =0; i<3; i++){
            int positionX = (int)(Math.random()*LARGEUR);
            for(int j = 0; j < 5; j++){
                int positionxBulle = positionX;
                positionxBulle += Math.random()*40;
                groupeBulles.add(new Bulles(positionxBulle, 500));
            }
        }
        return groupeBulles;
    }

    // fait le tire de balle encore temporaire
    public void tire (double xTire, double yTire){
        this.balleTest = new Balle(xTire,yTire);
        caExiste = true;
    }
}
