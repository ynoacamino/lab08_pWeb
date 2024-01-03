#!"C:\xampp\perl\bin\perl.exe"
use strict;
use warnings;
use CGI;
use utf8;

my $cgi = CGI->new;

my $nombre_universidad = $cgi->param('search') || '';

my $archivo_csv = 'data.csv';

open(my $fh, '<', $archivo_csv);

print "Content-type: text/html\n\n";
print '<html>';
print '<head>';
print '<meta name="author" content="Kay Vogelgesang">';
print '<link href="/xampp/xampp.css" rel="stylesheet" type="text/css">';
print '</head>';
print '<style>* { box-sizing: border-box; margin: 0; padding: 0; font-family: "Roboto", sans-serif; }body { min-height: 100vh; background-color: #f5f5f5; display: flex; flex-direction: column; align-items: center; justify-content: center; }table { border-collapse: collapse; width: 100%; border: 1px solid #ddd; font-family: Arial, sans-serif; } th { background-color: #f2f2f2; border: 1px solid #ddd; padding: 8px; text-align: left; } td { border: 1px solid #ddd; padding: 8px; } </style>';
print '<body>';

print "<h2>Resultados de la consulta:</h2>";
print "<table>";

print '<tr>';
print '<th style="width: 75px">Código</th>';
print '<th style="width: 300px">Nombre</th>';
print '<th style="width: 75px">Periodo</th>';
print '<th style="width: 75px">Ciudad</th>';
print '<th style="width: 600px">Programa</th>';
print '</tr>';

while (my $linea = <$fh>) {
  chomp $linea;
  if ($linea =~ /$nombre_universidad/i) {
    utf8::decode($linea);
    my @campos = split(quotemeta('|'), $linea);
    print "<tr>\n";
    print "<td>". $campos[0] ." </td>\n";
    print "<td>". $campos[1] ." </td>\n";
    print "<td>". $campos[4] ." </td>\n";
    print "<td>". $campos[10] ." </td>\n";
    print "<td>". $campos[16] ." </td>\n";
    print "</tr>\n";
  }
}

print "</table>";
close($fh);

print  "</body></html>";
