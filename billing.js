function FillBilling(f) {
	alert("adac");
  if(f.billingtoo.checked == true) {
    f.billingname.value = f.shippingname.value;
    f.billingcity.value = f.shippingcity.value;
  }
}