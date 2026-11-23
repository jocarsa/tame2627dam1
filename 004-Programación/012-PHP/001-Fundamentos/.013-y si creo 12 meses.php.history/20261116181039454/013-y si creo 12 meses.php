<!doctype html>
<html>
	<head>
  	<style>
    	section{display:grid;grid-template-columns:repeat(7,1fr);border:3px solid grey;}
      article{border:1px solid grey;height:50px;}
    </style>
  </head>
  <body>
  	<?php for($mes = 1;$mes <= 12;$mes++){?>
      <section>
        <?php
          for($dia = 1;$dia<31;$dia++){
            echo "<article>".$dia."</article>";
          }
        ?>
      </section>
    <?php } ?>
	</body>
</html>