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

print calculadora("1+2*3+4*5+6*7+8*9+10")