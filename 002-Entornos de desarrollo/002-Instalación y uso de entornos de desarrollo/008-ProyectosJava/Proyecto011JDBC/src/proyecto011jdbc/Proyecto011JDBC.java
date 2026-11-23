package proyecto011jdbc;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.Statement;
import java.sql.ResultSet;

public class Proyecto011JDBC {

    public static void main(String[] args) {
        // TODO code application logic here
        String direccion = "jdbc:mysql://localhost:3306/tiendaonlinetame";
        String usuario = "tiendaonlinetame";
        String contrasena = "TAME123$";
        // Intenta conectarte y si no lo consigues pues no te cuelgues
        try{
            Connection miconexion = DriverManager.getConnection(direccion, usuario, contrasena);
            Statement sentencia = miconexion.createStatement(); // Te voy a pedir algo
            ResultSet miresultado = sentencia.executeQuery("SELECT * FROM productos;");
            while(miresultado.next()){
                System.out.println(miresultado.getString("nombre"));
                System.out.println(miresultado.getString("descripcion"));
                System.out.println(miresultado.getDouble("precio"));
                System.out.println("---------------------------------------");
            }
            miconexion.close();
            miresultado.close();
            sentencia.close();
        }catch(Exception e){
            e.printStackTrace();
        }
    }
    
}
