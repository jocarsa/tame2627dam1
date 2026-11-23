<!doctype html>
<html>
	<head>
  	<style>
    	section{display:grid;grid-template-columns:repeat(7,1fr);}
    </style>
  </head>
  <body>
  	<section>
      <?php
        for($dia = 1;$dia<31;$dia++){
          echo "<article>".$dia."</article>";
        }
      ?>
    </section>
	</body>
</html>