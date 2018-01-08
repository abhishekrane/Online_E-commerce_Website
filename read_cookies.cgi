#!/usr/bin/perl  
use DBI;
use CGI;
use CGI::Cookie

$q = new CGI;


#send a blank cookie.  You must insert this into the header before
#printing anything.  Also, using the CGI module makes printing
#content-type: text/html redundant.
my $host = "opatija.sdsu.edu";
my $port = "3306";
my $database = "jadrn051";
my $username = "jadrn051";
my $password = "emulsion";
my $database_source = "dbi:mysql:$database:$host:$port";

    
my $dbh = DBI->connect($database_source, $username, $password) 
or die 'Cannot connect to db';

my $cookie = $q->cookie(-name=>'jadrn051',-value=>'',-path=>'/');
print $q->header(-cookie=>$cookie);
print <<END_CONTENT;
<?xml version="1.0" encoding="utf-8"?>
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN"
        "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
        <html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">

<head>
	<title>Cookie Reader</title>
        	<meta http-equiv="content-type"
                		content="text/html;charset=utf-8" />
            	<meta http-equiv="Content-Style-Type" content="text/css" />
                <link rel="stylesheet" href="http://jadran.sdsu.edu/~jadrn051/proj4/css/bootstrap.min.css"  type="text/css">
    <link rel ="stylesheet" type="text/css" href="http://jadran.sdsu.edu/~jadrn051/proj4/css/confirm.css" />
</head>

<body>


<nav class="navbar navbar-default navbar-fixed-top">
        <div class="container">
            <!-- Brand and toggle get grouped for better mobile display -->
            <div class="navbar-header page-scroll">
                <button type="button" class="navbar-toggle" data-toggle="collapse" data-target="#bs-example-navbar-collapse-1">
                   
                    <span class="icon-bar"></span>
                    <span class="icon-bar"></span>
                    <span class="icon-bar"></span>
                </button>
                <a class="navbar-brand page-scroll" href="http://jadran.sdsu.edu/~jadrn051/proj4/index.html">Bertha's Deluxe Chocolates</a>
            </div>

            <!-- Collect the nav links, forms, and other content for toggling -->
            <div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1">
                <ul class="nav navbar-nav navbar-right">
                    <li class="hidden">
                        <a href="#page-top"></a>
                    </li>
                    <li>
                        <a class="page-scroll" href="http://jadran.sdsu.edu/~jadrn051/proj4/index.html">Home</a>
                    </li>
                    
                    <li>
                        <a class="page-scroll" href="http://jadran.sdsu.edu/~jadrn051/proj4/menu.html">Order Online</a>
                    </li>
                    <li>
                        <a class="page-scroll" href="http://jadran.sdsu.edu/~jadrn051/proj4/products.html">Products</a>
                    </li>
                    <li>
                        <a class="page-scroll" href="http://jadran.sdsu.edu/~jadrn051/proj4/about.html">About Us</a>
                    </li>
                    <li>
                        <a class="page-scroll" href="http://jadran.sdsu.edu/~jadrn051/proj4/contact.html">Contact</a>
                    </li>
                </ul>
            </div>
            <!-- /.navbar-collapse -->
        </div>
        <!-- /.container-fluid -->
    </nav>

    <div>
          
END_CONTENT
my %cookies = $ENV{COOKIE};

print "<p>Confirmation Page</p>\n";
print "<table >\n";

my ($key, $value);
     
%cookies = CGI::Cookie->fetch;

    

my $v = $q->cookie('jadrn051');
  
@rows = split('\|\|',$v);
foreach $row (@rows) {
    ($sku, $qty) = split('\|',$row);
  
my $sth = $dbh->prepare("INSERT INTO report (id, sku, quantity, date) VALUES(0,'$sku','$qty', NOW());
");
$sth->execute();
$sth->finish();
$dbh->disconnect();
    }
    
print "<tr><td><h3>Shiiping Details</h3></td></tr>";
my $name = $q->param('shipfirstName');
print " <tr><td>Name: $name</td></tr>";
my $lastname = $q->param('shiplastName');
print " <tr><td>Last Name: $lastname</td></tr>";
my $address = $q->param('shipaddress1');
print " <tr><td>address1: $address</td></tr>";
my $address1 = $q->param('shipaddress2');
print " <tr><td>address2: $address1</td></tr>\n";
my $city = $q->param('shipcity');
print " <tr><td>city: $city</td></tr>";
my $state = $q->param('shipstate');
print " <tr><td>state: $state</td></tr>";
my $zip = $q->param('shipzip');
print " <tr><td>zip: $zip</td></tr>";


print "<tr><td><h3>Order Details</h3></td></tr>";
my $card = $q->param('cardtype');
print " <tr><td>Card Type: $card</td></tr>";


my $retail = $q->param('retail');
print " <tr><td>Retail $retail</td></tr>";
my $tax = $q->param('tax');
print " <tr><td>Tax $tax</td></tr>";
my $total = $q->param('total');
print " <tr><td>total $total</td></tr>";




     


print "</table>\n";
print "</div>\n";
print "</body>\n";
print "</html>\n";

print "</table>\n";
print "</div>\n";
print "</body>\n";
print "</html>\n";









 



        


