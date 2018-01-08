

// <!--code by Name:Abhishek RedID: 822056658 -->


var proj4_data;
$(document).ready( function() {

    var tot = 0;
    var retail = 0;
    var tax = 0;
    $.ajax({
  url: "http://jadran.sdsu.edu/perl/jadrn051/get_products.cgi", 
  type: "post",    
  success: function(response){
  
  storeData(response);
  }});
    proj4_data = new Array();

    var cart = new shopping_cart("jadrn051");
    var a ;

     setTimeout( function() { updateDisplay(); }, 500);

    function updateDisplay() {
        var cartArray = cart.getCartArray();
        var toWrite = "";
        var price = 0;
        var total = 0;
       

        var toWrite = "<table>";
        // toWrite += "<tr><th>Title</th><th>Quantity</th></tr>";
        for(i=0; i < cartArray.length; i++) {

            for(j=0;j<proj4_data.length;j++) {
               
                if (proj4_data[j][0] == cartArray[i][0])
                {
                     a = cartArray[i][1]
                  
                        toWrite += "<table border=\"1\">";
                        
                        toWrite += "<tr><td rowspan=\"4\" ><center><img src=\"/~jadrn000/PROJ4_IMAGES/"+
                        proj4_data[j][0]+".jpg\" alt=\""+proj4_data[j][2]+"\""+
                        " width=\"200px\"  /></center></td><td>"+ proj4_data[j][2] +"</td></tr>";     
                      
                        toWrite += "<tr><td>"+ proj4_data[j][6] + " $</td></tr>";
                        
                        
                            
                        toWrite += "<tr><td><input type='button' class='update' id='"+ cartArray[i][0] +"' value='"+ cartArray[i][1] +"' /> box <input type='button' id='remove' name='"+proj4_data[j][0]+ "' value='Remove from Cart' /></td></tr>";

                        toWrite += "<tr><td><input type='button' class='plus' name='"+proj4_data[j][0]+ "' id='"+ cartArray[i][0] +"' value='+' /> <input type='button' class='minus' name='"+proj4_data[j][0]+ "' id='"+ cartArray[i][0] +"' value='-' /></td></tr>";

                        toWrite += "</table><hr />"; 
                        price +=   proj4_data[j][6];
                        total += cartArray[i][1]*proj4_data[j][6];
                        
                }
            }
           
            }
            toWrite += "<hr/><tr><td>Items Total:"+ eval(total).toFixed(2)+"<br/>Tax (@ 8%):"+ eval(0.08*total).toFixed(2)+"<br/>Shipping Charges:$2.00<br/>Net Amount Payable:"+ eval(1.08* total + 2).toFixed(2) + "</td>";
                    
        toWrite += "</table>"; 
        $('#cart').html(toWrite); 
        $('#count').text(cart.size());     
        tot = eval(1.08* total + 2).toFixed(2);
        retail = eval(1 * total).toFixed(2);
        tax = eval(0.08* total).toFixed(2);

        var b = cart.size()

               if(b == 0) {
              
            document.getElementById('modal').style.visibility = 'hidden';

        } else {
            document.getElementById('modal').style.visibility = 'visible';
        }         
        

        } 
        
         

      $(document).on('click','#remove', function(e){
        cart.delete($(e.target).attr("name"));
        updateDisplay();
        }); 

    $(document).on('click','#modal', function(e){
      

   $("#total").val(tot);
    $("#retail").val(retail);
     $("#tax").val(tax);


        }); 

 $(document).on('click','.plus', function(e){
     
        var sku = this.id;
        cart.add(sku,1);
        
        updateDisplay();
        alert(cartArray[i][1]);


        }); 

        $(document).on('click','.minus', function(e){
          
         if( a > 1){
        var sku = this.id;
        cart.sub(sku,1);
        
        updateDisplay();}
        else{
        cart.delete($(e.target).attr("name"));
        updateDisplay();
        }
        


        });           
 

// $(document).on('click', ".buy", function() {  
//         var sku = this.id;
//         cart.add(sku,1);
//         $(this).next().fadeIn(50).fadeOut(2000);
//         });



function clearCart() {
    var cartArray = cart.getCartArray();
    for(var i=0; i<cartArray.length; i++)
        cart.delete(cartArray[i][0]);
}

function storeData(response) {
    var tmpArray = explodeArray(response,';');
    for(var i=0; i < tmpArray.length; i++) {
        innerArray = explodeArray(tmpArray[i],'|');
        proj4_data[i] = innerArray;
        }
    }
    // from http://www.webmasterworld.com/forum91/3262.htm            
function explodeArray(item,delimiter) {
tempArray=new Array(1);
var Count=0;
var tempString=new String(item);

while (tempString.indexOf(delimiter)>0) {
tempArray[Count]=tempString.substr(0,tempString.indexOf(delimiter));
tempString=tempString.substr(tempString.indexOf(delimiter)+1,tempString.length-tempString.indexOf(delimiter)+1);
Count=Count+1
}

tempArray[Count]=tempString;
return tempArray;
}  
   });
