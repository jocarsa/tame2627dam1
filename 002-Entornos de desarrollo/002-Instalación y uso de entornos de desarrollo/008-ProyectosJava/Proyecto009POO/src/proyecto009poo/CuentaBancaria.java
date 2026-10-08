package proyecto009poo;

public class CuentaBancaria {
    private int saldo;
    public CuentaBancaria(){
        saldo = 0;
    }
    public void imponerSaldo(int cantidad){
        if(cantidad < 10000){
            saldo += cantidad;
        }else{
            System.out.println("Cantidad demasiado grande, tienes que pasar por la oficina");
        }
    }
    public void retirarSaldo(int cantidad){
        if(saldo - cantidad > 0){
            saldo -= cantidad;
        }else{
            System.out.println("No tienes fondos para esa operacion");
        }
    }
    public int dimeSaldo(){
        return saldo;
    }
}
