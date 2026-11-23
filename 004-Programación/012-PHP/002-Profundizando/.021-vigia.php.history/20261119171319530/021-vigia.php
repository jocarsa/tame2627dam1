<?php
	$servidor = $_SERVER;
  $plataforma = $servidor['HTTP_SEC_CH_UA_PLATFORM'];
  $navegador = $servidor['HTTP_USER_AGENT'];
  $ip = $servidor['HTTP_HOST'];
  $fecha = $servidor['REQUEST_TIME'];
?>