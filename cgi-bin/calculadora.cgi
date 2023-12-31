#!"C:\xampp\perl\bin\perl.exe"
use strict;
use warnings;
use CGI;


sub calculadora {
  my ($expresion) = @_;

  $expresion =~ s/\s+//g;

  my @operandos = split /([\+\-\*\/])/, $expresion;

  my @numeros = ();
  my @operadores = ();

  foreach my $elemento (@operandos) {
    if ($elemento =~ /^\d+$/) {
      push @numeros, $elemento;
    } elsif ($elemento =~ /[\+\-\*\/]/) {
      push @operadores, $elemento;
    }
  }

  for(my $i = 0; $i < @operadores; $i++) {
    if ($operadores[$i] eq '*') {
      $numeros[$i] = $numeros[$i] * $numeros[$i + 1];
      splice @numeros, $i + 1, 1;
      splice @operadores, $i, 1;
      $i = $i - 1;
    } elsif ($operadores[$i] eq '/') {
      $numeros[$i] = $numeros[$i] / $numeros[$i + 1];
      splice @numeros, $i + 1, 1;
      splice @operadores, $i, 1;
      $i = $i - 1;
    }
  }

  for(my $i = 0; $i < @operadores; $i++) {
    if ($operadores[$i] eq '+') {
      $numeros[$i] = $numeros[$i] + $numeros[$i + 1];
      splice @numeros, $i + 1, 1;
      splice @operadores, $i, 1;
      $i = $i - 1;
    } elsif ($operadores[$i] eq '-') {
      $numeros[$i] = $numeros[$i] - $numeros[$i + 1];
      splice @numeros, $i + 1, 1;
      splice @operadores, $i, 1;
      $i = $i - 1;
    }
  }
  
  return $numeros[0];
}

my $cgi = CGI->new;

my $expresion = $cgi->param('expresion');

my $respuesta = calculadora($expresion);

print "Content-type: text/html\n\n";
print "<html><head><title>Ejemplo CGI Perl</title><style>* { box-sizing: border-box; margin: 0; padding: 0; font-family: 'Roboto', sans-serif; font-size: 1.2rem; } body { min-height: 100vh; background-color: #f5f5f5; display: flex; flex-direction: column; align-items: center; justify-content: center; } form { display: flex; gap: 20px; } button { cursor: pointer; padding: 10px 20px; border: none; color: white; background-color: #3a3a3a; border-radius: 5px; } input { padding: 10px 20px; border: none; border-radius: 5px; box-shadow: 0 0 5px rgba(0, 0, 0, 0.2); }</style></head><body>";
print "<h1>Hola la respusta es: </h1>";
print "<strong>$respuesta</strong>";
print "</body></html>";