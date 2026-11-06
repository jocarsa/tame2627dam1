package proyecto013pasarlobienconia;

import javax.swing.*;
import javax.swing.border.*;
import javax.swing.event.*;
import javax.swing.table.*;
import java.awt.*;
import java.awt.event.*;
import java.sql.*;
import java.util.*;
import java.util.List;

public class Agenda {
    static final Color FONDO = new Color(20, 23, 29);
    static final Color PANEL = new Color(29, 33, 41);
    static final Color CAMPO = new Color(38, 43, 53);
    static final Color BORDE = new Color(65, 73, 86);
    static final Color TEXTO = new Color(240, 244, 249);
    static final Color SECUNDARIO = new Color(180, 190, 203);
    static final Color ACENTO = new Color(70, 130, 180); // steelblue
    static final Color SELECCION = new Color(45, 75, 100);
    static final Color PELIGRO = new Color(165, 65, 72);
    static final Font FUENTE = new Font("SansSerif", Font.PLAIN, 14);
    static final String URL = "jdbc:mysql://localhost:3306/javaagenda";
    static final String USUARIO = "javaagenda";
    static final String PASSWORD = "TAME123$";

    static JFrame ventanaListado;
    static JTable tabla;
    static DefaultTableModel modelo;
    static JTextField buscador;
    static JComboBox<String> filtro;
    static JLabel contador;
    static final String[] CATEGORIAS = {"Personal", "Familia", "Amigos", "Trabajo", "Clientes", "Proveedores", "Otros"};

    static Connection conectar() throws SQLException {
        return DriverManager.getConnection(URL, USUARIO, PASSWORD);
    }

    static class Contacto {
        int id;
        String nombre, apellidos, movil, email, empresa, categoria, ciudad;
        Contacto() {}
        Contacto(ResultSet r) throws SQLException {
            id = r.getInt("id"); nombre = r.getString("nombre");
            apellidos = r.getString("apellidos"); movil = r.getString("movil");
            email = r.getString("email"); empresa = r.getString("empresa");
            categoria = r.getString("categoria"); ciudad = r.getString("ciudad");
        }
    }

    static void guardar(Contacto c) throws SQLException {
        boolean editar = c.id > 0;
        String sql = editar
            ? "UPDATE contacto SET nombre=?, apellidos=?, movil=?, email=?, empresa=?, categoria=?, ciudad=? WHERE id=?"
            : "INSERT INTO contacto (nombre, apellidos, movil, email, empresa, categoria, ciudad) VALUES (?,?,?,?,?,?,?)";
        try (Connection con = conectar(); PreparedStatement p = con.prepareStatement(sql)) {
            p.setString(1,c.nombre); p.setString(2,c.apellidos); p.setString(3,c.movil);
            p.setString(4,c.email); p.setString(5,c.empresa); p.setString(6,c.categoria);
            p.setString(7,c.ciudad);
            if (editar) p.setInt(8,c.id);
            p.executeUpdate();
        }
    }

    static void eliminar(int id) throws SQLException {
        try (Connection con=conectar(); PreparedStatement p=con.prepareStatement("DELETE FROM contacto WHERE id=?")) {
            p.setInt(1,id); p.executeUpdate();
        }
    }

    static Contacto obtener(int id) throws SQLException {
        try (Connection con=conectar(); PreparedStatement p=con.prepareStatement("SELECT * FROM contacto WHERE id=?")) {
            p.setInt(1,id);
            try (ResultSet r=p.executeQuery()) { return r.next() ? new Contacto(r) : null; }
        }
    }

