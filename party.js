var taipei,result
fetch("taipei.json")
  .then(response => response.json())
  .then(function(json) => {taipei = json});


fetch("result.json")
  .then(response => response.json())
  .then(function(json) => {result = json});


var parties = {};

for(var i in taipei.objects.village.geometries){
    var c = taipei.objects.village.geometries[i].properties.C_Name;
    var t = taipei.objects.village.geometries[i].properties.T_Name;
    var v = taipei.objects.village.geometries[i].properties.V_Name;
    var name = c+t+v;
    var area = c+t;
  console.log(name);
    taipei.objects.village.geometries[i].properties.party = result[name]["party"];
    var party = result[name]["party"];
     
    console.log(name);
    console.log(result[name]);
    
    if(parties.hasOwnProperty(area)){
          if(parties[area].hasOwnProperty(party)){
            parties[area][party] = parties[area][party]+1;
          }else{
             parties[area][party] =1;
          }
          
    }else{
           parties[area] = {};
           parties[area][party] = 1;
    
    }
    

    
}

for(var i in parties){
     var max = 0
     var party = "";
     for(var j in parties[i]){
          if(parties[i][j]> max){
                max = parties[i][j];
                party = j;
          }
     }
     parties[i]["majority"] = party;
}


for(var i in taipei.objects.town.geometries){
    var c = taipei.objects.town.geometries[i].properties.C_Name;
    var t = taipei.objects.town.geometries[i].properties.T_Name;
   console.log(taipei.objects.town.geometries[i].properties);
    var area = c+t;
    taipei.objects.town.geometries[i].properties.party = parties[area]["majority"]
    console.log(parties[area]["majority"]);

      
}
