use DBI;
use CGI qw(:standard);
use POSIX;

my $host = "opatija.sdsu.edu";
my $port = "3306";
my $database2 = "jadrn051";
my $username = "jadrn051";
my $password = "emulsion";
my $database_source2 = "dbi:mysql:$database2:$host:$port";

my $database1 = "proj4";
my $database_source1 = "dbi:mysql:$database1:$host:$port";
    


my $dbh2 = DBI->connect($database_source2, $username, $password) 
or die 'Cannot connect to db';


my $dbh1 = DBI->connect($database_source1, $username, $password) 
or die 'Cannot connect to db';


my $sth = $dbh2->prepare("SELECT * FROM report order by sku");
$sth->execute();

print header();

print "<h2>Sales</h2>";

print "<table>";
 
 print "<td>SKU</td><td>Quantity</td><td>Date</td><td>Cost Price</td><td>Retail Price</td><td>Total RetailPrice</td><td>Total CostPrice</td><td>Profit</td>";
my $Cost = 0;
my $Retail = 0;
my $totalCost = 0;
my $totalRetail = 0;
my $profit = 0;
my $Grossprofit = 0;
my $Grosssales = 0;
my $qty = 0;
        my $hi = "";
        while(my @row=$sth->fetchrow_array()) {
    		print "<tr>\n";
    		$hi = @row->[1];
    		print "<td>$hi</td>";
    	     $qty = @row->[2];
    	     print "<td>$qty</td>";
            $time = @row->[3];
    	     print "<td>$time</td>";
    	
        	my $sth1 = $dbh1->prepare("SELECT cost, retail FROM products where sku = '$hi'");
					$sth1->execute();
					while(my @row=$sth1->fetchrow_array()) {
    		    $Retail = @row->[1];
    		    $Cost = @row->[0];
    		    $totalRetail = ($Retail*$qty);
    		    $totalCost = ($Cost*$qty);
    		    $profit = ($totalRetail-$totalCost);
    		    $Grossprofit = ($profit+$Grossprofit);
    		    $Grosssales = ($totalRetail+$Grosssales);
    			foreach $item (@row) { 
    				
        		 print "<td>$item</td>\n";
        		


        	}   
        	print "<td>$totalRetail</td>"; 
        	print "<td>$totalCost</td>"; 
        	print "<td>$profit</td>"; 
        	$sth1->finish();
    		 print "</tr>\n";
    		 $dbh1->disconnect();
    		}


    	}
    	print "<tr><td>Grossprofit: $Grossprofit</td></tr>\n";
    	print "<tr><td>Gross-Sales: $Grosssales</td></tr>";
    	print "</table>\n";
print end_html();
$sth->finish();
$dbh2->disconnect();