    static List<Contacto> consultar(String texto, String categoria) throws SQLException {
        List<Contacto> resultado = new ArrayList<>();
        String sql = "SELECT * FROM contacto WHERE (nombre LIKE ? OR apellidos LIKE ? OR movil LIKE ? OR email LIKE ? OR empresa LIKE ? OR categoria LIKE ? OR ciudad LIKE ?) AND (?='Todas las categorías' OR categoria=?) ORDER BY nombre, apellidos";
        try (Connection con=conectar(); PreparedStatement p=con.prepareStatement(sql)) {
            for (int i=1;i<=7;i++) p.setString(i,"%"+texto+"%");
            p.setString(8,categoria); p.setString(9,categoria);
            try (ResultSet r=p.executeQuery()) { while(r.next()) resultado.add(new Contacto(r)); }
        }
        return resultado;
    }

    static void tema() {
        // Metal respeta los colores y los bordes que definimos; GTK puede sobrescribirlos.
        try { UIManager.setLookAndFeel("javax.swing.plaf.metal.MetalLookAndFeel"); }
        catch (Exception ignored) {}
        UIManager.put("control", PANEL);
        UIManager.put("info", PANEL);
        UIManager.put("nimbusBase", CAMPO);
        UIManager.put("text", TEXTO);
        UIManager.put("Label.foreground", TEXTO);
        UIManager.put("OptionPane.background", PANEL);
        UIManager.put("OptionPane.messageForeground", TEXTO);
        UIManager.put("Panel.background", PANEL);
        UIManager.put("Button.background", CAMPO);
        UIManager.put("Button.foreground", TEXTO);
        UIManager.put("ComboBox.background", CAMPO);
        UIManager.put("ComboBox.foreground", TEXTO);
        UIManager.put("ComboBox.selectionBackground", SELECCION);
        UIManager.put("ComboBox.selectionForeground", TEXTO);
        UIManager.put("ScrollBar.background", PANEL);
        UIManager.put("ScrollBar.thumb", BORDE);
        UIManager.put("Table.background", PANEL);
        UIManager.put("Table.foreground", TEXTO);
        UIManager.put("Table.selectionBackground", SELECCION);
        UIManager.put("Table.selectionForeground", TEXTO);
    }

    static JPanel panel(LayoutManager layout) {
        JPanel p = new JPanel(layout); p.setBackground(PANEL); return p;
    }
    static JLabel etiqueta(String texto) {
        JLabel l=new JLabel(texto); l.setFont(FUENTE); l.setForeground(SECUNDARIO); return l;
    }
    static JLabel titulo(String texto) {
        JLabel l=new JLabel(texto); l.setFont(new Font("SansSerif",Font.BOLD,26)); l.setForeground(TEXTO); return l;
    }
    static JTextField campo() {
        JTextField t=new JTextField(); t.setFont(FUENTE); t.setForeground(TEXTO);
        t.setCaretColor(TEXTO); t.setBackground(CAMPO); t.setOpaque(true);
        t.setSelectionColor(SELECCION); t.setSelectedTextColor(TEXTO);
        t.setBorder(new CompoundBorder(new LineBorder(BORDE,1),new EmptyBorder(9,12,9,12)));
        t.setPreferredSize(new Dimension(200,42)); return t;
    }
    static JButton boton(String texto, Color fondo) {
        JButton b=new JButton(texto); b.setFont(FUENTE); b.setForeground(TEXTO);
        b.setBackground(fondo); b.setOpaque(true); b.setContentAreaFilled(true);
        b.setBorderPainted(true); b.setFocusPainted(false);
        b.setBorder(new CompoundBorder(new LineBorder(fondo.equals(CAMPO)?BORDE:fondo,1),new EmptyBorder(10,17,10,17)));
        b.setCursor(Cursor.getPredefinedCursor(Cursor.HAND_CURSOR));
        return b;
    }
    static JComboBox<String> combo(String[] valores) {
        JComboBox<String> c=new JComboBox<>(valores); c.setFont(FUENTE);
        c.setBackground(CAMPO); c.setForeground(TEXTO); c.setOpaque(true);
        c.setBorder(new LineBorder(BORDE,1));
        c.setRenderer(new DefaultListCellRenderer() {
            @Override public Component getListCellRendererComponent(JList<?> list,Object value,int index,boolean selected,boolean focus) {
                JLabel l=(JLabel)super.getListCellRendererComponent(list,value,index,selected,focus);
                l.setOpaque(true); l.setBackground(selected?SELECCION:CAMPO);
                l.setForeground(TEXTO); l.setBorder(new EmptyBorder(8,10,8,10)); return l;
            }
        });
        c.setPreferredSize(new Dimension(205,42)); return c;
    }
    static void error(Component padre,Exception ex) {
        JOptionPane.showMessageDialog(padre,"Error de base de datos:\n"+ex.getMessage(),"Error",JOptionPane.ERROR_MESSAGE);
    }

