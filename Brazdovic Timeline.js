const timelineArray = [ 
    { 
        year: "1889", 
        eventt:  
"Ernestine Vrtock Brazdovic Born", 
    }, 
    { 
        year: "1935", 
        eventt:  
"Anne Married Steve Zelipsky", 
    }, 
    { 
        year: "1947", 
        eventt:  
"Jim Mager Born", 
    }, 
    { 
        year: "1949", 
        eventt:  
"Rick Mager Born", 
    }, 
    { 
        year: "1959", 
        eventt:  
"<a href=\"/MagerFamily/Robert Mager.html\">Bob Mager</a> Born ", 
    }, 
    { 
        year: "2000", 
        eventt:  
"Jonathan Mager Born", 
    }, 
]; 
  
function gfg() { 
    timelineArray.map((e, i) => { 
        let clss = "right"; 
        let dot = "dotRight"; 
        if (i % 2 == 0) { 
            clss = "left"; 
            dot = "dotLeft"; 
        } 
        const year = document.createElement("h3"); 
        year.innerText = e.year; 
        const eventt = document.createElement("p"); 
        eventt.innerHTML = e.eventt; 
        const item = document.createElement("div"); 
        item.appendChild(year); 
        item.appendChild(eventt); 
        item.classList.add("card"); 
        const contain = document.createElement("div"); 
        const li = document.createElement("li"); 
        contain.classList.add(dot); 
        contain.appendChild(item); 
        li.appendChild(contain); 
        li.classList.add(clss); 
        document.getElementById("menu").appendChild(li); 
    }); 
} 
gfg();