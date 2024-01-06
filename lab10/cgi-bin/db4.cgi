#!"C:\xampp\perl\bin\perl.exe"
use strict;
use warnings;
use CGI;
use utf8;

my $cgi = CGI->new;

my $year = $cgi->param('year') || '';

my $db_name = 'pweb1';
my $host = 'localhost';
my $port = '3308';
my $user = 'root';
my $password = '11yenaro11';


my $dsn = "DBI:MariaDB:database=$db_name;host=$host;port=$port";


my $dbh = DBI->connect($dsn, $user, $password);

my $sth = $dbh->prepare("SELECT * FROM Movie WHERE year=?");

$sth->execute($year);



$dbh->disconnect();

print "Content-type: text/html\n\n";
print '<html>';
print '<head>';
print '<meta name="author" content="Kay Vogelgesang">';
print '<link href="/xampp/xampp.css" rel="stylesheet" type="text/css">';
print '</head>';
print '<style>* { box-sizing: border-box; margin: 0; padding: 0; font-family: "Roboto", sans-serif; }body { min-height: 100vh; background-color: #f5f5f5; display: flex; flex-direction: column; align-items: center; justify-content: center; }table { border-collapse: collapse; width: 100%; border: 1px solid #ddd; font-family: Arial, sans-serif; } th { background-color: #f2f2f2; border: 1px solid #ddd; padding: 8px; text-align: left; } td { border: 1px solid #ddd; padding: 8px; } </style>';
print '<body>';

print "<h2>Resultados de la consulta:</h2>";

print "<strong> Las peliculas de $year son: </strong";

while( my @row = $sth->fetchrow_array ) {
  print "@row\	n";
}

print  "</body></html>";