    static void formulario(Contacto existente) {
        boolean edicion=existente!=null;
        JFrame frame=new JFrame(edicion?"JOCARSA | Editar contacto":"JOCARSA | Nuevo contacto");
        frame.setDefaultCloseOperation(JFrame.DISPOSE_ON_CLOSE);
        frame.setSize(680,660); frame.setMinimumSize(new Dimension(550,590));
        frame.setLocationRelativeTo(ventanaListado);
        JPanel raiz=new JPanel(new BorderLayout(0,22)); raiz.setBackground(FONDO);
        raiz.setBorder(new EmptyBorder(28,30,28,30));
        raiz.add(titulo(edicion?"Editar contacto":"Nuevo contacto"),BorderLayout.NORTH);
        JPanel cuerpo=panel(new GridBagLayout()); cuerpo.setBorder(new CompoundBorder(new LineBorder(BORDE),new EmptyBorder(22,24,22,24)));
        JTextField nombre=campo(), apellidos=campo(), movil=campo(), email=campo(), empresa=campo(), ciudad=campo();
        JComboBox<String> categoria=combo(CATEGORIAS);
        String[] etiquetas={"Nombre *","Apellidos","Móvil","Email","Empresa","Categoría","Ciudad"};
        JComponent[] controles={nombre,apellidos,movil,email,empresa,categoria,ciudad};
        GridBagConstraints g=new GridBagConstraints(); g.fill=GridBagConstraints.HORIZONTAL;
        g.insets=new Insets(8,6,8,10);
        for(int i=0;i<etiquetas.length;i++) {
            g.gridy=i; g.gridx=0; g.weightx=0; cuerpo.add(etiqueta(etiquetas[i]),g);
            g.gridx=1; g.weightx=1; cuerpo.add(controles[i],g);
        }
        raiz.add(cuerpo,BorderLayout.CENTER);
        if(edicion) {
            nombre.setText(existente.nombre); apellidos.setText(existente.apellidos);
            movil.setText(existente.movil); email.setText(existente.email);
            empresa.setText(existente.empresa); ciudad.setText(existente.ciudad);
            if(existente.categoria!=null) categoria.setSelectedItem(existente.categoria);
        }
        JPanel acciones=new JPanel(new FlowLayout(FlowLayout.RIGHT,10,0)); acciones.setOpaque(false);
        JButton cancelar=boton("Cancelar",CAMPO), guardar=boton(edicion?"Guardar cambios":"Crear contacto",ACENTO);
        cancelar.addActionListener(e->frame.dispose());
        guardar.addActionListener(e->{
            if(nombre.getText().trim().isEmpty()) { JOptionPane.showMessageDialog(frame,"El nombre es obligatorio"); nombre.requestFocus(); return; }
            Contacto c=new Contacto(); c.id=edicion?existente.id:0;
            c.nombre=nombre.getText().trim(); c.apellidos=apellidos.getText().trim();
            c.movil=movil.getText().trim(); c.email=email.getText().trim();
            c.empresa=empresa.getText().trim(); c.categoria=Objects.toString(categoria.getSelectedItem(),"");
            c.ciudad=ciudad.getText().trim();
            try { guardar(c); cargarTabla(); frame.dispose(); } catch(SQLException ex) { error(frame,ex); }
        });
        acciones.add(cancelar); acciones.add(guardar); raiz.add(acciones,BorderLayout.SOUTH);
        frame.setContentPane(raiz); frame.setVisible(true);
    }

