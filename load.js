
// <!--code by Name:Abhishek RedID: 822056658 -->



var proj4_data;
var tmpArray;
$(document).ready(function () {
   

    proj4_data = new Array();
    var cart = new shopping_cart("jadrn051");
    $.ajax({
        url:"http://jadran.sdsu.edu/perl/jadrn051/get_products.cgi", 
        success: function(result){    
        storeData(result);
        ShowProducts();
        
        },
    });

    function storeData(response) {
       
        var tmpArray = explodeArray(response,';');
        for(var i=0; i < tmpArray.length; i++) {
                innerArray = explodeArray(tmpArray[i],'|');
                proj4_data[i] = innerArray;
            }   
    }

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

    function ShowProducts(){
   
        tmpString = "";
        tmpString += "<table class=\"load\"><tr>";

        var i = 1 ;
        for(var j=0; j < 8; j++) {
        
                i = Math.floor((Math.random() * (proj4_data.length-1)));
        
               if(j===4){
                     tmpString += " <tr style=\"padding-top: 10px\"> </tr> ";
                }
                tmpString += "<td class=\"ImageTd\" style=\"padding-right: 10px\"><center><img src=\"/~jadrn000/PROJ4_IMAGES/"+
                proj4_data[i][0]+".jpg\" alt=\""+proj4_data[i][2]+"\" /></center></td>"; 
           
        }
         tmpString += "</tr></table>"; 
        var handle = document.getElementById('Products');
        handle.innerHTML = tmpString;

    } 
    });