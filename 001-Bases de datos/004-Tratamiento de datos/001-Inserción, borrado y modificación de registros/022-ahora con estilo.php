<!doctype html>
<html>
	<head>
  	
    <style>
      * {
        box-sizing: border-box;
      }

      body {
        margin: 0;
        padding: 40px;
        background: #f4f6f8;
        font-family: Arial, sans-serif;
        color: #333;
        min-height: 100vh;
        display: flex;
        justify-content: center;
        align-items: center;
      }

      form {
        width: 100%;
        max-width: 450px;
        padding: 35px;
        background: white;
        border-radius: 12px;
        box-shadow: 0 4px 20px rgba(0,0,0,0.08);
        display: flex;
        flex-direction: column;
        gap: 12px;
      }

      label {
        font-size: 14px;
        font-weight: 600;
        color: #2c3e50;
        margin-top: 10px;
      }

      input[type="text"] {
        width: 100%;
        padding: 14px 16px;
        border: 1px solid #ddd;
        border-radius: 8px;
        font-size: 14px;
        background: #f8fafc;
        outline: none;
        transition: all 0.2s;
      }

      input[type="text"]:focus {
        border-color: #3498db;
        background: white;
        box-shadow: 0 0 0 3px rgba(52,152,219,0.1);
      }

      input[type="submit"] {
        margin-top: 20px;
        padding: 15px;
        background: #2c3e50;
        color: white;
        border: none;
        border-radius: 8px;
        font-size: 14px;
        font-weight: 600;
        cursor: pointer;
        transition: all 0.2s;
      }

      input[type="submit"]:hover {
        background: #3498db;
        transform: translateY(-2px);
        box-shadow: 0 4px 12px rgba(52,152,219,0.2);
      }

      input[type="submit"]:active {
        transform: translateY(0);
      }

      @media (max-width: 600px) {
        body {
          padding: 15px;
        }

        form {
          padding: 25px;
        }
      }
    </style>

  </head>
  <body>
  	<form action="023-insertar.php" method="POST">
    	<label for="nombre">Introduce el nombre del alumno</label>
      <input type="text" name="nombre" id="nombre">
      
      <label for="apellidos">Introduce los apellidos del alumno</label>
      <input type="text" name="apellidos" id="apellidos">
      
      <label for="email">Introduce el email del alumno</label>
      <input type="text" name="email" id="email">
      
      <input type="submit">
    </form>
  </body>
</html>