    static int idSeleccionado() {
        int fila=tabla.getSelectedRow();
        if(fila<0) { JOptionPane.showMessageDialog(ventanaListado,"Selecciona un contacto"); return -1; }
        return (Integer)modelo.getValueAt(tabla.convertRowIndexToModel(fila),0);
    }
    static void editarSeleccionado() {
        int id=idSeleccionado(); if(id<0)return;
        try { Contacto c=obtener(id); if(c!=null) formulario(c); else JOptionPane.showMessageDialog(ventanaListado,"El contacto ya no existe"); }
        catch(SQLException ex){error(ventanaListado,ex);}
    }
    static void cargarTabla() {
        if(modelo==null)return;
        try {
            List<Contacto> lista=consultar(buscador.getText().trim(),Objects.toString(filtro.getSelectedItem(),"Todas las categorías"));
            modelo.setRowCount(0);
            for(Contacto c:lista)modelo.addRow(new Object[]{c.id,c.nombre,c.apellidos,c.movil,c.email,c.empresa,c.categoria,c.ciudad});
            contador.setText(lista.size()+" contactos visibles");
        } catch(SQLException ex){error(ventanaListado,ex);}
    }

    static void ventanaListado() {
        ventanaListado=new JFrame("JOCARSA | Agenda");
        ventanaListado.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        ventanaListado.setSize(1250,760); ventanaListado.setMinimumSize(new Dimension(850,550));
        ventanaListado.setLocationRelativeTo(null);
        JPanel raiz=new JPanel(new BorderLayout(0,22)); raiz.setBackground(FONDO);
        raiz.setBorder(new EmptyBorder(28,30,28,30));
        JPanel cabecera=new JPanel(new BorderLayout()); cabecera.setOpaque(false);
        cabecera.add(titulo("JOCARSA | Agenda"),BorderLayout.WEST);
        JButton nuevo=boton("+ Nuevo contacto",ACENTO); nuevo.addActionListener(e->formulario(null));
        cabecera.add(nuevo,BorderLayout.EAST); raiz.add(cabecera,BorderLayout.NORTH);
        JPanel centro=new JPanel(new BorderLayout(0,16)); centro.setOpaque(false);
        JPanel herramientas=new JPanel(new BorderLayout(14,0)); herramientas.setOpaque(false);
        buscador=campo(); buscador.setToolTipText("Buscar por nombre, móvil, email, empresa, categoría o ciudad");
        String[] filtros=new String[CATEGORIAS.length+1]; filtros[0]="Todas las categorías";
        System.arraycopy(CATEGORIAS,0,filtros,1,CATEGORIAS.length);
        filtro=combo(filtros);
        herramientas.add(buscador,BorderLayout.CENTER); herramientas.add(filtro,BorderLayout.EAST);
        centro.add(herramientas,BorderLayout.NORTH);
        modelo=new DefaultTableModel(new String[]{"ID","Nombre","Apellidos","Móvil","Email","Empresa","Categoría","Ciudad"},0){
            @Override public boolean isCellEditable(int r,int c){return false;}
            @Override public Class<?> getColumnClass(int c){return c==0?Integer.class:String.class;}
        };
        tabla=new JTable(modelo); tabla.setFont(FUENTE); tabla.setRowHeight(44);
        tabla.setBackground(PANEL); tabla.setForeground(TEXTO); tabla.setSelectionBackground(SELECCION);
        tabla.setSelectionForeground(TEXTO); tabla.setGridColor(BORDE); tabla.setShowVerticalLines(false);
        tabla.setFillsViewportHeight(true); tabla.setAutoCreateRowSorter(true);
        tabla.setSelectionMode(ListSelectionModel.SINGLE_SELECTION);
        tabla.setDefaultRenderer(Object.class,new DefaultTableCellRenderer(){
            @Override public Component getTableCellRendererComponent(JTable t,Object v,boolean selected,boolean focus,int row,int col){
                JLabel l=(JLabel)super.getTableCellRendererComponent(t,v,selected,focus,row,col);
                l.setBackground(selected?SELECCION:(row%2==0?PANEL:CAMPO)); l.setForeground(TEXTO);
                l.setBorder(new EmptyBorder(0,12,0,8)); return l;
            }
        });
        JTableHeader h=tabla.getTableHeader(); h.setReorderingAllowed(false);
        h.setFont(new Font("SansSerif",Font.BOLD,13)); h.setBackground(CAMPO); h.setForeground(TEXTO);
        h.setPreferredSize(new Dimension(100,46));
        h.setDefaultRenderer((t,value,selected,focus,row,col)->{
            JLabel l=new JLabel(value.toString()); l.setOpaque(true); l.setBackground(CAMPO); l.setForeground(TEXTO);
            l.setFont(new Font("SansSerif",Font.BOLD,13));
            l.setBorder(new CompoundBorder(new MatteBorder(0,0,1,1,BORDE),new EmptyBorder(0,12,0,8)));
            return l;
        });
        tabla.getColumnModel().getColumn(0).setPreferredWidth(55);
        JScrollPane scroll=new JScrollPane(tabla); scroll.setBorder(new LineBorder(BORDE));
        scroll.getViewport().setBackground(PANEL); scroll.setBackground(PANEL);
        centro.add(scroll,BorderLayout.CENTER);
        JPanel inferior=new JPanel(new BorderLayout()); inferior.setOpaque(false);
        contador=etiqueta("0 contactos visibles"); inferior.add(contador,BorderLayout.WEST);
        JPanel acciones=new JPanel(new FlowLayout(FlowLayout.RIGHT,10,0)); acciones.setOpaque(false);
        JButton actualizar=boton("Actualizar",CAMPO), editar=boton("Editar",CAMPO), borrar=boton("Eliminar",PELIGRO);
        actualizar.addActionListener(e->cargarTabla()); editar.addActionListener(e->editarSeleccionado());
        borrar.addActionListener(e->{
            int id=idSeleccionado(); if(id<0)return;
            if(JOptionPane.showConfirmDialog(ventanaListado,"¿Eliminar el contacto seleccionado?","Confirmar eliminación",JOptionPane.YES_NO_OPTION)==JOptionPane.YES_OPTION){
                try {eliminar(id); cargarTabla();}catch(SQLException ex){error(ventanaListado,ex);}
            }
        });
        acciones.add(actualizar); acciones.add(editar); acciones.add(borrar);
        inferior.add(acciones,BorderLayout.EAST); centro.add(inferior,BorderLayout.SOUTH);
        raiz.add(centro,BorderLayout.CENTER);
        buscador.getDocument().addDocumentListener(new DocumentListener(){
            public void insertUpdate(DocumentEvent e){cargarTabla();}
            public void removeUpdate(DocumentEvent e){cargarTabla();}
            public void changedUpdate(DocumentEvent e){cargarTabla();}
        });
        filtro.addActionListener(e->cargarTabla());
        tabla.addMouseListener(new MouseAdapter(){@Override public void mouseClicked(MouseEvent e){if(e.getClickCount()==2)editarSeleccionado();}});
        ventanaListado.setContentPane(raiz); cargarTabla(); ventanaListado.setVisible(true);
    }

    public static void main(String[] args){
        if(PASSWORD==null || PASSWORD.isEmpty()) {System.err.println("Define JAVAAGENDA_DB_PASSWORD antes de ejecutar.");return;}
        SwingUtilities.invokeLater(()->{tema();ventanaListado();});
    }
}