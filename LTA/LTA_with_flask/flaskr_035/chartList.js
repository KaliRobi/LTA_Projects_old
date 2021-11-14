var ctx = document.getElementById('myChart').getContext('2d');
if (chartExists == undefined) {
console.log('chart created')
    chartOne = new Chart(ctx, {
        type: 'bar',
        data: {
            labels: towns,

            datasets: [{
                label: 'heights in these towns',
                data: heights,

                backgroundColor: [
                  'rgba(128, 128, 0, 0.8)',
                  'rgba(0, 0, 128, 0.8)',
                    


                ],
                borderColor: [
                  'rgba(128, 128, 0, 0.8)',
                  'rgba(0, 0, 128, 0.8)',
                    
                    

                ],
                borderWidth: 1
            }]
        },
        options:
                                  
        { 
          chartArea: {
                  backgroundColor: 'rgb(132, 119, 170)'
              }
        },

        
       }



      ) 
}                         

      else {
          updateChart(chartOne,towns, heights)
          console.log('chart ctx updated')
         
                     }