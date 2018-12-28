//for http://db.cec.gov.tw/histQuery.jsp?voteCode=20181101J1E1&qryType=ctks
var votes = {};
var td = document.querySelectorAll("td > a");

for(var i in td){

fetch(td[i].href)
  .then(function(response) {
   
    return response.text();
  })
  .then(function(html) {

    var parser = new DOMParser(); 
var doc = parser.parseFromString(html, "text/html");
var tr = doc.querySelectorAll("tr.data"); 
var current_area = "";
var current_name = "";
      for(var r in tr){
           
           console.log(tr[r]);
           var data = tr[r].children
         
           var ci = 0;
           if(data.length==10){
           
              current_area = data[0].innerText.slice(-3);
              current_name = data[0].innerText;

              ci = 1;

           }

             let area = current_area;
             let full_name = current_name;
            
            var item = {"area":area,"full_name":full_name,"party":data[4+ci].innerText,"vote":data[5+ci].innerText,"ratio":data[6+ci].innerText};
            if(data[data.length-2].innerText=="*"){
    console.log(item);
             votes[full_name]=item;
                }

    

       
    }
});


}

