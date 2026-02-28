public class Quaterion {
    protected double scalar = 0;
    protected double i = 0;
    protected double j = 0;
    protected double k = 0;

    public Quaterion() {}

    public Quaterion(double scalar) {
        this.scalar = scalar;
    }

    public Quaterion(double scalar, double i) {
        this.scalar = scalar;
        this.i = i;
    }

    public Quaterion(double scalar, double i, double j) {
        this.scalar = scalar;
        this.i = i;
        this.j = j;
    }

    public Quaterion(double scalar, double i, double j, double k) {
        this.scalar = scalar;
        this.i = i;
        this.j = j;
        this.k = k;
    }

    public String display() {
        String sstring = "" + this.scalar;
        String istring = (this.i < 0 ? " - " : " + ") + Math.abs(this.i) + "i";
        String jstring = (this.j < 0 ? " - " : " + ") + Math.abs(this.j) + "j";
        String kstring = (this.k < 0 ? " - " : " + ") + Math.abs(this.k) + "k";
        return sstring + istring + jstring + kstring;
    }

    public double getScalar() {
        return this.scalar;
    }

    public double getI() {
        return this.i;
    }

    public double getJ() {
        return this.j;
    }

    public double getK() {
        return this.k;
    }

    public Quaterion add(Quaterion other) {
        double s = this.scalar + other.getScalar();
        double i = this.i + other.getI();
        double j = this.j + other.getJ();
        double k = this.k + other.getK();
        return new Quaterion(s, i, j, k);
    }

    public Quaterion mul(Quaterion other) {
        double s = this.scalar * other.getScalar() - this.i * other.getI() - this.j * other.getJ() - this.k * other.getK();
        double i = this.scalar * other.getI() + this.i * other.getScalar() + this.j * other.getK() - this.k * other.getJ();
        double j = this.scalar * other.getJ() - this.i * other.getK() + this.j * other.getScalar() + this.k * other.getI();
        double k = this.scalar * other.getK() + this.i * other.getJ() - this.j * other.getI() + this.k * other.getScalar();
        return new Quaterion(s, i, j, k);
    }

    public static void main(String[] args) {
        Quaterion q1 = new Quaterion(3, -1, 8, 2);
        Quaterion q2 = new Quaterion(-11, -3, 5, -4);

        System.out.println(q1.add(q2).display());
        System.out.println(q1.mul(q2).display());

        Quaterion q3 = new Quaterion(3, -1, 8);
        Quaterion q4 = new Quaterion(3, -1);
        Quaterion q5 = new Quaterion(3);
        Quaterion q6 = new Quaterion();
        System.out.println(q3.display());
        System.out.println(q4.display());
        System.out.println(q5.display());
        System.out.println(q6.display());
    }
    
}
