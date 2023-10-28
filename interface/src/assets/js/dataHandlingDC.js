selects = document.querySelectorAll('[name=req]')
console.log(selects[0].dataset.wrd)



function validate(){
    
    for( select of selects ){
        if (select.dataset.wrd == select.value){
            fetch(`http://127.0.0.1:5000/get_data/missing_values`)
            .then(() =>  {
                location.href = 'data_cleaning.html';
            })
        }
    }
}